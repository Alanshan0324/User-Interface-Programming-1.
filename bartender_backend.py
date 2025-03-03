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
class Order:
    def __init__(self, order_id, table_number):
        self.order_id = order_id
        self.table_number = table_number
        self.items = []  # list of tuples: (Product, quantity)
        self._undo_stack = []  # Internal stack for undo states
        self._redo_stack = []  # Internal stack for redo states

    def _save_state(self):
        """Save a copy of the current items state before modification."""
        # A shallow copy is enough since Product objects are immutable in this context.
        self._undo_stack.append(self.items.copy())
        # Clear the redo stack whenever a new change is made.
        self._redo_stack.clear()

    def add_item(self, product, quantity):
        self._save_state()
        self.items.append((product, quantity))
        print(f"Added {quantity} of '{product.name}' to Order {self.order_id}.")

    def remove_item(self, product):
        self._save_state()
        self.items = [item for item in self.items if item[0] != product]
        print(f"Removed '{product.name}' from Order {self.order_id}.")

    def total(self):
        return sum(product.price * quantity for product, quantity in self.items)

    def undo(self):
        if self._undo_stack:
            self._redo_stack.append(self.items.copy())
            self.items = self._undo_stack.pop()
            print(f"Order {self.order_id} undone. Current items: {self.items}")
        else:
            print("No undo available for Order", self.order_id)

    def redo(self):
        if self._redo_stack:
            self._undo_stack.append(self.items.copy())
            self.items = self._redo_stack.pop()
            print(f"Order {self.order_id} redone. Current items: {self.items}")
        else:
            print("No redo available for Order", self.order_id)

    def __repr__(self):
        items_str = ", ".join(f"{prod.name} x{qty}" for prod, qty in self.items)
        return f"Order(ID: {self.order_id}, Table: {self.table_number}, Items: [{items_str}])"


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


# ---------------------
# Controller Class for Bartender Functions
# ---------------------
class BartenderController:
    def __init__(self, employee, orders_db):
        self.employee = employee
        self.products_db = import_beers('DBFilesJSON/dutchman_table_sbl_beer.json')  # dictionary: product_id -> Product
        self.orders_db = orders_db      # dictionary: order_id -> Order
        self.payments_db = import_payments('DBFilesJSON/dutchman_table_payments.json')
        self.undo_manager = UndoRedoManager()

    def login_employee(self):
        self.employee.login()

    def logout_employee(self):
        self.employee.logout()

    def view_products(self):
        return list(self.products_db.values())

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

    def get_order_for_table(self, table_number):
        for order in self.orders_db.values():
            if order.table_number == table_number:
                return order
        print("No active order for this table.")
        return None

    def update_order(self, order_id, modifications):
        if order_id in self.orders_db:
            order = self.orders_db[order_id]
            modifications(order)
            print(f"Order {order_id} updated.")
        else:
            print("Order not found.")

    def undo(self):
        self.undo_manager.undo()

    def redo(self):
        self.undo_manager.redo()


# ---------------------
# Demo
# ---------------------
if __name__ == "__main__":
    # Define file paths (adjust as needed)
    beers_bought_file = 'DBFilesJSON/dutchman_table_beers_bought.json'
    beers_sold_file = 'DBFilesJSON/dutchman_table_beers_sold.json'
    payments_file = 'DBFilesJSON/dutchman_table_payments.json'
    sbl_beers_file = 'DBFilesJSON/dutchman_table_sbl_beer.json'
    users_file = 'DBFilesJSON/dutchman_table_users.json'

    # Import data using functions from data_import.py
    beers_bought_data = import_beers_bought(beers_bought_file)
    beers_sold_data = import_beers_sold(beers_sold_file)
    payments_data = import_payments(payments_file)
    products_db = import_beers(sbl_beers_file)
    users_data = import_users(users_file)

    # Create a sample orders database for demonstration
    order1 = Order(101, 1)
    sample_product = products_db.get(10001)
    if sample_product:
        order1.add_item(sample_product, 2)
    orders_db = import_beers('DBFilesJSON/dutchman_table_sbl_beer.json')

    # Create an employee (bartender)
    bartender_employee = Employee(1001, "Alice", "Bartender")

    # Instantiate the controller with the employee and imported data
    controller = BartenderController(bartender_employee, orders_db)

    # Simulate bartender actions:
    controller.login_employee()

    # Remove a product (this action is undoable)
    controller.remove_product_from_menu(10001)

    # Modify product price (this action is undoable)
    controller.modify_product_price(10001, 45.0)

    print("\n--- Demonstrating undo/redo ---")
    order1.add_item(sample_product, 3)
    print(order1.__repr__())
    order1.undo()
    print(order1.__repr__())
    order1.redo()
    print(order1.__repr__())

    print("\n--- View products ---")
    controller.view_products()

    # Demonstrate undo/redo:
    print("\n--- Undoing last action ---")
    controller.undo()

    print("\n--- Redoing last undone action ---")
    controller.redo()

    controller.logout_employee()
