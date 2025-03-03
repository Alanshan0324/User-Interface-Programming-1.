# commands.py

class Command:
    def execute(self):
        raise NotImplementedError("Must implement execute()")

    def undo(self):
        raise NotImplementedError("Must implement undo()")


# Command to modify a product's price.
class ModifyPriceCommand(Command):
    def __init__(self, products_db, product_id, new_price):
        self.products_db = products_db
        self.product_id = product_id
        self.new_price = new_price
        self.old_price = None

    def execute(self):
        if self.product_id in self.products_db:
            product = self.products_db[self.product_id]
            self.old_price = product.price
            product.price = self.new_price
            print(f"Price of '{product.name}' changed from {self.old_price} to {self.new_price}.")
        else:
            print("Product not found.")

    def undo(self):
        if self.product_id in self.products_db and self.old_price is not None:
            product = self.products_db[self.product_id]
            product.price = self.old_price
            print(f"Undo: Price of '{product.name}' restored to {self.old_price}.")


# Command to remove a product from the menu.
class RemoveProductCommand(Command):
    def __init__(self, products_db, product_id):
        self.products_db = products_db
        self.product_id = product_id
        self.previous_state = None  # Save the previous availability status

    def execute(self):
        if self.product_id in self.products_db:
            product = self.products_db[self.product_id]
            self.previous_state = product.available
            product.available = False
            print(f"Product '{product.name}' removed from menu.")
        else:
            print("Product not found.")

    def undo(self):
        if self.product_id in self.products_db and self.previous_state is not None:
            product = self.products_db[self.product_id]
            product.available = self.previous_state
            print(f"Undo: Product '{product.name}' restored to menu.")


# Command to offer a discount on a product.
class OfferDiscountCommand(Command):
    def __init__(self, products_db, product_id, discount_percentage):
        self.products_db = products_db
        self.product_id = product_id
        self.discount_percentage = discount_percentage
        self.old_price = None

    def execute(self):
        if self.product_id in self.products_db:
            product = self.products_db[self.product_id]
            self.old_price = product.price
            discounted_price = round(product.price * (1 - self.discount_percentage / 100), 2)
            product.price = discounted_price
            print(
                f"Offering discount for '{product.name}': Original Price {self.old_price}, Discounted Price {discounted_price}.")
        else:
            print("Product not found.")

    def undo(self):
        if self.product_id in self.products_db and self.old_price is not None:
            product = self.products_db[self.product_id]
            product.price = self.old_price
            print(f"Undo: Discount removed. Price of '{product.name}' restored to {self.old_price}.")


# Command to update the stock count of a product.
class UpdateStockCommand(Command):
    def __init__(self, products_db, product_id, new_stock):
        self.products_db = products_db
        self.product_id = product_id
        self.new_stock = new_stock
        self.old_stock = None

    def execute(self):
        if self.product_id in self.products_db:
            product = self.products_db[self.product_id]
            self.old_stock = product.stock_count
            product.stock_count = self.new_stock
            print(f"Stock for '{product.name}' updated from {self.old_stock} to {self.new_stock}.")
        else:
            print("Product not found.")

    def undo(self):
        if self.product_id in self.products_db and self.old_stock is not None:
            product = self.products_db[self.product_id]
            product.stock_count = self.old_stock
            print(f"Undo: Stock for '{product.name}' restored to {self.old_stock}.")
