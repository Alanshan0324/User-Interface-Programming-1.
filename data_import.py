# data_import.py

import json
from models import Product


def load_json_file(file_path):
    """Load JSON data from the given file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def import_beers_bought(file_path):
    """
    Import beer purchase transactions.
    Each entry is converted to the appropriate types.
    """
    data = load_json_file(file_path)
    for entry in data:
        entry['transaction_id'] = int(entry['transaction_id'])
        entry['admin_id'] = int(entry['admin_id'])
        # beer_id is kept as a string (or convert as needed)
        entry['amount'] = int(entry['amount'])
        entry['price'] = float(entry['price'])
    return data


def import_beers_sold(file_path):
    """
    Import beer sold transactions.
    """
    data = load_json_file(file_path)
    for entry in data:
        entry['transaction_id'] = int(entry['transaction_id'])
        entry['user_id'] = int(entry['user_id'])
    return data


def import_payments(file_path):
    """
    Import payment transactions.
    """
    data = load_json_file(file_path)
    for entry in data:
        entry['transaction_id'] = int(entry['transaction_id'])
        entry['user_id'] = int(entry['user_id'])
        entry['admin_id'] = int(entry['admin_id'])
        entry['amount'] = float(entry['amount'])
    return data


def convert_sbl_beer_to_product(beer_dict):
    """
    Convert a dictionary from the dutchman_sbl_beer JSON file into a Product instance.

    Mapping:
      - id: "nr"
      - name: "namn"
      - producer: "producent"
      - country: "ursprunglandnamn"
      - type: "varugrupp"
      - strength: "alkoholhalt"
      - serving_size: "forpackning"
      - price: "prisinklmoms"
      - stock_count: defaulted (since not provided)
    """
    try:
        product_id = int(beer_dict.get("nr", 0))
    except ValueError:
        product_id = 0
    name = beer_dict.get("namn", "Unknown")
    producer = beer_dict.get("producent", "Unknown")
    country = beer_dict.get("ursprunglandnamn", "Unknown")
    type_ = beer_dict.get("varugrupp", "Unknown")
    strength = beer_dict.get("alkoholhalt", "Unknown")
    serving_size = beer_dict.get("forpackning", "Unknown")

    price_str = beer_dict.get("prisinklmoms", "0").replace(",", ".")
    try:
        price = float(price_str)
    except ValueError:
        price = 0.0
    # Set a default stock count since the file does not include one
    stock_count = 100
    return Product(product_id, name, producer, country, type_, strength, serving_size, price, stock_count)


def import_beers(file_path):
    """
    Import product (beer) data from the dutchman_sbl_beer JSON file.
    Converts each beer into a Product instance.
    Returns a dictionary of Product objects keyed by product id.
    """
    data = load_json_file(file_path)
    products = {}
    for beer in data:
        product = convert_sbl_beer_to_product(beer)
        products[product.id] = product
    return products


def import_products(file_path):
    """
    Imports products from a JSON file and returns a list of Product objects.

    Args:
        file_path (str): The path to the JSON file containing product data.

    Returns:
        list: A list of Product objects.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    products = []
    for item in data:
        product = Product(
            id=item.get("id"),
            name=item.get("name"),
            producer=item.get("producer"),
            country=item.get("country"),
            type_=item.get("type_"),
            strength=item.get("strength"),
            serving_size=item.get("serving_size"),
            price=item.get("price"),
            stock_count=item.get("stock_count")
        )
        products.append(product)
    return products


def import_users(file_path):
    """
    Import user data.
    """
    data = load_json_file(file_path)
    for entry in data:
        entry['user_id'] = int(entry['user_id'])
        entry['credentials'] = int(entry['credentials'])
    return data


# Example usage:
if __name__ == "__main__":
    # Adjust the file paths as needed to match your project structure
    beers_bought = import_beers_bought('DBFilesJSON/dutchman_table_beers_bought.json')
    beers_sold = import_beers_sold('DBFilesJSON/dutchman_table_beers_sold.json')
    payments = import_payments('DBFilesJSON/dutchman_table_payments.json')
    beers = import_beers('DBFilesJSON/dutchman_table_sbl_beer.json')
    products = import_products('DBFilesJSON/products.json')
    users = import_users('DBFilesJSON/dutchman_table_users.json')

    print(products)
