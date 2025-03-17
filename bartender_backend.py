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



        # 其他按鈕和標籤文字...
    }
}
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
        
        self.current_language = 'en'  # Default language is English
    
    def get_translation(self, key):
        return LANGUAGES.get(self.current_language, {}).get(key)
    def set_language(self, language_code):
        """設定語言"""
        if language_code in LANGUAGES:
            self.current_language = language_code
        else:
            print(f"Unsupported language: {language_code}")

       


    

        
   

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

    def do_accounting(self):
        """
        Perform a simple accounting simulation:
         - Total cost from beers bought (sum of amount * price)
         - Total payments from table payments
         - Total number of beers sold (count of records)
         - Net revenue = total payments - total cost
        """
        beers_bought = import_beers_bought('DBFilesJSON/dutchman_table_beers_bought.json')
        beers_sold = import_beers_sold('DBFilesJSON/dutchman_table_beers_sold.json')
        payments = import_payments('DBFilesJSON/dutchman_table_payments.json')

        total_cost = sum(entry['amount'] * entry['price'] for entry in beers_bought)
        total_payments = sum(entry['amount'] for entry in payments)
        total_beers_sold = len(beers_sold)
        net_revenue = total_payments - total_cost

        summary = (
            f"Total Cost (Beers Bought): {total_cost:.2f}\n"
            f"Total Payments: {total_payments:.2f}\n"
            f"Total Beers Sold: {total_beers_sold}\n"
            f"Net Revenue: {net_revenue:.2f}"
        )
        return summary

    def refill_low_stock_items(self, refill_amount=100):
        """
        Refill all products that have a stock lower than 5.
        Sets stock_count to refill_amount (default 100) for those products.
        Returns the count of products refilled.
        """
        count = 0
        for product in self.products_db.values():
            if product.stock_count < 5:
                product.stock_count = refill_amount
                count += 1
        print(f"Refilled {count} items with low stock.")
        return count

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
