import os

# Fake users and products data
users = [
    {'username': 'bartender', 'password': 'password123', 'role': 'Bartender'},
    {'username': 'waiter', 'password': 'password123', 'role': 'Waiter'},
    {'username': 'waitress', 'password': 'password123', 'role': 'Waitress'}
]

products = [
    {'name': 'Beer', 'availability': 10},
    {'name': 'Whiskey', 'availability': 5},
    {'name': 'Vodka', 'availability': 0},
    {'name': 'Coke', 'availability': 20}
]

# Language dictionary
translations = {
    'en': {
        'login': 'Login',
        'logout': 'Logout',
        'welcome': 'Welcome, {user}!',
        'product_availability': 'Product Availability',
        'running_low': 'Running low!',
        'remove': 'Remove',
        'select_product': 'Select a product to remove (enter number):',
        'invalid_choice': 'Invalid choice, please try again.',
        'exit': 'Exit'
    },
    'zh': {
        'login': '登录',
        'logout': '登出',
        'welcome': '欢迎, {user}!',
        'product_availability': '产品可用性',
        'running_low': '库存不足！',
        'remove': '移除',
        'select_product': '选择要移除的产品（输入数字）：',
        'invalid_choice': '无效选择，请重试。',
        'exit': '退出'
    },
    'sv': {
        'login': 'Logga in',
        'logout': 'Logga ut',
        'welcome': 'Välkommen, {user}!',
        'product_availability': 'Produkt Tillgänglighet',
        'running_low': 'Låg lager!',
        'remove': 'Ta bort',
        'select_product': 'Välj en produkt att ta bort (ange nummer):',
        'invalid_choice': 'Ogiltigt val, försök igen.',
        'exit': 'Avsluta'
    }
}

# Global variables to track the current user and language
current_user = None
current_language = 'en'

# Function to switch language
def change_language():
    global current_language
    print("\nSelect language: ")
    print("1. English")
    print("2. Chinese")
    print("3. Swedish")
    choice = input(f"Enter the number for your language choice: ")

    if choice == '1':
        current_language = 'en'
    elif choice == '2':
        current_language = 'zh'
    elif choice == '3':
        current_language = 'sv'
    else:
        print(translations[current_language]['invalid_choice'])
        change_language()

# Function to display the product list and handle removals
def display_products():
    print("\n" + translations[current_language]['product_availability'] + ":")
    for idx, product in enumerate(products):
        status = f"{product['name']} - {product['availability']} available"
        if product['availability'] == 0:
            status += f" ({translations[current_language]['running_low']})"
        print(f"{idx + 1}. {status}")
    
    if current_user and current_user['role'] == 'Bartender':
        try:
            choice = int(input(translations[current_language]['select_product']))
            if 1 <= choice <= len(products):
                products[choice - 1]['availability'] = 0
                print(f"Product {products[choice - 1]['name']} has been temporarily removed.")
            else:
                print(translations[current_language]['invalid_choice'])
        except ValueError:
            print(translations[current_language]['invalid_choice'])

# Login function
def login():
    global current_user
    username = input("Username: ")
    password = input("Password: ")

    user = next((u for u in users if u['username'] == username and u['password'] == password), None)
    if user:
        current_user = user
        print(translations[current_language]['welcome'].format(user=current_user['username']))
        return True
    else:
        print("Invalid login credentials.")
        return False

# Logout function
def logout():
    global current_user
    current_user = None
    print("You have logged out.")

# Main loop
def main():
    global current_user
    while True:
        if not current_user:
            print("\n--- Welcome to the Bar System ---")
            if login():
                while current_user:
                    print("\n1. View Products")
                    print("2. Change Language")
                    print("3. Logout")
                    print("4. Exit")
                    choice = input("Select an option: ")

                    if choice == '1':
                        display_products()
                    elif choice == '2':
                        change_language()
                    elif choice == '3':
                        logout()
                    elif choice == '4':
                        print("Goodbye!")
                        return
                    else:
                        print(translations[current_language]['invalid_choice'])
        else:
            print("\nYou are already logged in. Please logout to change user.")
            return

if __name__ == "__main__":
    main()

