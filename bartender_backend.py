# bartender_backend.py

from models import Product
from data_import import (
    import_beers,
    import_beers_bought,
    import_beers_sold,
    import_payments,
    import_users
)
from undo_manager import UndoRedoManager
from commands import *

# ---------------------
# Model Classes (Order, Employee)
# ---------------------
# In bartender_backend.py
class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        # Each item is a dictionary: {"product": product, "quantity": qty, "discount": discount}
        self.items = []
        self._undo_stack = []  # Stores snapshots (deep copies) of self.items
        self._redo_stack = []

    def _save_state(self):
        # Save a deep copy of the current items.
        self._undo_stack.append([item.copy() for item in self.items])
        self._redo_stack.clear()

    def add_item(self, product, quantity, discount=0):
        self._save_state()
        # Check if an item with the same product and discount already exists.
        for item in self.items:
            if item["product"].id == product.id and item["discount"] == discount:
                item["quantity"] += quantity
                print(f"Updated {product.name}: new quantity = {item['quantity']}")
                return
        # Otherwise, add as a new order line.
        self.items.append({"product": product, "quantity": quantity, "discount": discount})
        print(f"Added {quantity} of '{product.name}' to Order {self.order_id}.")

    def remove_item_quantity(self, product, quantity, discount=0):
        # Remove a given quantity of a product (with matching discount) from the order.
        for i, item in enumerate(self.items):
            if item["product"].id == product.id and item["discount"] == discount:
                self._save_state()
                if item["quantity"] > quantity:
                    item["quantity"] -= quantity
                    print(f"Reduced quantity of '{product.name}' by {quantity}. New quantity: {item['quantity']}")
                    return
                else:
                    # If quantity to remove is equal to or exceeds current, remove the item entirely.
                    self.items.pop(i)
                    print(f"Removed '{product.name}' from order.")
                    return
        print("Product not found in order.")

    def total(self):
        return sum(item["product"].price * item["quantity"] * (1 - item["discount"] / 100)
                   for item in self.items)

    def undo(self):
        if self._undo_stack:
            self._redo_stack.append([item.copy() for item in self.items])
            self.items = self._undo_stack.pop()
            print(f"Order {self.order_id} undone. Current items: {self.items}")
        else:
            print("No undo available for Order", self.order_id)

    def redo(self):
        if self._redo_stack:
            self._undo_stack.append([item.copy() for item in self.items])
            self.items = self._redo_stack.pop()
            print(f"Order {self.order_id} redone. Current items: {self.items}")
        else:
            print("No redo available for Order", self.order_id)

    def __repr__(self):
        items_str = ", ".join(f"{item['product'].name} x{item['quantity']} ({item['discount']}% off)" for item in self.items)
        return f"Order(ID: {self.order_id}, Items: [{items_str}])"



class Employee:
    def __init__(self, employee_id, name, role):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.logged_in = False

    def login(self):
        self.logged_in = True
        print(f"{self.name} logged in as {self.role}")

    def logout(self):
        self.logged_in = False
        print(f"{self.name} logged out")


class BartenderController:
    def __init__(self, employee):
        self.employee = employee
        self.products_db = import_beers('DBFilesJSON/dutchman_table_sbl_beer.json')
        self.payments_db = import_payments('DBFilesJSON/dutchman_table_payments.json')
        self.undo_manager = UndoRedoManager()
        self.current_order = None  # Only one active order

    def login_employee(self):
        self.employee.login()

    def logout_employee(self):
        self.employee.logout()

    # --- Product functions (global actions) remain unchanged ---
    def get_product_ids(self):
        return list(self.products_db.keys())

    def get_product(self, product_id):
        return self.products_db.get(product_id)

    def remove_product_from_menu(self, product_id):
        command = RemoveProductCommand(self.products_db, product_id)
        self.undo_manager.execute_command(command)

    def modify_product_price(self, product_id, new_price):
        command = ModifyPriceCommand(self.products_db, product_id, new_price)
        self.undo_manager.execute_command(command)

    def offer_discount(self, product_id, discount_percentage):
        command = OfferDiscountCommand(self.products_db, product_id, discount_percentage)
        self.undo_manager.execute_command(command)

    def update_stock(self, product_id, new_stock):
        command = UpdateStockCommand(self.products_db, product_id, new_stock)
        self.undo_manager.execute_command(command)

    # --- Order functions ---
    def create_order(self):
        if self.current_order is None:
            self.current_order = Order(101)
            print(f"Created new active order with ID {self.current_order.order_id}.")
        else:
            print("An active order already exists.")
        return self.current_order

    def add_item_to_current_order(self, product_id, quantity):
        if self.current_order is None:
            print("No active order. Create an order first.")
            return None
        product = self.get_product(product_id)
        if product:
            # Enforce stock constraint: the total quantity in the order cannot exceed current stock.
            current_qty = sum(item["quantity"] for item in self.current_order.items if item["product"].id == product_id)
            if current_qty + quantity > product.stock_count:
                print(f"Cannot add {quantity} of '{product.name}'. Only {product.stock_count - current_qty} available.")
                return None
            self.current_order.add_item(product, quantity)
        else:
            print("Product not found.")
        return self.current_order

    def remove_item_from_current_order(self, product_id, quantity):
        if self.current_order is None:
            print("No active order.")
            return None
        product = self.get_product(product_id)
        if product:
            self.current_order.remove_item_quantity(product, quantity)
        else:
            print("Product not found.")
        return self.current_order

    def offer_discount_on_order(self, product_id, discount_percentage):
        if self.current_order is None:
            print("No active order.")
            return
        found = False
        self.current_order._save_state()
        for item in self.current_order.items:
            if item["product"].id == product_id:
                item["discount"] = discount_percentage
                found = True
                print(f"Applied discount of {discount_percentage}% on '{item['product'].name}' in order.")
        if not found:
            print("Product not found in current order.")

    def finish_current_order(self):
        if self.current_order is None:
            print("No active order to finish.")
            return None
        total = self.current_order.total()
        # Update stock for each product based on quantities in the order.
        for item in self.current_order.items:
            product = item["product"]
            product.stock_count -= item["quantity"]
        print(f"Finished order {self.current_order.order_id} with total {total}. Stock updated.")
        self.current_order = None
        return total

    # --- Global Undo/Redo for product actions ---
    def undo(self):
        self.undo_manager.undo()

    def redo(self):
        self.undo_manager.redo()

    # --- Order-Level Undo/Redo ---
    def order_undo(self):
        if self.current_order:
            self.current_order.undo()
        else:
            print("No active order to undo.")

    def order_redo(self):
        if self.current_order:
            self.current_order.redo()
        else:
            print("No active order to redo.")
