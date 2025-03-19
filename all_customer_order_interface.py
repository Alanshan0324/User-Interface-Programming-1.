# all_customer_order_interface.py
from data_import import import_products
from controller import *
import subprocess, sys


class MenuItem:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

class Order:
    def __init__(self, table_number=None):
        self.items = []
        self.total = 0 
        self.table_number = table_number
        self.sub_orders = []

    def add_item(self, item, quantity=1, sub_order_index=None):
        is_group = len(self.sub_orders) > 0 or sub_order_index is not None
        
        if is_group:
            while len(self.sub_orders) <= (sub_order_index or 0):
                self.sub_orders.append([])
            
            self.sub_orders[sub_order_index].append((item, quantity))
        else:
            self.items.append((item, quantity))
        
        self.total += item.price * quantity
    
    def remove_item(self, item_id, quantity=1, sub_order_index=None):
        is_group = len(self.sub_orders) > 0
        
        if is_group and sub_order_index is not None:
            # Check if the suborder index is valid
            if sub_order_index >= len(self.sub_orders):
                return False
                
            # Find the item in the sub-order
            for i, (item, item_qty) in enumerate(self.sub_orders[sub_order_index]):
                if item.id == item_id:
                    # If the quantity to be removed is less than the number of items, then decrease the quantity
                    if quantity < item_qty:
                        self.sub_orders[sub_order_index][i] = (item, item_qty - quantity)
                        self.total -= item.price * quantity
                    # Otherwise delete the entire item
                    else:
                        actual_qty = item_qty  # The actual number of deletions does not exceed the existing number
                        self.sub_orders[sub_order_index].pop(i)
                        self.total -= item.price * actual_qty
                    return True
        else:
            # Look for this item in the regular order
            for i, (item, item_qty) in enumerate(self.items):
                if item.id == item_id:
                    # If the quantity to be removed is less than the number of items, then decrease the quantity
                    if quantity < item_qty:
                        self.items[i] = (item, item_qty - quantity)
                        self.total -= item.price * quantity
                    # Otherwise delete the entire item
                    else:
                        actual_qty = item_qty  # The actual number of deletions does not exceed the existing number
                        self.items.pop(i)
                        self.total -= item.price * actual_qty
                    return True
        
        return False  # item not found

    def is_group_order(self):
        return len(self.sub_orders) > 0

    def clear(self):
        self.items = []
        self.total = 0
        self.sub_orders = []

    def get_split_bills(self):
        if not self.is_group_order():
            return [(self.items, self.total)]

        result = []
        for sub_order in self.sub_orders:
            sub_total = sum(item.price * qty for item, qty in sub_order)
            result.append((sub_order, sub_total))
        return result

    def get_all_items(self):
        if self.is_group_order():
            all_items = []
            for sub_order in self.sub_orders:
                all_items.extend(sub_order)
            return all_items
        return self.items


class LanguageModel:
    def __init__(self):
        self.languages = ["English", "繁體中文", "Svenska"]
        self.current_language = "English"
        
        self.translations = {
            "English": {
                "language_selection": "Language Selection",
                "alcoholic_drinks": "Alcoholic Drinks",
                "classic_cocktails": "Classic Cocktails",
                "non_alcoholic_specials": "Non-Alcoholic Specials",
                "bar_snacks": "Bar Snacks",
                "main_dishes": "Main Dishes",
                "desserts": "Desserts",
                "table_number": "Table Number",
                "add": "Add",
                "remove": "Remove",
                "clear": "Clear",
                "group_order": "Group Order",
                "regular_order": "Regular Order",
                "order_summary": "Order Summary",
                "split_bill": "Split Bill",
                "total": "Total",
                "order": "Order",
                "logout": "Log Out",
                "quantity": "Quantity",
                "person": "Person",
                "persons": "Persons",
                "bill": "Bill"
            },
            "繁體中文": {
                "language_selection": "語言選擇",
                "alcoholic_drinks": "酒精飲料",
                "classic_cocktails": "經典雞尾酒",
                "non_alcoholic_specials": "無酒精特調",
                "bar_snacks": "酒吧小吃",
                "main_dishes": "主餐",
                "desserts": "甜點",
                "table_number": "桌號",
                "add": "添加",
                "remove": "移除",
                "clear": "清空",
                "group_order": "團體訂單",
                "regular_order": "一般訂單",
                "order_summary": "訂單摘要",
                "split_bill": "分單結帳",
                "total": "總計",
                "order": "訂單",
                "quantity": "數量",
                "person": "顧客",
                "persons": "人數",
                "bill": "帳單",
                "menu": "菜單",
                "name": "名稱",
                "price": "價格",
                "total_order": "總訂單",
                "delete_item": "刪除項目",
                "decrease_quantity": "減少數量",
                "drop_items_here": "將項目拖放至此",
                "drag_hint": "拖曳菜單項目至此添加至訂單",
                "information": "資訊",
                "no_items": "無項目",
                "subtotal": "小計",
                "print_bills": "列印帳單",
                "printing_bills": "正在列印帳單...",
                "close": "關閉",
                "checkout": "結帳",
                "logout": "登出",
                "all": "全部",
                "choose_person": "選擇顧客"
            },
            "Svenska": {
                "language_selection": "Språkval",
                "alcoholic_drinks": "Alkoholhaltiga Drycker",
                "classic_cocktails": "Klassiska Cocktails",
                "non_alcoholic_specials": "Alkoholfria Specialiteter",
                "bar_snacks": "Barsnacks",
                "main_dishes": "Huvudrätter",
                "desserts": "Efterrätter",
                "table_number": "Bordsnummer",
                "add": "Lägg till",
                "remove": "Ta bort",
                "clear": "Rensa",
                "group_order": "Gruppbeställning",
                "regular_order": "Vanlig Beställning",
                "order_summary": "Beställningsöversikt",
                "split_bill": "Dela Nota",
                "total": "Totalt",
                "order": "Beställning",
                "quantity": "Antal",
                "person": "Person",
                "persons": "Personer",
                "bill": "Nota",
                "menu": "Meny",
                "name": "Namn",
                "price": "Pris",
                "total_order": "Total Beställning",
                "delete_item": "Ta Bort Artikel",
                "decrease_quantity": "Minska Antal",
                "drop_items_here": "Släpp Artiklar Här",
                "drag_hint": "Dra menyartiklar hit för att lägga till i beställningen",
                "information": "Information",
                "no_items": "Inga Artiklar",
                "subtotal": "Delsumma",
                "print_bills": "Skriv Ut Notor",
                "printing_bills": "Skriver ut notor...",
                "close": "Stäng",
                "checkout": "Betala",
                "logout": "Logga ut",
                "all": "Alla",
                "choose_person": "Välj Person"
            }
        }
    
    def get_languages(self):
        return self.languages
    
    def set_language(self, language):
        if language in self.languages:
            self.current_language = language
            return True
        return False
    
    def get_current_language(self):
        return self.current_language
    
    def get_text(self, key):
        return self.translations.get(self.current_language, {}).get(key, key)


class MenuModel:
    def __init__(self):
        self.category_translations = {
            "Alcoholic Drinks": {
                "English": "Alcoholic Drinks",
                "繁體中文": "酒精飲料",
                "Svenska": "Alkoholhaltiga Drycker"
            },
            "Classic Cocktails": {
                "English": "Classic Cocktails",
                "繁體中文": "經典雞尾酒",
                "Svenska": "Klassiska Cocktails"
            },
            "Non-Alcoholic Specials": {
                "English": "Non-Alcoholic Specials",
                "繁體中文": "無酒精特調",
                "Svenska": "Alkoholfria Specialiteter"
            },
            "Bar Snacks": {
                "English": "Bar Snacks",
                "繁體中文": "酒吧小吃",
                "Svenska": "Barsnacks"
            },
            "Main Dishes": {
                "English": "Main Dishes",
                "繁體中文": "主餐",
                "Svenska": "Huvudrätter"
            },
            "Desserts": {
                "English": "Desserts",
                "繁體中文": "甜點",
                "Svenska": "Efterrätter"
            }
        }

        # Sample menu data
        self.menu_items = [
            # Alcoholic Drinks
            MenuItem(1, "Draft Beer", 6.00, "Alcoholic Drinks"),
            MenuItem(2, "Stout Beer", 7.00, "Alcoholic Drinks"),
            MenuItem(3, "Lager Beer", 6.00, "Alcoholic Drinks"),
            MenuItem(4, "Pale Ale", 7.00, "Alcoholic Drinks"),
            MenuItem(5, "Cider", 6.00, "Alcoholic Drinks"),
            MenuItem(6, "Vodka", 8.00, "Alcoholic Drinks"),
            MenuItem(7, "Whiskey", 10.00, "Alcoholic Drinks"),
            MenuItem(8, "Gin", 8.00, "Alcoholic Drinks"),
            MenuItem(9, "Rum", 8.00, "Alcoholic Drinks"),
            MenuItem(10, "Brandy", 10.00, "Alcoholic Drinks"),
            MenuItem(11, "Plum Wine", 9.00, "Alcoholic Drinks"),
            MenuItem(12, "Red Wine", 9.00, "Alcoholic Drinks"),
            MenuItem(13, "White Wine", 9.00, "Alcoholic Drinks"),
            MenuItem(14, "Champagne", 12.00, "Alcoholic Drinks"),
            MenuItem(15, "Sake", 10.00, "Alcoholic Drinks"),
            
            # Classic Cocktails
            MenuItem(16, "Martini", 12.00, "Classic Cocktails"),
            MenuItem(17, "Mojito", 10.00, "Classic Cocktails"),
            MenuItem(18, "Margarita", 11.00, "Classic Cocktails"),
            MenuItem(19, "Long Island Iced Tea", 13.00, "Classic Cocktails"),
            MenuItem(20, "Tequila Sunrise", 10.00, "Classic Cocktails"),
            MenuItem(21, "Old Fashioned", 12.00, "Classic Cocktails"),
            MenuItem(22, "Negroni", 11.00, "Classic Cocktails"),
            MenuItem(23, "Whiskey Sour", 10.00, "Classic Cocktails"),
            MenuItem(24, "Daiquiri", 9.50, "Classic Cocktails"),
            MenuItem(25, "Manhattan", 12.50, "Classic Cocktails"),
            MenuItem(26, "French 75", 11.00, "Classic Cocktails"),
            MenuItem(27, "Pina Colada", 10.50, "Classic Cocktails"),
            MenuItem(28, "Cosmopolitan", 10.00, "Classic Cocktails"),
            MenuItem(29, "Sidecar", 11.50, "Classic Cocktails"),
            MenuItem(30, "Mai Tai", 12.00, "Classic Cocktails"),
            
            # Non-Alcoholic Specials
            MenuItem(31, "Hot Chocolate", 6.00, "Non-Alcoholic Specials"),
            MenuItem(32, "Rose Lemon Soda", 7.00, "Non-Alcoholic Specials"),
            MenuItem(33, "Honey Yuzu Tea", 7.00, "Non-Alcoholic Specials"),
            MenuItem(34, "Fresh Smoothie", 8.00, "Non-Alcoholic Specials"),
            MenuItem(35, "Matcha Latte", 7.00, "Non-Alcoholic Specials"),
            MenuItem(36, "Iced Americano", 6.50, "Non-Alcoholic Specials"),
            MenuItem(37, "Strawberry Milkshake", 7.50, "Non-Alcoholic Specials"),
            MenuItem(38, "Mango Lassi", 8.00, "Non-Alcoholic Specials"),
            MenuItem(39, "Coconut Water", 5.50, "Non-Alcoholic Specials"),
            MenuItem(40, "Green Apple Soda", 6.50, "Non-Alcoholic Specials"),
            
            # Bar Snacks
            MenuItem(41, "Classic Fries", 5.00, "Bar Snacks"),
            MenuItem(42, "Onion Rings", 6.00, "Bar Snacks"),
            MenuItem(43, "Cheese Sticks", 7.00, "Bar Snacks"),
            MenuItem(44, "Spicy Chicken Wings", 8.00, "Bar Snacks"),
            MenuItem(45, "Fish & Chips", 10.00, "Bar Snacks"),
            MenuItem(46, "Garlic Bread", 5.50, "Bar Snacks"),
            MenuItem(47, "Popcorn Shrimp", 9.00, "Bar Snacks"),
            MenuItem(48, "Jalapeno Poppers", 7.50, "Bar Snacks"),
            MenuItem(49, "BBQ Pork Skewers", 8.50, "Bar Snacks"),
            MenuItem(50, "Salted Peanuts", 4.00, "Bar Snacks"),
            
            # Main Dishes
            MenuItem(51, "Grilled Steak", 20.00, "Main Dishes"),
            MenuItem(52, "Beef Burrito", 15.00, "Main Dishes"),
            MenuItem(53, "Seafood Pasta", 16.00, "Main Dishes"),
            MenuItem(54, "Teriyaki Chicken Rice", 14.00, "Main Dishes"),
            MenuItem(55, "Classic Burger", 12.00, "Main Dishes"),
            MenuItem(56, "BBQ Ribs", 18.00, "Main Dishes"),
            MenuItem(57, "Vegetarian Pizza", 14.50, "Main Dishes"),
            MenuItem(58, "Lamb Chops", 22.00, "Main Dishes"),
            MenuItem(59, "Chicken Alfredo", 15.50, "Main Dishes"),
            MenuItem(60, "Pork Schnitzel", 13.50, "Main Dishes"),
            
            # Desserts
            MenuItem(61, "Classic Tiramisu", 8.00, "Desserts"),
            MenuItem(62, "Molten Chocolate Cake", 9.00, "Desserts"),
            MenuItem(63, "New York Cheesecake", 8.00, "Desserts"),
            MenuItem(64, "Vanilla Panna Cotta", 7.00, "Desserts"),
            MenuItem(65, "Matcha Red Bean Pancakes", 9.00, "Desserts"),
            MenuItem(66, "Lemon Tart", 7.50, "Desserts"),
            MenuItem(67, "Strawberry Shortcake", 8.50, "Desserts"),
            MenuItem(68, "Carrot Cake", 7.50, "Desserts"),
            MenuItem(69, "Banoffee Pie", 9.00, "Desserts"),
            MenuItem(70, "Chocolate Brownie", 8.00, "Desserts")
        ]

    def get_menu_items(self):
        return self.menu_items

    def get_item_by_id(self, item_id):
        return next((item for item in self.menu_items if item.id == item_id), None)
    
    def get_translated_category(self, category, language):
        return self.category_translations.get(category, {}).get(language, category)

# view
import tkinter as tk
from tkinter import ttk, messagebox

class POSView:
    def __init__(self, root, language_model):
        self.root = root
        self.root.title("Bar POS System")
        self.root.geometry("1430x600")
        self.root.minsize(600, 400)  # Set minimum window size
        
        self.language_model = language_model
        
        # Define breakpoints for responsive design
        self.breakpoints = {
            "mobile": 800,    # Mobile layout below 800px width
            "tablet": 1200    # Tablet layout between 800px and 1200px width
        }
        
        # Track current layout
        self.current_layout = "desktop"  # Default layout
        
        # Set column weights to control the proportions of the left and right sides
        root.columnconfigure(0, weight=4)  # Menu 4/5
        root.columnconfigure(1, weight=1)  # Order 1/5
        root.rowconfigure(0, weight=1)
        
        # Add language selection framework
        self.language_frame = ttk.Frame(root)
        self.language_frame.grid(row=0, column=0, sticky="nw", padx=5, pady=5)
        
        ttk.Label(self.language_frame, text=self.get_text("language_selection"), 
                 font=('Arial', 10)).pack(side=tk.LEFT, padx=(0, 5))
        
        # Create a language selection drop-down box
        self.language_var = tk.StringVar(value=self.language_model.get_current_language())
        self.language_combobox = ttk.Combobox(self.language_frame, 
                                             textvariable=self.language_var,
                                             values=self.language_model.get_languages(),
                                             state="readonly",
                                             width=15)
        self.language_combobox.pack(side=tk.LEFT)
        self.language_combobox.bind("<<ComboboxSelected>>", self.on_language_change)
        
        # Create the main frame using grid instead of pack
        self.menu_frame = ttk.Frame(root)
        self.menu_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=(40, 5))  # Adjust top spacing
        
        self.order_frame = ttk.Frame(root)
        self.order_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        # menu
        self.menu_label = ttk.Label(self.menu_frame, text="Menu", font=('Arial', 16, 'bold'))
        self.menu_label.pack()
        
        # Create menu category framework (better visual organization)
        self.categories_frame = ttk.Frame(self.menu_frame)
        self.categories_frame.pack(fill=tk.X, pady=5)
        
        # Category button frame displayed in two rows
        self.categories_row1 = ttk.Frame(self.categories_frame)
        self.categories_row1.pack(fill=tk.X)
        
        self.categories_row2 = ttk.Frame(self.categories_frame)
        self.categories_row2.pack(fill=tk.X, pady=(5, 0))
        
        # Category Button
        self.category_buttons = {}
        self.selected_category = tk.StringVar(value="All")
        
        # Menu item frame and scroll bar
        self.menu_items_frame = ttk.Frame(self.menu_frame)
        self.menu_items_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Canvas for scrolling
        self.menu_canvas = tk.Canvas(self.menu_items_frame)
        self.menu_scrollbar = ttk.Scrollbar(self.menu_items_frame, orient="vertical", command=self.menu_canvas.yview)
        self.menu_scrollable_frame = ttk.Frame(self.menu_canvas)
        
        self.menu_scrollable_frame.bind(
            "<Configure>",
            lambda e: self.menu_canvas.configure(scrollregion=self.menu_canvas.bbox("all"))
        )
        
        self.menu_canvas.create_window((0, 0), window=self.menu_scrollable_frame, anchor="nw")
        self.menu_canvas.configure(yscrollcommand=self.menu_scrollbar.set)
        
        self.menu_canvas.pack(side="left", fill="both", expand=True)
        self.menu_scrollbar.pack(side="right", fill="y")
        
        # Order section and notebook
        self.order_title_label = ttk.Label(self.order_frame, text=self.get_text("order"), font=('Arial', 16, 'bold'))
        self.order_title_label.pack()
        
        # Order Controls
        order_config_frame = ttk.Frame(self.order_frame)
        order_config_frame.pack(fill=tk.X, pady=5)
        
        self.table_number_label = ttk.Label(order_config_frame, text=f"{self.get_text('table_number')}:")
        self.table_number_label.pack(side=tk.LEFT, padx=5)
        self.table_number = ttk.Entry(order_config_frame, width=5)
        self.table_number.pack(side=tk.LEFT, padx=5)
        
        # Group size control
        self.group_control_frame = ttk.Frame(order_config_frame)
        self.group_control_frame.pack(side=tk.LEFT, padx=10)
        
        self.persons_label = ttk.Label(self.group_control_frame, text=f"{self.get_text('persons')}:")
        self.persons_label.pack(side=tk.LEFT, padx=5)
        self.people_count = tk.IntVar(value=1)
        self.people_count_label = ttk.Label(self.group_control_frame, textvariable=self.people_count)
        self.people_count_label.pack(side=tk.LEFT, padx=5)
        
        self.add_person_btn = ttk.Button(self.group_control_frame, text="+", width=2)
        self.add_person_btn.pack(side=tk.LEFT, padx=2)
        
        self.remove_person_btn = ttk.Button(self.group_control_frame, text="-", width=2)
        self.remove_person_btn.pack(side=tk.LEFT, padx=2)

        # Add a new personnel number
        self.current_person = tk.IntVar(value=1)
        self.choose_person_label = ttk.Label(self.group_control_frame, text=f"{self.get_text('choose_person')}:")
        self.choose_person_label.pack(side=tk.LEFT, padx=5)
        self.person_spinbox = ttk.Spinbox(
            self.group_control_frame, 
            from_=1, 
            to=1, 
            width=5,
            textvariable=self.current_person
        )
        self.person_spinbox.pack(side=tk.LEFT, padx=5)
        
        # Create a notebook
        self.order_notebook = ttk.Notebook(self.order_frame)
        self.order_notebook.pack(fill=tk.BOTH, expand=True)
        
        # Total Order Tab
        self.total_order_frame = ttk.Frame(self.order_notebook)
        self.order_notebook.add(self.total_order_frame, text=self.get_text("total"))
        
        # Creating the Drop Zone Frame
        self.drop_frame = ttk.LabelFrame(self.total_order_frame, text=self.get_text("drop_items_here"))
        self.drop_frame.pack(fill=tk.X, padx=5, pady=5, ipady=10)
        
        # Label for the drop zone
        self.drop_label = ttk.Label(self.drop_frame, 
                                  text=self.get_text("drag_hint"), 
                                  font=('Arial', 10), foreground='gray')
        self.drop_label.pack(pady=20)
        
        # Create a tree view of total orders
        self.order_tree = ttk.Treeview(self.total_order_frame, columns=('Name', 'Quantity', 'Price'), show='headings')
        self.order_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.order_tree.heading('Name', text=self.get_text("name"))
        self.order_tree.heading('Quantity', text=self.get_text("quantity"))
        self.order_tree.heading('Price', text=self.get_text("price"))
        
        # Personal Order Frame (will be populated dynamically)
        self.individual_trees = {}  # Stores each person's tree view
        
        # Total Label
        self.total_label = ttk.Label(self.order_frame, text=f"{self.get_text('total')}: $0.00", font=('Arial', 14))
        self.total_label.pack(pady=10)
        
        # Buttons
        self.button_frame = ttk.Frame(self.order_frame)
        self.button_frame.pack(fill=tk.X, pady=5)
        
        self.clear_button = ttk.Button(self.button_frame, text=self.get_text("clear"))
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        self.checkout_button = ttk.Button(self.button_frame, text=self.get_text("checkout"))
        self.checkout_button.pack(side=tk.LEFT, padx=5)

        self.split_bill_button = ttk.Button(self.button_frame, text=self.get_text("split_bill"))
        self.split_bill_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = ttk.Button(self.button_frame, text=self.get_text("delete_item"))
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.logout_button = ttk.Button(self.button_frame, text=self.get_text("logout"))
        self.logout_button.pack(side=tk.RIGHT, padx=5)
        
        # Dictionary used to store menu item widgets
        self.menu_item_widgets = {}

        # Bind window resize event
        self.root.bind("<Configure>", self.on_window_resize)

        self.order_tree.bind("<<TreeviewSelect>>", self.on_order_item_selected)
    
    def get_text(self, key):
        return self.language_model.get_text(key)
    
    def on_language_change(self, event):
        selected_language = self.language_var.get()
        if self.language_model.set_language(selected_language):
            self.update_interface_text()
            
            # Notify the controller that the language has changed
            if hasattr(self, 'on_language_change_callback'):
                self.on_language_change_callback()
    
    def set_on_language_change_callback(self, callback):
        self.on_language_change_callback = callback
    
    def update_interface_text(self):
        # Update top menu
        self.menu_label.config(text=self.get_text("menu"))
        
        # Update Order Section
        self.order_title_label.config(text=self.get_text("order"))
        self.table_number_label.config(text=f"{self.get_text('table_number')}:")
        self.persons_label.config(text=f"{self.get_text('persons')}:")
        self.choose_person_label.config(text=f"{self.get_text('choose_person')}:")
        
        # Update Drop Zone
        self.drop_frame.config(text=self.get_text("drop_items_here"))
        self.drop_label.config(text=self.get_text("drag_hint"))
        
        # Update order tree view
        self.order_tree.heading('Name', text=self.get_text("name"))
        self.order_tree.heading('Quantity', text=self.get_text("quantity"))
        self.order_tree.heading('Price', text=self.get_text("price"))
        
        # Update Order Tab
        self.order_notebook.tab(0, text=self.get_text("total_order"))
        
        # Update personal order tab
        for i, (person_name, person_data) in enumerate(self.individual_trees.items()):
            translated_name = f"{self.get_text('person')} {i+1}"
            self.order_notebook.tab(person_data['frame'], text=translated_name)
            if 'drop_frame' in person_data:
                person_data['drop_frame'].config(text=f"{self.get_text('drop_items_here')} - {translated_name}")
            
            # Update personal tree view
            person_data['tree'].heading('Name', text=self.get_text("name"))
            person_data['tree'].heading('Quantity', text=self.get_text("quantity"))
            person_data['tree'].heading('Price', text=self.get_text("price"))
        
        # Update Button
        self.clear_button.config(text=self.get_text("clear"))
        self.checkout_button.config(text=self.get_text("checkout"))
        self.split_bill_button.config(text=self.get_text("split_bill"))
        self.delete_button.config(text=self.get_text("delete_item"))
        
        # Update total label
        total_value = self.total_label.cget("text").split("$")[1]
        self.total_label.config(text=f"{self.get_text('total')}: ${total_value}")
        
        # Update category buttons (translate category names according to menu model)
        if hasattr(self, 'menu_model') and hasattr(self, 'on_category_change_callback'):
            self.update_category_buttons()
            self.on_category_change_callback()

    def on_order_item_selected(self, event):
        pass

    def set_on_delete_button_callback(self, callback):
        self.delete_button.config(command=callback)

    def on_delete_button_clicked(self):
        current_tab = self.order_notebook.select()
        
        # Check whether the current order is a general order or a personal order
        if current_tab == str(self.total_order_frame):
            # Total Order Page
            selection = self.order_tree.selection()
            if selection:
                item_id = selection[0]
                item_name = self.order_tree.item(item_id, 'values')[0]
                if hasattr(self, 'on_remove_item_callback'):
                    self.on_remove_item_callback(item_name)
        else:
            # Personal order page
            for idx, (tab_name, tab_data) in enumerate(self.individual_trees.items()):
                if current_tab == str(tab_data['frame']):
                    selection = tab_data['tree'].selection()
                    if selection:
                        item_id = selection[0]
                        item_name = tab_data['tree'].item(item_id, 'values')[0]
                        if hasattr(self, 'on_remove_item_callback'):
                            self.on_remove_item_callback(item_name, idx)
                    break  

    def set_menu_model(self, menu_model):
        self.menu_model = menu_model

    def show_order_context_menu(self, event):
        # Get the clicked item
        item_id = self.order_tree.identify_row(event.y)
        if item_id:
            # Select the clicked item
            self.order_tree.selection_set(item_id)
            
            # Create a right-click menu
            context_menu = tk.Menu(self.root, tearoff=0)
            context_menu.add_command(label=self.get_text("delete_item"), 
                                command=lambda: self.on_delete_item(item_id))
            context_menu.add_command(label=self.get_text("decrease_quantity"), 
                                command=lambda: self.on_decrease_quantity(item_id))
            
            # Show Menu
            context_menu.post(event.x_root, event.y_root)

    def on_delete_item(self, item_id):
        if item_id:
            # Get the item name
            item_name = self.order_tree.item(item_id, 'values')[0]
            
            # Notify the controller via callback
            if hasattr(self, 'on_remove_item_callback'):
                # Decide whether to delete the overall order or individual orders from the currently displayed tab
                current_tab = self.order_notebook.select()
                
                if current_tab == str(self.total_order_frame):
                    # Total Order Page
                    self.on_remove_item_callback(item_name)
                else:
                    # Personal order page
                    for idx, (tab_name, tab_data) in enumerate(self.individual_trees.items()):
                        if current_tab == str(tab_data['frame']):
                            self.on_remove_item_callback(item_name, idx)
                            break

    def on_decrease_quantity(self, item_id):
        if item_id:
            # Get the item name and current quantity
            values = self.order_tree.item(item_id, 'values')
            item_name = values[0]
            current_qty = int(values[1])
            
            if current_qty > 1:
                # Notify the controller to reduce the number through callback
                if hasattr(self, 'on_decrease_quantity_callback'):
                    current_tab = self.order_notebook.select()
                    
                    if current_tab == str(self.total_order_frame):
                        self.on_decrease_quantity_callback(item_name)
                    else:
                        for idx, (tab_name, tab_data) in enumerate(self.individual_trees.items()):
                            if current_tab == str(tab_data['frame']):
                                self.on_decrease_quantity_callback(item_name, idx)
                                break
            else:
                # If the quantity is 1, delete it directly
                self.on_delete_item(item_id)

    def on_window_resize(self, event):
        """Handle window resize events to apply responsive layout"""
        # Only process events from the root window, not child widgets
        if event.widget == self.root:
            width = event.width
            
            # Determine the layout based on window width
            if width < self.breakpoints["mobile"] and self.current_layout != "mobile":
                self.apply_mobile_layout()
                self.current_layout = "mobile"
            elif width >= self.breakpoints["mobile"] and width < self.breakpoints["tablet"] and self.current_layout != "tablet":
                self.apply_tablet_layout()
                self.current_layout = "tablet"
            elif width >= self.breakpoints["tablet"] and self.current_layout != "desktop":
                self.apply_desktop_layout()
                self.current_layout = "desktop"
            
            # Rebuild menu with current category
            current_category = self.selected_category.get()
            self.root.after(100, lambda: self.rebuild_menu_after_resize(current_category))

    def apply_mobile_layout(self):
        """Apply mobile layout for small screens"""
        # Reconfigure the grid to stack menu and order sections vertically
        self.root.grid_columnconfigure(0, weight=1)  # Full width
        self.root.grid_columnconfigure(1, weight=1)  # Hidden/collapsed
        
        # Move order frame below menu frame
        self.order_frame.grid_forget()
        self.order_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        
        # Reduce category button size and adjust padding
        for cat_btn in self.category_buttons.values():
            cat_btn.configure(padding=(2, 1))
        
        # Adjust menu items to use fewer columns
        self.max_menu_cols = 3  # 3 columns for mobile
        
        # Adjust font sizes
        self.menu_label.configure(font=('Arial', 14, 'bold'))
        self.order_title_label.configure(font=('Arial', 14, 'bold'))
        self.total_label.configure(font=('Arial', 12))
        
        # Make order controls more compact
        self.table_number.configure(width=3)
        self.person_spinbox.configure(width=3)

        self.order_tree.configure(height=4)
        for person_data in self.individual_trees.values():
            if 'tree' in person_data:
                person_data['tree'].configure(height=4)
    
        self.drop_frame.pack(fill=tk.X, padx=5, pady=3, ipady=5) 
        self.drop_label.pack(pady=10)
        
        # Stack buttons in the button frame vertically
        for button in [self.clear_button, self.checkout_button, self.split_bill_button, self.delete_button]:
            button.pack_forget()
            button.pack(fill=tk.X, padx=2, pady=2)
        
        # Ensure scrollbars remain functional
        self.menu_canvas.configure(height=200)  # Fixed height for menu area

    def apply_tablet_layout(self):
        """Apply tablet layout for medium screens"""
        # Restore horizontal layout but with adjusted proportions
        self.root.grid_columnconfigure(0, weight=2)  # Menu 2/3
        self.root.grid_columnconfigure(1, weight=1)  # Order 1/3
        
        # Move order frame back to side
        self.order_frame.grid_forget()
        self.order_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        # Adjust category buttons
        for cat_btn in self.category_buttons.values():
            cat_btn.configure(padding=(4, 2))
        
        # Adjust menu items to use medium number of columns
        self.max_menu_cols = 2  # 2 columns for tablet
        
        # Restore font sizes
        self.menu_label.configure(font=('Arial', 16, 'bold'))
        self.order_title_label.configure(font=('Arial', 16, 'bold'))
        self.total_label.configure(font=('Arial', 14))
        
        # Restore field sizes
        self.table_number.configure(width=5)
        self.person_spinbox.configure(width=5)
        
        # Restore horizontal button layout
        for button in [self.clear_button, self.checkout_button, self.split_bill_button, self.delete_button]:
            button.pack_forget()
        self.clear_button.pack(side=tk.LEFT, padx=3)
        self.checkout_button.pack(side=tk.LEFT, padx=3)
        self.split_bill_button.pack(side=tk.LEFT, padx=3)
        self.delete_button.pack(side=tk.LEFT, padx=3)
        
        # Adjust canvas to expand properly
        self.menu_canvas.configure(height=0)  # Let it expand naturally

    def apply_desktop_layout(self):
        """Apply desktop layout for large screens"""
        # Original desktop proportions
        self.root.grid_columnconfigure(0, weight=4)  # Menu 4/5
        self.root.grid_columnconfigure(1, weight=1)  # Order 1/5
        
        # Ensure order frame is in the right position
        self.order_frame.grid_forget()
        self.order_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        # Full size for category buttons
        for cat_btn in self.category_buttons.values():
            cat_btn.configure(padding=(5, 3))
        
        # Use maximum number of columns for menu items
        self.max_menu_cols = 3  # 3 columns for desktop
        
        # Standard font sizes
        self.menu_label.configure(font=('Arial', 16, 'bold'))
        self.order_title_label.configure(font=('Arial', 16, 'bold'))
        self.total_label.configure(font=('Arial', 14))
        
        # Standard field sizes
        self.table_number.configure(width=5)
        self.person_spinbox.configure(width=5)
        
        # Standard button layout
        for button in [self.clear_button, self.checkout_button, self.split_bill_button, self.delete_button]:
            button.pack_forget()
        self.clear_button.pack(side=tk.LEFT, padx=5)
        self.checkout_button.pack(side=tk.LEFT, padx=5)
        self.split_bill_button.pack(side=tk.LEFT, padx=5)
        self.delete_button.pack(side=tk.LEFT, padx=5)
        
        # Full expansion for menu area
        self.menu_canvas.configure(height=0)

    def rebuild_menu_after_resize(self, category):
        """Rebuild the menu after window resize with the current category"""
        # Store the current category
        old_category = self.selected_category.get()
        
        # Set the category (this will trigger a rebuild if it's different)
        if category != old_category:
            self.selected_category.set(category)
        else:
            # If the category is the same, we need to manually trigger a rebuild
            if hasattr(self, 'on_category_change_callback'):
                self.on_category_change_callback()
    
    def update_category_buttons(self):
        current_language = self.language_model.get_current_language()
        if hasattr(self, 'menu_model'):
            for category, button in self.category_buttons.items():
                if category == "All":
                    button.config(text=self.get_text("all"))
                else:
                    translated_cat = self.menu_model.get_translated_category(category, current_language)
                    button.config(text=translated_cat)
    
    def create_menu_items(self, items, categories):
        """Create draggable menu item widgets with improved usability and responsive design"""
        # Clear existing widgets
        for widget in self.menu_scrollable_frame.winfo_children():
            widget.destroy()
        
        # Clear existing category buttons if any
        for widget in self.categories_row1.winfo_children():
            widget.destroy()
        for widget in self.categories_row2.winfo_children():
            widget.destroy()
        
        self.category_buttons = {}
        current_language = self.language_model.get_current_language()
        
        # Add "All" category first in row 1
        all_btn = ttk.Radiobutton(self.categories_row1, text=self.get_text("all"), value="All", 
                                variable=self.selected_category)
        all_btn.pack(side=tk.LEFT, padx=5)
        self.category_buttons["All"] = all_btn
        
        # Split categories evenly between two rows
        total_categories = len(categories)
        half_categories = total_categories // 2 + (1 if total_categories % 2 != 0 else 0)
        
        # Add first half of categories to row 1
        for i, category in enumerate(categories[:half_categories]):
            # Use translated category names
            translated_cat = self.menu_model.get_translated_category(category, current_language) if hasattr(self, 'menu_model') else category
            cat_btn = ttk.Radiobutton(self.categories_row1, text=translated_cat, value=category, 
                                    variable=self.selected_category)
            cat_btn.pack(side=tk.LEFT, padx=5)
            self.category_buttons[category] = cat_btn
        
        # Add second half of categories to row 2
        for category in categories[half_categories:]:
            # Use translated category names
            translated_cat = self.menu_model.get_translated_category(category, current_language) if hasattr(self, 'menu_model') else category
            cat_btn = ttk.Radiobutton(self.categories_row2, text=translated_cat, value=category, 
                                    variable=self.selected_category)
            cat_btn.pack(side=tk.LEFT, padx=5)
            self.category_buttons[category] = cat_btn
        
        # Create menu items
        current_category = self.selected_category.get()
        
        # Determine number of columns based on current layout
        max_cols = getattr(self, 'max_menu_cols', 3)  # Default to 3 if not set
        
        row = 0
        col = 0
        
        # Filter items by selected category if not "All"
        display_items = items if current_category == "All" else [item for item in items if item.category == current_category]
        
        # Configure the grid with evenly distributed columns
        for i in range(max_cols):
            self.menu_scrollable_frame.columnconfigure(i, weight=1)
        
        # Adjust item size based on layout
        if self.current_layout == "mobile":
            item_width = 100
            item_height = 60
            font_size_name = 10
            font_size_price = 9
        elif self.current_layout == "tablet":
            item_width = 110
            item_height = 70
            font_size_name = 11
            font_size_price = 10
        else:  # desktop
            item_width = 120
            item_height = 80
            font_size_name = 12
            font_size_price = 10
        
        for item in display_items:
            if col >= max_cols:
                col = 0
                row += 1
                
            # Create a frame for each menu item
            item_frame = ttk.Frame(self.menu_scrollable_frame, relief="raised", borderwidth=2)
            item_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            
            # Set minimum size based on layout
            item_frame.columnconfigure(0, minsize=item_width)
            item_frame.rowconfigure(0, minsize=item_height)
            
            # Create a container inside the frame for better styling
            inner_frame = ttk.Frame(item_frame, padding=3)
            inner_frame.pack(fill=tk.BOTH, expand=True)
            
            # Item name with the price - adjust font size based on layout
            name_label = ttk.Label(inner_frame, text=f"{item.name}", 
                                 font=('Arial', font_size_name, 'bold'))
            name_label.pack(pady=(3, 0), fill=tk.BOTH, expand=True)
            
            price_label = ttk.Label(inner_frame, text=f"${item.price:.2f}", 
                                  font=('Arial', font_size_price))
            price_label.pack(pady=(0, 3), fill=tk.BOTH, expand=True)
            
            # Store reference to the item in the widget
            item_frame.item = item
            inner_frame.item = item
            name_label.item = item
            price_label.item = item
            
            # Make all elements draggable
            for widget in [item_frame, inner_frame, name_label, price_label]:
                widget.bind("<ButtonPress-1>", lambda e, i=item: self.on_drag_start(e, i))
                widget.bind("<B1-Motion>", self.on_drag_motion)
                widget.bind("<ButtonRelease-1>", self.on_drag_release)
            
            # Store widget reference
            self.menu_item_widgets[item.id] = item_frame
            
            col += 1
        
        # Configure grid weights for responsive layout
        for i in range(max_cols):
            self.menu_scrollable_frame.columnconfigure(i, weight=1)

    def on_drag_start(self, event, item):
        """Start dragging a menu item"""
        widget = event.widget
        widget._drag_start_x = event.x
        widget._drag_start_y = event.y
        widget._drag_item = item
        
        # Create a drag image
        self.drag_image = tk.Toplevel(self.root)
        self.drag_image.overrideredirect(True)
        self.drag_image.attributes('-topmost', True)
        self.drag_image.attributes('-alpha', 0.7)
        
        # Create a more visible drag image
        frame = ttk.Frame(self.drag_image, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Adjust drag image font size based on current layout
        if self.current_layout == "mobile":
            font_size = 10
        else:
            font_size = 11
            
        label = ttk.Label(frame, text=f"{item.name}\n${item.price:.2f}",
                        background='lightblue', font=('Arial', font_size, 'bold'), padding=10)
        label.pack(fill=tk.BOTH, expand=True)
        
        # Position the drag image at cursor
        x, y = self.root.winfo_pointerxy()
        self.drag_image.geometry(f"+{x}+{y}")
        
        # Highlight drop zones
        self.highlight_drop_zones(True)

    def on_drag_motion(self, event):
        """Handle the drag motion"""
        if hasattr(self, 'drag_image'):
            x, y = self.root.winfo_pointerxy()
            self.drag_image.geometry(f"+{x}+{y}")

    def on_drag_release(self, event):
        """Handle the release of a dragged item"""
        if hasattr(self, 'drag_image'):
            # Get the current position
            x, y = self.root.winfo_pointerxy()
            
            # Check if we're over a drop zone
            drop_zone = None
            
            # Check main drop zone
            drop_x = self.drop_frame.winfo_rootx()
            drop_y = self.drop_frame.winfo_rooty()
            drop_w = self.drop_frame.winfo_width()
            drop_h = self.drop_frame.winfo_height()
            
            if (drop_x <= x <= drop_x + drop_w and 
                drop_y <= y <= drop_y + drop_h):
                # Main order drop zone
                drop_zone = "main"
            
            # Check individual tabs if they exist
            for person_idx, person_data in enumerate(self.individual_trees.values(), 1):
                if self.order_notebook.select() == str(person_data['frame']):
                    person_drop = person_data.get('drop_frame')
                    if person_drop:
                        p_drop_x = person_drop.winfo_rootx()
                        p_drop_y = person_drop.winfo_rooty()
                        p_drop_w = person_drop.winfo_width()
                        p_drop_h = person_drop.winfo_height()
                        
                        if (p_drop_x <= x <= p_drop_x + p_drop_w and 
                            p_drop_y <= y <= p_drop_y + p_drop_h):
                            drop_zone = f"person_{person_idx-1}"
                            break
            
            # Destroy the drag image
            self.drag_image.destroy()
            delattr(self, 'drag_image')
            
            # Remove highlight from drop zones
            self.highlight_drop_zones(False)
            
            # If dropped in a valid zone, trigger add item
            if drop_zone and hasattr(event.widget, '_drag_item'):
                item = event.widget._drag_item
                if drop_zone == "main":
                    self.on_drop(item)
                elif drop_zone.startswith("person_"):
                    person_idx = int(drop_zone.split('_')[1])
                    self.on_drop(item, person_idx)

    def highlight_drop_zones(self, highlight=True):
        """Highlight or unhighlight drop zones"""
        style = 'TLabelframe.Label'
        if highlight:
            self.root.option_add('*TLabelframe.Label.foreground', 'blue')
            self.drop_frame.configure(style='Highlight.TLabelframe')
            # Highlight individual drop zones if visible
            for person_data in self.individual_trees.values():
                if 'drop_frame' in person_data:
                    person_data['drop_frame'].configure(style='Highlight.TLabelframe')
        else:
            self.root.option_add('*TLabelframe.Label.foreground', '')
            self.drop_frame.configure(style='TLabelframe')
            # Remove highlight from individual drop zones
            for person_data in self.individual_trees.values():
                if 'drop_frame' in person_data:
                    person_data['drop_frame'].configure(style='TLabelframe')

    def on_drop(self, item, person_idx=None):
        """Handle item drop on order"""
        # This will be connected to the controller to add the item
        if hasattr(self, 'on_add_item_callback'):
            self.on_add_item_callback(item, person_idx)

    def set_on_add_item_callback(self, callback):
        """Set callback for adding items to order"""
        self.on_add_item_callback = callback

    def update_individual_tabs(self, num_people):
        """Update personal order paging"""
        # Remove existing personal pages
        for tab in list(self.individual_trees.keys()):
            if tab not in [f"Person {i+1}" for i in range(num_people)]:
                self.order_notebook.forget(self.individual_trees[tab]['frame'])
                del self.individual_trees[tab]
        
        # Add or update personal pages
        for i in range(num_people):
            person_name = f"Person {i+1}"
            translated_name = f"{self.get_text('person')} {i+1}"
            
            if person_name not in self.individual_trees:
                # Create a new page
                person_frame = ttk.Frame(self.order_notebook)
                self.order_notebook.add(person_frame, text=translated_name)
                
                # Create a drop zone for this person
                person_drop_frame = ttk.LabelFrame(person_frame, 
                                                 text=f"{self.get_text('drop_items_here')} - {translated_name}")
                person_drop_frame.pack(fill=tk.X, padx=5, pady=5, ipady=10)
                
                # Adjust label size based on current layout
                if self.current_layout == "mobile":
                    font_size = 9
                else:
                    font_size = 10
                
                person_drop_label = ttk.Label(person_drop_frame, 
                                           text=f"{self.get_text('drag_hint')} - {translated_name}",
                                           font=('Arial', font_size), foreground='gray')
                person_drop_label.pack(pady=20)
                
                # Create the treeview for this page
                person_tree = ttk.Treeview(person_frame, columns=('Name', 'Quantity', 'Price'), show='headings')
                person_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
                
                person_tree.heading('Name', text=self.get_text("name"))
                person_tree.heading('Quantity', text=self.get_text("quantity"))
                person_tree.heading('Price', text=self.get_text("price"))
                
                # Adjust column widths based on layout
                if self.current_layout == "mobile":
                    person_tree.column('Name', width=80)
                    person_tree.column('Quantity', width=40)
                    person_tree.column('Price', width=60)
                else:
                    person_tree.column('Name', width=150)
                    person_tree.column('Quantity', width=80)
                    person_tree.column('Price', width=100)
                
                # Save reference
                self.individual_trees[person_name] = {
                    'frame': person_frame,
                    'tree': person_tree,
                    'drop_frame': person_drop_frame
                }
                # Bind events
                person_tree.bind("<<TreeviewSelect>>", self.on_order_item_selected)

    def show_individual_order_context_menu(self, event, tree, person_index):
        item_id = tree.identify_row(event.y)
        if item_id:
            tree.selection_set(item_id)
            
            context_menu = tk.Menu(self.root, tearoff=0)
            context_menu.add_command(label=self.get_text("delete_item"), 
                                command=lambda: self.on_delete_individual_item(item_id, tree, person_index))
            context_menu.add_command(label=self.get_text("decrease_quantity"), 
                                command=lambda: self.on_decrease_individual_quantity(item_id, tree, person_index))
            
            context_menu.post(event.x_root, event.y_root)

    def set_on_remove_item_callback(self, callback):
        self.on_remove_item_callback = callback

    def set_on_decrease_quantity_callback(self, callback):
        self.on_decrease_quantity_callback = callback

    def on_delete_individual_item(self, item_id, tree, person_index):
        if item_id:
            item_name = tree.item(item_id, 'values')[0]
            # Notify the controller via callback
            if hasattr(self, 'on_remove_item_callback'):
                self.on_remove_item_callback(item_name, person_index)

    def on_decrease_individual_quantity(self, item_id, tree, person_index):
        if item_id:
            # Get the item name and current quantity
            values = tree.item(item_id, 'values')
            item_name = values[0]
            current_qty = int(values[1])
            
            if current_qty > 1:
                # Notify the controller to reduce the number through callback
                if hasattr(self, 'on_decrease_quantity_callback'):
                    self.on_decrease_quantity_callback(item_name, person_index)
            else:
                # If the quantity is 1, delete it directly
                self.on_delete_individual_item(item_id, tree, person_index)

    def update_order_display(self, order_items, total, split_items=None):
        """Update order display, including total orders and individual orders"""
        # Update total order display
        for item in self.order_tree.get_children():
            self.order_tree.delete(item)
        for item, quantity in order_items:
            self.order_tree.insert('', 'end', values=(item.name, quantity, f"${item.price * quantity:.2f}"))
        
        # Adjust total order column widths based on layout
        if self.current_layout == "mobile":
            self.order_tree.column('Name', width=80)
            self.order_tree.column('Quantity', width=40)
            self.order_tree.column('Price', width=60)
        else:
            self.order_tree.column('Name', width=150)
            self.order_tree.column('Quantity', width=80)
            self.order_tree.column('Price', width=100)
        
        # If there is split account information, update personal order display
        if split_items:
            for person_idx, (items, subtotal) in enumerate(split_items):
                person_name = f"Person {person_idx+1}"
                if person_name in self.individual_trees:
                    tree = self.individual_trees[person_name]['tree']
                    # Clear existing items
                    for item in tree.get_children():
                        tree.delete(item)
                    # Add New Items
                    for item, quantity in items:
                        tree.insert('', 'end', values=(item.name, quantity, f"${item.price * quantity:.2f}"))
        
        self.total_label.config(text=f"{self.get_text('total')}: ${total:.2f}")

    def show_message(self, message):
        messagebox.showinfo(self.get_text("information"), message)

    def display_split_bills(self, split_bills):
        # Create a responsive split bill window
        split_bill_window = tk.Toplevel(self.root)
        split_bill_window.title(self.get_text("split_bill"))
        
        # Adjust size based on current layout
        if self.current_layout == "mobile":
            split_bill_window.geometry("400x500")
        else:
            split_bill_window.geometry("600x400")

        main_canvas = tk.Canvas(split_bill_window)
        scrollbar = ttk.Scrollbar(split_bill_window, orient="vertical", command=main_canvas.yview)
        scrollable_frame = ttk.Frame(main_canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
        )
        
        main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        main_canvas.configure(yscrollcommand=scrollbar.set)
        
        main_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Sub-bills
        for i, (items, subtotal) in enumerate(split_bills, 1):
            frame = ttk.LabelFrame(scrollable_frame, text=f"{self.get_text('person')} {i}")
            frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
            
            if not items:  # Check if there are items
                ttk.Label(frame, text=self.get_text("no_items")).pack(pady=10)
                ttk.Label(frame, text=f"{self.get_text('subtotal')}: $0.00", 
                        font=('Arial', 12 if self.current_layout != "mobile" else 11, 'bold')).pack(anchor=tk.E, padx=10, pady=5)
                continue
            
            bill_tree = ttk.Treeview(frame, columns=('Name', 'Quantity', 'Price'), show='headings', 
                                    height=4 if self.current_layout == "mobile" else 5)
            bill_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
            
            # Add a horizontal scroll bar
            tree_scrollbar_x = ttk.Scrollbar(frame, orient="horizontal", command=bill_tree.xview)
            bill_tree.configure(xscrollcommand=tree_scrollbar_x.set)
            tree_scrollbar_x.pack(fill="x")
            
            bill_tree.heading('Name', text=self.get_text("name"))
            bill_tree.heading('Quantity', text=self.get_text("quantity"))
            bill_tree.heading('Price', text=self.get_text("price"))
            
            # Set column width based on layout
            if self.current_layout == "mobile":
                bill_tree.column('Name', width=100, minwidth=80)
                bill_tree.column('Quantity', width=60, minwidth=40)
                bill_tree.column('Price', width=80, minwidth=60)
            else:
                bill_tree.column('Name', width=150, minwidth=100)
                bill_tree.column('Quantity', width=80, minwidth=60)
                bill_tree.column('Price', width=100, minwidth=80)
            
            for item, quantity in items:
                bill_tree.insert('', 'end', values=(item.name, quantity, f"${item.price * quantity:.2f}"))
                
            ttk.Label(frame, text=f"{self.get_text('subtotal')}: ${subtotal:.2f}", 
                    font=('Arial', 12 if self.current_layout != "mobile" else 11, 'bold')).pack(anchor=tk.E, padx=10, pady=5)
        
        # Add Print and Close buttons
        button_frame = ttk.Frame(scrollable_frame)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Adjust button layout based on current display
        if self.current_layout == "mobile":
            ttk.Button(button_frame, text=self.get_text("print_bills"), 
                    command=lambda: self.show_message(self.get_text("printing_bills"))).pack(fill=tk.X, padx=5, pady=2)
            ttk.Button(button_frame, text=self.get_text("close"), 
                    command=split_bill_window.destroy).pack(fill=tk.X, padx=5, pady=2)
        else:
            ttk.Button(button_frame, text=self.get_text("print_bills"), 
                    command=lambda: self.show_message(self.get_text("printing_bills"))).pack(side=tk.LEFT, padx=5)
            ttk.Button(button_frame, text=self.get_text("close"), 
                    command=split_bill_window.destroy).pack(side=tk.RIGHT, padx=5)

# controller
class POSController:
    def __init__(self, menu_model, view, language_model,root):
        self.menu_model = menu_model
        self.view = view
        self.language_model = language_model
        self.current_order = Order()
        self.root = root

        # Set the language model to the view
        self.view.set_menu_model(self.menu_model)

        # Set language change callback
        self.view.set_on_language_change_callback(self.on_language_change)

        # Setting callbacks
        self.view.set_on_add_item_callback(self.add_to_order_drag_drop)
        self.view.set_on_delete_button_callback(self.view.on_delete_button_clicked)
        self.view.set_on_remove_item_callback(self.remove_from_order)
        self.view.set_on_decrease_quantity_callback(self.decrease_item_quantity)

        # Binding Events
        self.view.clear_button.config(command=self.clear_order)
        self.view.checkout_button.config(command=self.checkout)
        self.view.split_bill_button.config(command=self.split_bill)
        self.view.add_person_btn.config(command=self.add_person)
        self.view.remove_person_btn.config(command=self.remove_person)
        self.view.selected_category.trace("w", self.on_category_change)
        self.view.logout_button.config(command=self.logout_funtion)

        # Set category change callback
        self.view.on_category_change_callback = self.on_category_change

        # Initialize order
        self.reset_order()

        # Initialize menu display
        self.initialize_menu()

        # Update the number of people to select
        self.update_person_spinbox_range()
    def logout_funtion(self):
        confirm = messagebox.askyesno(
            self.view.get_text("logout"),
            self.view.get_text("confirm_logout")
        )
        if confirm:
            self.root.quit()  # 結束 Tkinter 事件循環
            self.root.destroy()  # 銷毀 Tkinter 主視窗
            subprocess.Popen([sys.executable, "login_interface.py"], start_new_session=True)  # 啟動登入視窗

        

    def on_language_change(self):
        self.initialize_menu()
        self.update_all_displays()

    def remove_from_order(self, item_name, person_index=None):
        # Find the corresponding menu item
        menu_items = self.menu_model.get_menu_items()
        target_item = next((item for item in menu_items if item.name == item_name), None)

        if target_item:
            # Remove from order
            people_count = self.view.people_count.get()

            if people_count > 1 and person_index is not None:
                # Remove from the specified person's order
                self.current_order.remove_item(target_item.id, sub_order_index=person_index)
            else:
                # Remove from total order
                self.current_order.remove_item(target_item.id)

            # Update Display
            self.update_all_displays()

    def decrease_item_quantity(self, item_name, person_index=None):
        # Find the corresponding menu item
        menu_items = self.menu_model.get_menu_items()
        target_item = next((item for item in menu_items if item.name == item_name), None)

        if target_item:
            # Reduce quantity from order (remove 1)
            people_count = self.view.people_count.get()

            if people_count > 1 and person_index is not None:
                # Reduce from the order of the designated person
                self.current_order.remove_item(target_item.id, quantity=1, sub_order_index=person_index)
            else:
                # Subtract from total order
                self.current_order.remove_item(target_item.id, quantity=1)

            # Update Display
            self.update_all_displays()

    def initialize_menu(self):
        menu_items = self.menu_model.get_menu_items()
        categories = sorted(set(item.category for item in menu_items))
        self.view.create_menu_items(menu_items, categories)

    def on_category_change(self, *args):
        self.initialize_menu()

    def reset_order(self):
        self.current_order = Order()
        self.view.update_individual_tabs(1)
        self.update_all_displays()

    def add_person(self):
        current_count = self.view.people_count.get()
        self.view.people_count.set(current_count + 1)
        self.update_person_spinbox_range()
        if len(self.current_order.sub_orders) < current_count + 1:
            self.current_order.sub_orders.append([])
        # Update order paging display
        self.view.update_individual_tabs(current_count + 1)
        # Update all order display
        self.update_all_displays()

    def remove_person(self):
        current_count = self.view.people_count.get()
        if current_count > 1:
            self.view.people_count.set(current_count - 1)
            self.update_person_spinbox_range()
            if len(self.current_order.sub_orders) > current_count - 1:
                self.current_order.sub_orders.pop()
            # Update order paging display
            self.view.update_individual_tabs(current_count - 1)
            # Update all order display
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

        # Set table number from view
        self.current_order.table_number = self.view.table_number.get() if self.view.table_number.get() else None

        table_info = f" {self.language_model.get_text('for_table')} {self.current_order.table_number}" if self.current_order.table_number else ""
        group_info = f" ({self.language_model.get_text('group_order')})" if self.current_order.is_group_order() else ""

        self.view.show_message(f"{self.language_model.get_text('order')}{table_info}{group_info} {self.language_model.get_text('completed')}! {self.language_model.get_text('total')}: ${self.current_order.total:.2f}")
        self.clear_order()


def main():
    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()

    # Create a style for highlighted drop zones.
    style = ttk.Style()
    style.configure("Highlight.TLabelframe", background="lightblue")

    # Initialize the static menu model and language model.
    menu_model = MenuModel()
    language_model = LanguageModel()

    # Initialize the view (POSView) and pass in the language model.
    view = POSView(root, language_model)

    # Create an Employee instance (adjust the details as needed).
    employee = Employee(2001, "VIP Customer", "VIP")

    # Initialize the unified controller.
    #controller = Controller(employee, menu_model, view, language_model)
    controller = POSController(menu_model, view, language_model,root)
    # At this point, the controller has set up all callbacks in the view,
    # and the unified backend is used for all product and order operations.
    root.mainloop()


if __name__ == "__main__":
    main()

