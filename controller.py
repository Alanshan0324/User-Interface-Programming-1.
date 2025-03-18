# controller.py

import copy
from typing import List, Dict, Any
from datetime import datetime
from models import Product
from data_import import (
    import_beers,
    import_beers_bought,
    import_beers_sold,
    import_payments,
    import_users, import_products
)
from undo_manager import UndoRedoManager
from commands import *
LANGUAGES = {
    'en': {  # English

        'logout': "Logout",
        'create_order_button': "Create Order",
        'add_item_button': "Add Item to Order",
        'remove_item_button': "Remove Item from Order",
        'finish_order_button': "Finish Order",
        'undo_button': "Undo",
        'redo_button': "Redo",
        'language_label': "Language",
        'product_label': "Products",
        'sort_label': "Sort by:",
        'product_id_label': "Product ID:",
        'new_price_label': "New Price:",
        'new_stock_label': "New Stock:",
        'quantity_label': "Quantity:",
        'remove_quantity_label': "Quantity to Remove:",
        'current_order_label': "Current Order:",
        'order_management_label': "--- Order Management ---",
        'refill_low_stock_button': "Refill Low Stock Items",
        'alert_security_button': "Alert Security",
        'refresh_products_button': "Refresh Products",
        'modify_price_button': "Modify Price",
        'remove_product_button': "Remove Product",
        'update_stock_button': "Update Stock",
        "order_undo": "Order Undo",
        "order_redo": "Order Redo",
        "current_order": "Current Order:",
        'do_accounting': "Do accounting"
        # 其他按鈕和標籤文字...
    },
    'zh': {  # 中文

        'logout': "登出",
        'create_order_button': "創建訂單",
        'add_item_button': "添加項目",
        'remove_item_button': "移除項目",
        'finish_order_button': "完成訂單",
        'undo_button': "撤銷",
        'redo_button': "重做",
        'language_label': "語言",
        'product_label': "產品",
        'sort_label': "排序方式:",
        'product_id_label': "產品 ID:",
        'new_price_label': "新價格:",
        'new_stock_label': "新庫存:",
        'quantity_label': "數量:",
        'remove_quantity_label': "移除數量:",
        'current_order_label': "當前訂單:",
        'order_management_label': "--- 訂單管理 ---",
        'refill_low_stock_button': "補充低庫存商品",
        'alert_security_button': "警報安全",
        'refresh_products_button': "刷新產品",
        'modify_price_button': "修改價格",
        'remove_product_button': "移除產品",
        'update_stock_button': "更新庫存",
        "order_undo": "訂單撤銷",
        "order_redo": "訂單重做",
        "current_order": "當前訂單:",
        'do_accounting': "做會計"

        # 其他按鈕和標籤文字...
    },
    'sv': {  # Swedish

        'logout': "Logga ut",
        'create_order_button': "Skapa Order",
        'add_item_button': "Lägg till Artikel",
        'remove_item_button': "Ta bort Artikel",
        'finish_order_button': "Avsluta Order",
        'undo_button': "Ångra",
        'redo_button': "Gör om",
        'language_label': "Språk",
        'product_label': "Produkter",
        'sort_label': "Sortera efter:",
        'product_id_label': "Produkt ID:",
        'new_price_label': "Nytt Pris:",
        'new_stock_label': "Nytt Lager:",
        'quantity_label': "Kvantitet:",
        'remove_quantity_label': "Kvantitet att Ta Bort:",
        'current_order_label': "Aktuell Order:",
        'order_management_label': "--- Orderhantering ---",
        'refill_low_stock_button': "Fyll på Lågt Lager",
        'alert_security_button': "Larma Säkerhet",
        'refresh_products_button': "Uppdatera Produkter",
        'modify_price_button': "Ändra Pris",
        'remove_product_button': "Ta Bort Produkt",
        'update_stock_button': "Upp",
        "order_undo": "OrderÅngra",
        "order_redo": "OrderGör om",
        "current_order": "Aktuell Order:",
        'do_accounting': "Utför bokföring"



        # 其他按鈕和標籤文字...
    }
}
# ---------------------
# Model Classes (Payment, Order, Employee)
# ---------------------
# In controller.py

class Payment:
    def __init__(self, payment_id, order_id, amount, date=None, method="cash"):
        self.payment_id = payment_id
        self.order_id = order_id
        self.amount = amount
        self.date = date if date is not None else datetime.now()
        self.method = method

    def __repr__(self):
        return (f"Payment(id={self.payment_id}, order_id={self.order_id}, amount={self.amount}, "
                f"date={self.date.strftime('%Y-%m-%d %H:%M:%S')}, method='{self.method}')")

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
        return sum(float(item["product"].price) * float(item["quantity"]) * (1 - float(item["discount"]) / 100)
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

class Controller:
    def __init__(self, employee, menu_model=None, view=None, language_model=None):
        self.employee = employee
        self.menu_model = menu_model         # Typically contains static menu items
        self.view = view                     # A POSView instance from your customer order interface
        self.language_model = language_model # A LanguageModel instance for translations
        self.payment_id_counter = 1
        self.all_payments: List[Payment] = []  # Stores finished orders as Payment records

        # Load product and payment data from JSON
        self.products_db = import_products('DBFilesJSON/products.json')
        self.payments_db = []
        self.undo_manager = UndoRedoManager()
        self.current_order = None  # Will be created when needed
        self.current_language = 'en'
        self.order_id_counter = 101  # Simple counter for order IDs

        # If a view is provided, register callbacks for customer order interactions.
        if self.view is not None:
            self.view.set_menu_model(self.menu_model)
            self.view.set_on_language_change_callback(self.on_language_change)
            self.view.set_on_add_item_callback(self.add_to_order_drag_drop)
            self.view.set_on_delete_button_callback(self.view.on_delete_button_clicked)
            self.view.set_on_remove_item_callback(self.remove_from_order)
            self.view.set_on_decrease_quantity_callback(self.decrease_item_quantity)
            self.view.clear_button.config(command=self.clear_order)
            self.view.checkout_button.config(command=self.checkout)
            self.view.split_bill_button.config(command=self.split_bill)
            self.view.add_person_btn.config(command=self.add_person)
            self.view.remove_person_btn.config(command=self.remove_person)
            self.view.selected_category.trace("w", self.on_category_change)
            self.view.on_category_change_callback = self.on_category_change

            self.reset_order()
            self.initialize_menu()
            self.update_person_spinbox_range()

    # --- General Employee & Language Methods ---
    def get_translation(self, key):
        return LANGUAGES.get(self.current_language, {}).get(key)

    def set_language(self, language_code):
        if language_code in LANGUAGES:
            self.current_language = language_code
        else:
            print(f"Unsupported language: {language_code}")

    def login_employee(self):
        self.employee.login()

    def logout_employee(self):
        self.employee.logout()

    # --- Product Functions ---
    def get_product_ids(self):
        return [product.id for product in self.products_db]

    def get_product(self, product_id):
        for product in self.products_db:
            if product.id == product_id:
                return product
        return None

    def remove_product_from_menu(self, product_id):
        product = self.get_product(product_id)
        if product:
            command = RemoveProductCommand(self.products_db, product)
            self.undo_manager.execute_command(command)
        else:
            print(f"Product with id {product_id} not found.")

    def modify_product_price(self, product_id, new_price):
        product = self.get_product(product_id)
        if product:
            command = ModifyPriceCommand(self.products_db, product, new_price)
            self.undo_manager.execute_command(command)
        else:
            print(f"Product with id {product_id} not found.")

    def offer_discount(self, product_id, discount_percentage):
        product = self.get_product(product_id)
        if product:
            command = OfferDiscountCommand(self.products_db, product, discount_percentage)
            self.undo_manager.execute_command(command)
        else:
            print(f"Product with id {product_id} not found.")

    def update_stock(self, product_id, new_stock):
        product = self.get_product(product_id)
        if product:
            command = UpdateStockCommand(self.products_db, product, new_stock)
            self.undo_manager.execute_command(command)
        else:
            print(f"Product with id {product_id} not found.")

    def refill_low_stock_items(self, refill_amount=20):
        command = RefillLowStockCommand(self.products_db, refill_amount=refill_amount, threshold=5)
        self.undo_manager.execute_command(command)
        return len(command.affected_products)

    def do_accounting(self):
        """
        Aggregates all finished orders (payments) and returns a summary string.
        """
        if not self.all_payments:
            return "No orders finished yet."
        total_sales = sum(payment.amount for payment in self.all_payments)
        order_count = len(self.all_payments)
        summary_lines = [
            f"Finished Orders: {order_count}",
            f"Total Sales: ${total_sales:.2f}",
            "",
            "Order Details:"
        ]
        for payment in self.all_payments:
            summary_lines.append(
                f"Order {payment.order_id}: ${payment.amount:.2f} on {payment.date.strftime('%Y-%m-%d %H:%M')}"
            )
        return "\n".join(summary_lines)

    def add_order_to_payment_db(self, order_id, items, total):
        self.payments_db.append(Payment(order_id, items, total))

    def undo(self):
        self.undo_manager.undo()

    def redo(self):
        self.undo_manager.redo()

    # --- Order Functions ---
    def create_order(self):
        if self.current_order is None:
            self.current_order = Order(self.order_id_counter)
            self.order_id_counter += 1
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
            # Enforce stock constraint (convert stock_count to int if necessary)
            current_qty = sum(item["quantity"] for item in self.current_order.items if item["product"].id == product_id)
            if current_qty + quantity > int(product.stock_count):
                print(f"Cannot add {quantity} of '{product.name}'. Only {int(product.stock_count) - current_qty} available.")
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
        for item in self.current_order.items:
            product = item["product"]
            product.stock_count -= item["quantity"]
        print(f"Finished order {self.current_order.order_id} with total {total}. Stock updated.")
        # Record the payment, storing a copy of the order items for accounting.
        payment = Payment(
            payment_id=self.payment_id_counter,
            order_id=self.current_order.order_id,
            amount=total,
            date=datetime.now()
        )
        self.all_payments.append(payment)
        self.payment_id_counter += 1
        self.current_order = None
        return total

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

    # --- Methods for Customer Interface (Callbacks from the View) ---
    def on_language_change(self):
        self.initialize_menu()
        self.update_all_displays()

    def remove_from_order(self, item_name, person_index=None):
        # Look up the corresponding menu item using the menu model.
        menu_items = self.menu_model.get_menu_items()
        target_item = next((item for item in menu_items if item.name == item_name), None)
        if target_item:
            people_count = self.view.people_count.get()
            if people_count > 1 and person_index is not None:
                self.current_order.remove_item(target_item.id, sub_order_index=person_index)
            else:
                self.current_order.remove_item(target_item.id)
            self.update_all_displays()
        else:
            print("Item not found in menu model.")

    def decrease_item_quantity(self, item_name, person_index=None):
        menu_items = self.menu_model.get_menu_items()
        target_item = next((item for item in menu_items if item.name == item_name), None)
        if target_item:
            people_count = self.view.people_count.get()
            if people_count > 1 and person_index is not None:
                self.current_order.remove_item(target_item.id, quantity=1, sub_order_index=person_index)
            else:
                self.current_order.remove_item(target_item.id, quantity=1)
            self.update_all_displays()
        else:
            print("Item not found in menu model.")

    def initialize_menu(self):
        menu_items = self.menu_model.get_menu_items()
        categories = sorted(set(item.category for item in menu_items))
        self.view.create_menu_items(menu_items, categories)

    def on_category_change(self, *args):
        self.initialize_menu()

    def reset_order(self):
        self.current_order = Order(self.order_id_counter)
        self.order_id_counter += 1
        self.view.update_individual_tabs(1)
        self.update_all_displays()

    def add_person(self):
        current_count = self.view.people_count.get()
        self.view.people_count.set(current_count + 1)
        self.update_person_spinbox_range()
        if len(self.current_order.sub_orders) < current_count + 1:
            self.current_order.sub_orders.append([])
        self.view.update_individual_tabs(current_count + 1)
        self.update_all_displays()

    def remove_person(self):
        current_count = self.view.people_count.get()
        if current_count > 1:
            self.view.people_count.set(current_count - 1)
            self.update_person_spinbox_range()
            if len(self.current_order.sub_orders) > current_count - 1:
                self.current_order.sub_orders.pop()
            self.view.update_individual_tabs(current_count - 1)
            self.update_all_displays()

    def update_all_displays(self):
        all_items = self.current_order.get_all_items()
        split_bills = self.current_order.get_split_bills()
        self.view.update_order_display(all_items, self.current_order.total, split_bills)

    def update_person_spinbox_range(self):
        current_count = self.view.people_count.get()
        self.view.person_spinbox.config(from_=1, to=current_count)
        if self.view.current_person.get() > current_count:
            self.view.current_person.set(current_count)

    def add_to_order_drag_drop(self, menu_item, person_index=None):
        if menu_item:
            people_count = self.view.people_count.get()
            if people_count > 1 and person_index is not None:
                self.current_order.add_item(menu_item, sub_order_index=person_index)
            else:
                self.current_order.add_item(menu_item)
            self.update_all_displays()

    def split_bill(self):
        if self.view.people_count.get() <= 1:
            self.view.show_message(self.language_model.get_text("not_group_order"))
            return
        split_bills = self.current_order.get_split_bills()
        if not split_bills or all(not items for items, _ in split_bills):
            self.view.show_message(self.language_model.get_text("no_items_to_split"))
            return
        self.view.display_split_bills(split_bills)

    def clear_order(self):
        self.reset_order()
        self.view.people_count.set(1)
        self.update_person_spinbox_range()

    def checkout(self):
        if not self.current_order.get_all_items():
            self.view.show_message(self.language_model.get_text("order_is_empty"))
            return
        self.current_order.table_number = self.view.table_number.get() if self.view.table_number.get() else None
        table_info = f" {self.language_model.get_text('for_table')} {self.current_order.table_number}" if self.current_order.table_number else ""
        group_info = f" ({self.language_model.get_text('group_order')})" if self.current_order.is_group_order() else ""
        self.view.show_message(f"{self.language_model.get_text('order')}{table_info}{group_info} {self.language_model.get_text('completed')}! {self.language_model.get_text('total')}: ${self.current_order.total:.2f}")
        self.clear_order()


if __name__ == "__main__":
    employee = Employee(1001, "Alice", "Bartender")

    controller = Controller(employee)
    controller.login_employee()