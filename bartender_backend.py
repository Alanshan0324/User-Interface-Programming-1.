# bartender_backend.py

from models import Product

from data_import import (
    import_beers,
    import_beers_bought,
    import_beers_sold,
    import_payments,
    import_users
)

# ---------------------
# Model Classes
# ---------------------
class Order:
    def __init__(self, order_id, table_number):
        self.order_id = order_id
        self.table_number = table_number
        self.items = []  # list of tuples: (Product, quantity)

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def remove_item(self, product):
        self.items = [item for item in self.items if item[0] != product]

    def total(self):
        return sum(product.price * quantity for product, quantity in self.items)

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
    def __init__(self, employee, products_db, orders_db):
        self.employee = employee
        self.products_db = products_db  # dictionary: product_id -> Product
        self.orders_db = orders_db      # dictionary: order_id -> Order

    def login_employee(self):
        self.employee.login()

    def logout_employee(self):
        self.employee.logout()

    def view_products(self):
        return list(self.products_db.values())

    def remove_product_from_menu(self, product_id):
        if product_id in self.products_db:
            self.products_db[product_id].available = False
            print(f"Product '{self.products_db[product_id].name}' removed from menu.")
        else:
            print("Product not found.")

    def modify_product_price(self, product_id, new_price, reason):
        if product_id in self.products_db:
            old_price = self.products_db[product_id].price
            self.products_db[product_id].price = new_price
            print(f"Price of '{self.products_db[product_id].name}' changed from {old_price} to {new_price}. Reason: {reason}")
        else:
            print("Product not found.")

    def offer_discount(self, product_id, discount_percentage, reason):
        if product_id in self.products_db:
            product = self.products_db[product_id]
            discounted_price = round(product.price * (1 - discount_percentage / 100), 2)
            print(f"Offering discount for '{product.name}': Original Price {product.price}, Discounted Price {discounted_price}. Reason: {reason}")
            product.price = discounted_price
        else:
            print("Product not found.")

    def update_stock(self, product_id, new_stock):
        if product_id in self.products_db:
            self.products_db[product_id].stock_count = new_stock
            print(f"Stock for '{self.products_db[product_id].name}' updated to {new_stock}.")
        else:
            print("Product not found.")

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


# demo
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

    # # Debug print the imported data
    # print("Imported Beers Bought:")
    # print(beers_bought_data)
    # print("\nImported Beers Sold:")
    # print(beers_sold_data)
    # print("\nImported Payments:")
    # print(payments_data)
    # print("\nImported Products:")
    # for product in products_db.values():
    #     print(product)
    # print("\nImported Users:")
    # print(users_data)

    # Create a sample orders database for demonstration
    orders_db = {}
    order1 = Order(101, 1)
    # Add an item from the imported products (using a sample product id, e.g., 10001)
    sample_product = products_db.get(10001)
    if sample_product:
        order1.add_item(sample_product, 2)
    orders_db[101] = order1

    # Create an employee (bartender)
    bartender_employee = Employee(1001, "Alice", "Bartender")

    # Instantiate the controller with the employee and imported data
    controller = BartenderController(bartender_employee, products_db, orders_db)

    # Simulate bartender actions:
    controller.login_employee()

    # print("\nAvailable Products:")
    # for product in controller.view_products():
    #     print(product)

    # Remove a product from the menu (example)
    controller.remove_product_from_menu(10001)

    # Modify product price (example)
    controller.modify_product_price(10001, 45.0, "Promotional discount due to service delay")

    # Offer discount on a product (example)
    controller.offer_discount(10001, 20, "VIP discount")

    # Update stock for a product (example)
    controller.update_stock(10001, 80)

    # Retrieve and display the order for table 1
    order = controller.get_order_for_table(1)
    if order:
        print("\nOrder Details (Before Update):", order)

    # Update order: remove the sample product (example)
    def remove_sample_product(order):
        order.items = [item for item in order.items if item[0].id != 10001]

    controller.update_order(101, remove_sample_product)
    print("Order Details (After Update):", orders_db[101])

    controller.logout_employee()
