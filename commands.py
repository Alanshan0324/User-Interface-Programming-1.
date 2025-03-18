# commands.py

class Command:
    def execute(self):
        raise NotImplementedError("Must implement execute()")

    def undo(self):
        raise NotImplementedError("Must implement undo()")


# Command to modify a product's price.
class ModifyPriceCommand(Command):
    def __init__(self, products_db, product, new_price):
        """
        Args:
            products_db (list): The list of Product objects.
            product (Product): The product object to modify.
            new_price (float): The new price to set.
        """
        self.products_db = products_db
        self.product = product
        self.new_price = new_price
        self.old_price = None

    def execute(self):
        self.old_price = self.product.price
        self.product.price = self.new_price
        print(f"Price of '{self.product.name}' changed from {self.old_price} to {self.new_price}.")

    def undo(self):
        self.product.price = self.old_price
        print(f"Undo: Price of '{self.product.name}' restored to {self.old_price}.")


# Command to remove a product from the menu.
class RemoveProductCommand(Command):
    def __init__(self, products_db, product):
        """
        Args:
            products_db (list): The list of Product objects.
            product (Product): The product object to remove.
        """
        self.products_db = products_db
        self.product = product
        self.previous_state = None  # Save the previous availability status

    def execute(self):
        self.previous_state = self.product.available
        self.product.available = False
        print(f"Product '{self.product.name}' removed from menu.")

    def undo(self):
        self.product.available = self.previous_state
        print(f"Undo: Product '{self.product.name}' restored to menu.")


# Command to offer a discount on a product.
class OfferDiscountCommand(Command):
    def __init__(self, products_db, product, discount_percentage):
        """
        Args:
            products_db (list): The list of Product objects.
            product (Product): The product object to discount.
            discount_percentage (float): The discount percentage to apply.
        """
        self.products_db = products_db
        self.product = product
        self.discount_percentage = discount_percentage
        self.old_price = None

    def execute(self):
        self.old_price = self.product.price
        discounted_price = round(self.product.price * (1 - self.discount_percentage / 100), 2)
        self.product.price = discounted_price
        print(f"Offering discount for '{self.product.name}': Original Price {self.old_price}, Discounted Price {discounted_price}.")

    def undo(self):
        self.product.price = self.old_price
        print(f"Undo: Discount removed. Price of '{self.product.name}' restored to {self.old_price}.")


# Command to update the stock count of a product.
class UpdateStockCommand(Command):
    def __init__(self, products_db, product, new_stock):
        """
        Args:
            products_db (list): The list of Product objects.
            product (Product): The product object to update.
            new_stock (int): The new stock count.
        """
        self.products_db = products_db
        self.product = product
        self.new_stock = new_stock
        self.old_stock = None

    def execute(self):
        self.old_stock = self.product.stock_count
        self.product.stock_count = self.new_stock
        print(f"Stock for '{self.product.name}' updated from {self.old_stock} to {self.new_stock}.")

    def undo(self):
        self.product.stock_count = self.old_stock
        print(f"Undo: Stock for '{self.product.name}' restored to {self.old_stock}.")

class RefillLowStockCommand(Command):
    def __init__(self, products_db, refill_amount=20, threshold=5):
        """
        Args:
            products_db (list): The list of Product objects.
            refill_amount (int): The new stock count to set.
            threshold (int): The threshold below which a product is considered low-stock.
        """
        self.products_db = products_db
        self.refill_amount = refill_amount
        self.threshold = threshold
        # List to keep track of affected products and their old stock values.
        self.affected_products = []  # Each element is a tuple (product, old_stock)

    def execute(self):
        for product in self.products_db:
            # Convert to int if necessary.
            if int(product.stock_count) < self.threshold:
                # Save the product and its current stock.
                self.affected_products.append((product, product.stock_count))
                # Refill to the new stock amount.
                product.stock_count = self.refill_amount
        print(f"Refilled {len(self.affected_products)} low-stock products.")

    def undo(self):
        for product, old_stock in self.affected_products:
            product.stock_count = old_stock
        print(f"Undo: Restored stock for {len(self.affected_products)} products.")
