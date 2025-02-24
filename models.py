# models.py

class Product:
    def __init__(self, id, name, producer, country, type_, strength, serving_size, price, stock_count):
        self.id = id
        self.name = name
        self.producer = producer
        self.country = country
        self.type_ = type_
        self.strength = strength
        self.serving_size = serving_size
        self.price = price
        self.stock_count = stock_count
        self.available = True  # Determines if the product is shown on the menu

    def __repr__(self):
        return f"Product({self.name}, Price: {self.price}, Stock: {self.stock_count}, Available: {self.available})"
