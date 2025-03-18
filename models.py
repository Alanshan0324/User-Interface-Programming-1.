from datetime import datetime

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
        self.stock_count = int(stock_count)
        self.available = True

    def __repr__(self):
        return (f"Product(id={self.id}, name='{self.name}', producer='{self.producer}', "
                f"country='{self.country}', type_='{self.type_}', strength='{self.strength}', "
                f"serving_size='{self.serving_size}', price='{self.price}', stock_count={self.stock_count}, "
                f"available={self.available})")