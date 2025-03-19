# model
import random
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import subprocess, sys, random

LANGUAGES = {
    "English": {
        "choose_language": "Choose Language:", 
        "menu": "Menu",
        "current_order": "Current Order",
        "total": "Total",
        "checkout": "Checkout",
        "clear_order": "Clear Order",
        "split_bill": "Split Bill",
        "show_vip_balance": "Show VIP Balance",
        "pay_from_account": "Pay from Account",
        "top_up": "Top Up",
        "logout": "Logout",
        "unlock": "Unlock",
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
        "total_order": "Total Order",
        "quantity": "Quantity",
        "person": "Person",
        "persons": "Persons",
        "bill": "Bill",
        "choose_person": "Choose Person",
        "drop_items_here": "Drop items here",
        "drag_hint": "Drag menu items here to add to order",
        "order_table": {
                    "name": "Name",
                    "quantity": "Quantity",
                    "price": "Price"
                },
        "categories": {
            "Alcoholic Drinks": "Alcoholic Drinks",
            "Classic Cocktails": "Classic Cocktails",
            "Non-Alcoholic Specials": "Non-Alcoholic Specials",
            "Bar Snacks": "Bar Snacks",
            "Main Dishes": "Main Dishes",
            "Desserts": "Desserts",
            "Special Menu": "Special Menu",
        },
        "unlock_fridge": "Unlock Fridge",
        "locker_code": "Locker Code",
        "hidden": "Hidden",
        "enter_valid_code": "Please enter a valid 4-digit code.",
        "unlocked": "Unlocked! Enjoy your drink. Remaining balance: {} USD",
        "not_enough_balance": "Not enough balance! Remaining balance: {} USD. Please add more.",
        "wrong_code": "Wrong code! Try again.",
        "information": "Information",
        "subtotal": "Subtotal",
        "print_bills": "Print Bills",
        "printing_bills": "Printing bills...",
        "close": "Close",
        "all": "All",
        "for_table": "for table",
        "group_order_msg": "(Group order)",
        "order_completed": "Order completed!",
        "order_is_empty": "The order is empty",
        "not_group_order": "This is not a group order.",
        "no_items_to_split": "No items to split",
        "your_vip_balance": "Your VIP balance is: ${}",
        "insufficient_balance": "Insufficient VIP balance!",
        "top_up_prompt": "Enter amount to top-up:",
        "recharged": "Recharged!\n New Balance: {} USD",
        "confirm_logout": "Are you sure you want to logout?",
        "success": "Success",
        "no_items": "No items",
    },

    "中文": {
        "choose_language": "選擇語言:",
        "menu": "菜單",
        "current_order": "當前訂單",
        "total": "總計",
        "checkout": "結帳",
        "clear_order": "清除訂單",
        "split_bill": "分攤帳單",
        "show_vip_balance": "顯示 VIP 餘額",
        "pay_from_account": "從帳戶支付",
        "top_up": "儲值",
        "logout": "登出",
        "unlock": "解鎖",
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
        "all": "全部",
        "choose_person": "選擇顧客",
        "unlock_fridge": "解鎖冰箱",
        "locker_code": "鎖櫃密碼",
        "hidden": "隱藏",
        "enter_valid_code": "請輸入有效的4位數密碼。",
        "unlocked": "解鎖成功！享用您的飲料。剩餘餘額：{} 美元",
        "not_enough_balance": "餘額不足！剩餘餘額：{} 美元。請增加儲值。",
        "wrong_code": "密碼錯誤！請重試。",
        "order_table": {
            "name": "名稱",
            "quantity": "數量",
            "price": "價格"
        },
        "categories": {
            "Alcoholic Drinks": "酒精飲品",
            "Classic Cocktails": "經典雞尾酒",
            "Non-Alcoholic Specials": "無酒精特飲",
            "Bar Snacks": "酒吧小吃",
            "Main Dishes": "主菜",
            "Desserts": "甜點",
            "Special Menu": "特別菜單",
        },
        "for_table": "桌號",
        "group_order_msg": "（團體訂單）",
        "order_completed": "訂單完成！",
        "order_is_empty": "訂單是空的",
        "not_group_order": "這不是團體訂單。",
        "no_items_to_split": "沒有可分攤的項目",
        "your_vip_balance": "您的VIP餘額為：${}",
        "insufficient_balance": "VIP餘額不足！",
        "top_up_prompt": "請輸入儲值金額：",
        "recharged": "儲值成功！\n 新餘額：{} 美元",
        "confirm_logout": "確定要登出嗎？",
        "success": "成功",
    },

    "Svenska": {
        "choose_language": "Välj språk:",
        "menu": "Meny",
        "current_order": "Nuvarande beställning",
        "total": "Totalt",
        "checkout": "Betala",
        "clear_order": "Rensa beställning",
        "split_bill": "Dela räkningen",
        "show_vip_balance": "Visa VIP-saldo",
        "pay_from_account": "Betala från konto",
        "top_up": "Ladda upp",
        "logout": "Logga ut",
        "unlock": "Lås upp",
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
        "all": "Alla",
        "choose_person": "Välj Person",
        "unlock_fridge": "Lås upp kylen",
        "locker_code": "Skåpkod",
        "hidden": "Dold",
        "enter_valid_code": "Vänligen ange en giltig 4-siffrig kod.",
        "unlocked": "Upplåst! Njut av din dryck. Återstående saldo: {} USD",
        "not_enough_balance": "Inte tillräckligt med saldo! Återstående saldo: {} USD. Vänligen fyll på mer.",
        "wrong_code": "Fel kod! Försök igen.",
        "order_table": {
            "name": "Namn",
            "quantity": "Antal",
            "price": "Pris"
        },
        "categories": {
            "Alcoholic Drinks": "Alkoholhaltiga drycker",
            "Classic Cocktails": "Klassiska cocktails",
            "Non-Alcoholic Specials": "Alkoholfri specialitet",
            "Bar Snacks": "Bar snacks",
            "Main Dishes": "Huvudrätter",
            "Desserts": "Desserter",
            "Special Menu": "Specialmeny",
        },
        "for_table": "för bord",
        "group_order_msg": "(Gruppbeställning)",
        "order_completed": "Beställning slutförd!",
        "order_is_empty": "Beställningen är tom",
        "not_group_order": "Detta är inte en gruppbeställning.",
        "no_items_to_split": "Inga artiklar att dela",
        "your_vip_balance": "Ditt VIP-saldo är: ${}",
        "insufficient_balance": "Otillräckligt VIP-saldo!",
        "top_up_prompt": "Ange belopp att ladda upp:",
        "recharged": "Laddad! \n Nytt saldo: {} USD",
        "confirm_logout": "Är du säker på att du vill logga ut?",
        "success": "Framgång",
    }
}

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
            if sub_order_index is None:
                sub_order_index = 0  # Default to the first sub-order if not specified

            while len(self.sub_orders) <= sub_order_index:
                self.sub_orders.append([])

            self.sub_orders[sub_order_index].append((item, quantity))
        else:
            self.items.append((item, quantity))
        
        self.total += item.price * quantity

    def remove_item(self, item_id, quantity=1, sub_order_index=None):
        is_group = len(self.sub_orders) > 0

        if is_group and sub_order_index is not None:
            # Check if the sub-order index is valid
            if sub_order_index >= len(self.sub_orders):
                return False

            # Find the item in the sub-order
            for i, (item, item_qty) in enumerate(self.sub_orders[sub_order_index]):
                if item.id == item_id:
                    # If the quantity to remove is less than the item's quantity, decrease the quantity
                    if quantity < item_qty:
                        self.sub_orders[sub_order_index][i] = (item, item_qty - quantity)
                        self.total -= item.price * quantity
                    # Otherwise, remove the entire item
                    else:
                        actual_qty = item_qty  # Actual quantity removed does not exceed the existing quantity
                        self.sub_orders[sub_order_index].pop(i)
                        self.total -= item.price * actual_qty
                    return True
        else:
            # Find the item in the regular order
            for i, (item, item_qty) in enumerate(self.items):
                if item.id == item_id:
                    # If the quantity to remove is less than the item's quantity, decrease the quantity
                    if quantity < item_qty:
                        self.items[i] = (item, item_qty - quantity)
                        self.total -= item.price * quantity
                    # Otherwise, remove the entire item
                    else:
                        actual_qty = item_qty  # Actual quantity removed does not exceed the existing quantity
                        self.items.pop(i)
                        self.total -= item.price * actual_qty
                    return True

        return False  # Item not found

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

class SpecialLocker:
    def __init__(self):
        self.lock_code = self.generate_code()

    def generate_code(self):
        return random.randint(1000, 9999)  # Generate a 4-digit code

    def verify_code(self, code):
        return code == self.lock_code

    def update_code(self):
        self.lock_code = self.generate_code()  # Update the code after a successful purchase

class MenuModel:
    def __init__(self):
        # Sample menu data
        self.vip_account = 100.00
        self.locker = SpecialLocker()

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
            MenuItem(70, "Chocolate Brownie", 8.00, "Desserts"),

            # Special Menu
            MenuItem(71, "Lobster Bisque", 30.00, "Special Menu"),
            MenuItem(72, "Foie Gras", 35.00, "Special Menu"),
            MenuItem(73, "Black Truffle Risotto", 60.00, "Special Menu"),
            MenuItem(74, "Gold Leaf Dessert", 55.00, "Special Menu"),
        ]

    def get_menu_items(self):
        return self.menu_items

    def get_item_by_id(self, item_id):
        return next((item for item in self.menu_items if item.id == item_id), None)

    def get_translated_category(self, category, language):
       
        if language in LANGUAGES and "categories" in LANGUAGES[language]:
            return LANGUAGES[language]["categories"].get(category, category)
        return category

# view
import tkinter as tk
from tkinter import ttk, messagebox

class POSView:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.current_lang = "English"
        self.root.title("VIP POS System")
        self.root.geometry("1430x600")
        self.root.minsize(600, 400)  # Set minimum window size

        # Define breakpoints for responsive design
        self.breakpoints = {
            "mobile": 800,    # Use mobile layout for width less than 800px
            "tablet": 1200    # Use tablet layout for width between 800px and 1200px
        }

        # Track the current layout
        self.current_layout = "desktop"  # Default to desktop layout

        # Set column weights to control the ratio between menu and order sections
        root.columnconfigure(0, weight=4)  # Menu takes 4/5
        root.columnconfigure(1, weight=1)  # Order takes 1/5
        root.rowconfigure(0, weight=1)

        # Create main frames using grid instead of pack
        self.menu_frame = ttk.Frame(root)
        self.menu_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        self.order_frame = ttk.Frame(root)
        self.order_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Create title frame
        self.title_frame = ttk.Frame(self.menu_frame)
        self.title_frame.pack(fill=tk.X)

        # Menu label
        self.menu_label = ttk.Label(self.title_frame, text=self.get_text("menu"),
                                   font=('Arial', 16, 'bold'))
        self.menu_label.pack(side=tk.LEFT, pady=5)

        # Create language selection frame
        self.language_frame = ttk.Frame(self.title_frame)
        self.language_frame.pack(side=tk.RIGHT, padx=5, pady=5)

        # Language selection label
        self.label_choose_language = ttk.Label(self.language_frame,
                                             text=self.get_text("choose_language"),
                                             font=("Arial", 10))
        self.label_choose_language.pack(side=tk.LEFT, padx=(0, 5))

        # Language selection dropdown
        self.language_var = tk.StringVar(self.root)
        self.language_var.set(self.current_lang)  # Default language
        
        self.language_menu = ttk.OptionMenu(self.language_frame,
            self.language_var,
            *LANGUAGES.keys(),
            command=self.change_language)
        self.language_menu.pack(side=tk.LEFT)
        self.update_language_menu()

        # Create menu category frame (better visual organization)
        self.categories_frame = ttk.Frame(self.menu_frame)
        self.categories_frame.pack(fill=tk.X, pady=5)
        
        # Two rows for category buttons
        self.categories_row1 = ttk.Frame(self.categories_frame)
        self.categories_row1.pack(fill=tk.X)
        
        self.categories_row2 = ttk.Frame(self.categories_frame)
        self.categories_row2.pack(fill=tk.X, pady=(5, 0))
        
        # Category buttons
        self.category_buttons = {}
        self.selected_category = tk.StringVar(value="All")
        
        # Menu items frame with scrollbar
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
        
        # Order section and label
        self.order_title_frame = ttk.Frame(self.order_frame)
        self.order_title_frame.pack(fill=tk.X)
        
        self.order_label = ttk.Label(self.order_title_frame, text=self.get_text("current_order"),
                                    font=('Arial', 16, 'bold'))
        self.order_label.pack(pady=5)
        
        # Order controls
        order_config_frame = ttk.Frame(self.order_frame)
        order_config_frame.pack(fill=tk.X, pady=5)
        
        # Table number control
        self.table_text = ttk.Label(order_config_frame, text=f"{self.get_text('table_number')}:")
        self.table_text.pack(side=tk.LEFT, padx=5)
        self.table_number = ttk.Entry(order_config_frame, width=5)
        self.table_number.pack(side=tk.LEFT, padx=5)
        
        # Group size control
        self.group_control_frame = ttk.Frame(order_config_frame)
        self.group_control_frame.pack(side=tk.LEFT, padx=10)
        
        self.person_text = ttk.Label(self.group_control_frame, text=f"{self.get_text('persons')}:")
        self.person_text.pack(side=tk.LEFT, padx=5)
        self.people_count = tk.IntVar(value=1)
        self.people_count_label = ttk.Label(self.group_control_frame, textvariable=self.people_count)
        self.people_count_label.pack(side=tk.LEFT, padx=5)
        
        self.add_person_btn = ttk.Button(self.group_control_frame, text="+", width=2)
        self.add_person_btn.pack(side=tk.LEFT, padx=2)
        
        self.remove_person_btn = ttk.Button(self.group_control_frame, text="-", width=2)
        self.remove_person_btn.pack(side=tk.LEFT, padx=2)

        # Add person selector
        self.current_person = tk.IntVar(value=1)
        self.choose_person_text = ttk.Label(self.group_control_frame, text=f"{self.get_text('choose_person')}:")
        self.choose_person_text.pack(side=tk.LEFT, padx=5)
        self.person_spinbox = ttk.Spinbox(
            self.group_control_frame, 
            from_=1, 
            to=1, 
            width=5,
            textvariable=self.current_person
        )
        self.person_spinbox.pack(side=tk.LEFT, padx=5)
        
        # Create notebook
        self.order_notebook = ttk.Notebook(self.order_frame)
        self.order_notebook.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Total order tab
        self.total_order_frame = ttk.Frame(self.order_notebook)
        self.order_notebook.add(self.total_order_frame, text=self.get_text("total_order"))
        
        # Create drop area frame
        self.drop_frame = ttk.LabelFrame(self.total_order_frame, text=self.get_text("drop_items_here"))
        self.drop_frame.pack(fill=tk.X, padx=5, pady=5, ipady=10)
        
        # Drop area label
        self.drop_label = ttk.Label(self.drop_frame, text=self.get_text("drag_hint"),
                                  font=('Arial', 10), foreground='gray')
        self.drop_label.pack(pady=20)
        
        # Create total order treeview
        self.order_tree = ttk.Treeview(self.total_order_frame, columns=('Name', 'Quantity', 'Price'), show='headings')
        self.order_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
       
        self.order_tree.heading('Name', text=self.get_text("order_table")["name"])
        self.order_tree.heading('Quantity', text=self.get_text("order_table")["quantity"])
        self.order_tree.heading('Price', text=self.get_text("order_table")["price"])

        # Set column widths
        self.order_tree.column('Name', width=150, minwidth=100)
        self.order_tree.column('Quantity', width=80, minwidth=60)
        self.order_tree.column('Price', width=100, minwidth=80)
        
        # Individual order frames (to be dynamically populated)
        self.individual_trees = {}  # Store treeviews for each person
        
        # Create order summary frame
        self.summary_frame = ttk.Frame(self.order_frame)
        self.summary_frame.pack(fill=tk.X, pady=5)

        # Total and fridge unlock frame
        self.total_frame = ttk.Frame(self.summary_frame)
        self.total_frame.pack(fill=tk.X, pady=5)

        # Total label
        self.total_label = ttk.Label(self.total_frame, text=f"{self.get_text('total')}: $0.00", font=('Arial', 14))
        self.total_label.pack(side=tk.LEFT, padx=10)

        # Locker code label
        self.locker_frame = ttk.Frame(self.summary_frame)
        self.locker_frame.pack(fill=tk.X, pady=5)

        self.locker_code_label = ttk.Label(self.locker_frame,
                                         text=f"{self.get_text('locker_code')}: {self.get_text('hidden')}",
                                         font=('Arial', 12))
        self.locker_code_label.pack(side=tk.LEFT, padx=10)

        # Password entry
        self.unlock_entry = ttk.Entry(self.locker_frame, width=6, show="*")
        self.unlock_entry.pack(side=tk.LEFT, padx=10)

        # Unlock button
        self.unlock_button = ttk.Button(self.locker_frame, text=self.get_text("unlock_fridge"))
        self.unlock_button.pack(side=tk.LEFT, padx=10)

        # Button frame - use more rows for better button organization
        self.button_frame = ttk.Frame(self.order_frame)
        self.button_frame.pack(fill=tk.X, pady=5)
        
        # Basic order operation buttons row
        self.basic_button_frame = ttk.Frame(self.button_frame)
        self.basic_button_frame.pack(fill=tk.X, pady=2)

        self.clear_button = ttk.Button(self.basic_button_frame, text=self.get_text("clear_order"))
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        self.checkout_button = ttk.Button(self.basic_button_frame, text=self.get_text("checkout"))
        self.checkout_button.pack(side=tk.LEFT, padx=5)

        self.split_bill_button = ttk.Button(self.basic_button_frame, text=self.get_text("split_bill"))
        self.split_bill_button.pack(side=tk.LEFT, padx=5)

        # VIP feature buttons row
        self.vip_button_frame = ttk.Frame(self.button_frame)
        self.vip_button_frame.pack(fill=tk.X, pady=2)

        self.vip_balance_button = ttk.Button(self.vip_button_frame, text=self.get_text("show_vip_balance"))
        self.vip_balance_button.pack(side=tk.LEFT, padx=5)
        
        self.pay_from_account_button = ttk.Button(self.vip_button_frame, text=self.get_text("pay_from_account"))
        self.pay_from_account_button.pack(side=tk.LEFT, padx=5)

        self.topup_button = ttk.Button(self.vip_button_frame, text=self.get_text("top_up"))
        self.topup_button.pack(side=tk.LEFT, padx=5)

        # Logout button row
        self.logout_frame = ttk.Frame(self.button_frame)
        self.logout_frame.pack(fill=tk.X, pady=2)

        self.logout_button = ttk.Button(self.logout_frame, text=self.get_text("logout"))
        self.logout_button.pack(side=tk.LEFT, padx=5)

        # Dictionary to store menu item widgets
        self.menu_item_widgets = {}

        # Set right-click context menu binding
        self.order_tree.bind("<Button-3>", self.show_order_context_menu)

        # Bind window resize event
        self.root.bind("<Configure>", self.on_window_resize)

        # Set maximum menu columns
        self.max_menu_cols = 3  # Default to 3 columns for desktop

    def get_text(self, key):
        """獲取當前語言的文本"""
        if key in LANGUAGES[self.current_lang]:
            return LANGUAGES[self.current_lang][key]
        # Handle nested dictionary keys
        if isinstance(key, str) and "." in key:
            parts = key.split(".")
            current = LANGUAGES[self.current_lang]
            for part in parts:
                if part in current:
                    current = current[part]
                else:
                    return key
                return current
        return key

    def change_language(self, selected_lang):
            """Switch language and update the UI"""
            self.current_lang = selected_lang

            # Update main interface elements' text
            self.menu_label.config(text=self.get_text("menu"))
            self.order_label.config(text=self.get_text("current_order"))
            self.label_choose_language.config(text=self.get_text("choose_language"))

            # Update order control area text
            self.table_text.config(text=f"{self.get_text('table_number')}:")
            self.person_text.config(text=f"{self.get_text('persons')}:")
            self.choose_person_text.config(text=f"{self.get_text('choose_person')}:")

            # Update drag-and-drop area text
            self.drop_frame.config(text=self.get_text("drop_items_here"))
            self.drop_label.config(text=self.get_text("drag_hint"))

            # Update order table headers
            self.order_tree.heading('Name', text=self.get_text("order_table")["name"])
            self.order_tree.heading('Quantity', text=self.get_text("order_table")["quantity"])
            self.order_tree.heading('Price', text=self.get_text("order_table")["price"])

            # Update order tab text
            self.order_notebook.tab(0, text=self.get_text("total_order"))

            # Update individual order tab text
            for i, (person_name, tab_data) in enumerate(self.individual_trees.items()):
                new_name = f"{self.get_text('person')} {i+1}"
                self.order_notebook.tab(tab_data['frame'], text=new_name)
                if 'drop_frame' in tab_data:
                    tab_data['drop_frame'].config(text=f"{self.get_text('drop_items_here')} - {new_name}")

                # Update individual order table headers
                tab_data['tree'].heading('Name', text=self.get_text("order_table")["name"])
                tab_data['tree'].heading('Quantity', text=self.get_text("order_table")["quantity"])
                tab_data['tree'].heading('Price', text=self.get_text("order_table")["price"])

            # Update total label - retain the current amount
            current_total = self.total_label.cget("text").split("$")[1]
            self.total_label.config(text=f"{self.get_text('total')}: ${current_total}")

            # Update locker-related elements
            self.locker_code_label.config(text=f"{self.get_text('locker_code')}: {self.get_text('hidden')}")
            self.unlock_button.config(text=self.get_text("unlock_fridge"))

            # Update button text
            self.clear_button.config(text=self.get_text("clear_order"))
            self.checkout_button.config(text=self.get_text("checkout"))
            self.split_bill_button.config(text=self.get_text("split_bill"))
            self.vip_balance_button.config(text=self.get_text("show_vip_balance"))
            self.pay_from_account_button.config(text=self.get_text("pay_from_account"))
            self.topup_button.config(text=self.get_text("top_up"))
            self.logout_button.config(text=self.get_text("logout"))

            # Update menu category buttons
            self.update_menu_categories()

            # Update language dropdown menu
            self.update_language_menu()
       
    def update_language_menu(self):
            """Update the language selection dropdown menu"""
            menu = self.language_menu["menu"]
            menu.delete(0, "end")  # Clear old options
            
            for lang in LANGUAGES.keys():
                menu.add_command(label=lang,
                    command=lambda value=lang: self.language_var.set(value) or self.change_language(value))

    def update_menu_categories(self):
            """Update the text of menu category buttons"""
            # Special handling for the "All" category button
            if "All" in self.category_buttons:
                self.category_buttons["All"].config(text=self.get_text("all"))

            # Other category buttons
            for category, button in self.category_buttons.items():
                if category != "All":
                    translated = self.model.get_translated_category(category, self.current_lang)
                    button.config(text=translated)

    def update_locker_code(self, code):
            """Update the locker code display - for development mode, show the code for testing"""
            print(f"Locker Code: {code}")
            # This display can be removed in production

    def show_order_context_menu(self, event):
            """Show the right-click context menu for order items"""
            # Get the clicked item
            item_id = self.order_tree.identify_row(event.y)
            if item_id:
                # Select the clicked item
                self.order_tree.selection_set(item_id)

                # Create the right-click menu
                context_menu = tk.Menu(self.root, tearoff=0)
                context_menu.add_command(
                label=self.get_text("delete_item"),
                command=lambda: self.on_delete_item(item_id)
                )
                context_menu.add_command(
                    label=self.get_text("decrease_quantity"),
                    command=lambda: self.on_decrease_quantity(item_id)
                )

                # Display the context menu
                context_menu.post(event.x_root, event.y_root)

    def on_delete_item(self, item_id):
        """Callback to delete an item from the order"""
        if item_id:
            # Get the item name
            item_name = self.order_tree.item(item_id, 'values')[0]

            # Notify the controller via callback
            if hasattr(self, 'on_remove_item_callback'):
                # Decide whether to delete from the main order or an individual order based on the current tab
                current_tab = self.order_notebook.select()

                if current_tab == str(self.total_order_frame):
                    # Main order tab
                    self.on_remove_item_callback(item_name)
                else:
                    # Individual order tab
                    for idx, (tab_name, tab_data) in enumerate(self.individual_trees.items()):
                        if current_tab == str(tab_data['frame']):
                            self.on_remove_item_callback(item_name, idx)
                            break

    def on_decrease_quantity(self, item_id):
        """Callback to decrease the quantity of an item in the order"""
        if item_id:
            # Get the item name and current quantity
            values = self.order_tree.item(item_id, 'values')
            item_name = values[0]
            current_qty = int(values[1])

            if current_qty > 1:
                # Notify the controller via callback to decrease the quantity
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
                # If the quantity is 1, directly delete the item
                self.on_delete_item(item_id)

    def on_window_resize(self, event):
        """Handle window resizing to apply responsive layouts"""
        # Only handle events from the root window, not child widgets
        if event.widget == self.root:
            width = event.width

            # Determine the layout based on the window width
            if width < self.breakpoints["mobile"] and self.current_layout != "mobile":
                self.apply_mobile_layout()
                self.current_layout = "mobile"
            elif width >= self.breakpoints["mobile"] and width < self.breakpoints["tablet"] and self.current_layout != "tablet":
                self.apply_tablet_layout()
                self.current_layout = "tablet"
            elif width >= self.breakpoints["tablet"] and self.current_layout != "desktop":
                self.apply_desktop_layout()
                self.current_layout = "desktop"

            # Rebuild the menu using the current category
            current_category = self.selected_category.get()
            self.root.after(100, lambda: self.rebuild_menu_after_resize(current_category))

    def apply_mobile_layout(self):
        """Apply mobile layout"""
        # Reconfigure the grid to stack menu and order sections vertically
        self.root.grid_columnconfigure(0, weight=1)  # Full width
        self.root.grid_columnconfigure(1, weight=1)  # Hidden/collapsed

        # Move the order frame below the menu frame
        self.order_frame.grid_forget()
        self.order_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        # Reduce category button size and adjust padding
        for cat_btn in self.category_buttons.values():
            cat_btn.configure(padding=(2, 1))

        # Adjust menu items to use fewer columns
        self.max_menu_cols = 2  # Mobile mode: 2 columns

        # Adjust font sizes
        self.menu_label.configure(font=('Arial', 14, 'bold'))
        self.order_label.configure(font=('Arial', 14, 'bold'))
        self.total_label.configure(font=('Arial', 12))

        # Make order controls more compact
        self.table_number.configure(width=3)
        self.person_spinbox.configure(width=3)

        # Adjust treeview height
        self.order_tree.configure(height=4)
        for person_data in self.individual_trees.values():
            if 'tree' in person_data:
                person_data['tree'].configure(height=4)

        # Adjust drop area size
        self.drop_frame.pack(fill=tk.X, padx=5, pady=3, ipady=5)
        self.drop_label.pack(pady=10)

        # Stack VIP-related configurations
        self.locker_frame.pack_forget()
        self.locker_frame.pack(fill=tk.X, pady=2)

        # Adjust VIP-related element sizes
        self.locker_code_label.configure(font=('Arial', 10))
        self.unlock_entry.configure(width=4)

        # Rearrange buttons
        # Basic order operation buttons
        for button in [self.clear_button, self.checkout_button, self.split_bill_button]:
            button.pack_forget()
            button.pack(fill=tk.X, padx=2, pady=2)

        # VIP feature buttons
        for button in [self.vip_balance_button, self.pay_from_account_button, self.topup_button]:
            button.pack_forget()
            button.pack(fill=tk.X, padx=2, pady=2)

        # Logout button
        self.logout_button.pack_forget()
        self.logout_button.pack(fill=tk.X, padx=2, pady=2)

        # Ensure scrollbar remains functional
        self.menu_canvas.configure(height=200)  # Fixed height for menu area

    def apply_tablet_layout(self):
        """Apply tablet layout"""
        # Restore horizontal layout but adjust proportions
        self.root.grid_columnconfigure(0, weight=2)  # Menu takes 2/3
        self.root.grid_columnconfigure(1, weight=1)  # Order takes 1/3

        # Move the order frame back to the side
        self.order_frame.grid_forget()
        self.order_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Adjust category buttons
        for cat_btn in self.category_buttons.values():
            cat_btn.configure(padding=(4, 2))

        # Adjust menu items to use a moderate number of columns
        self.max_menu_cols = 2  # Tablet mode: 2 columns

        # Restore font sizes
        self.menu_label.configure(font=('Arial', 16, 'bold'))
        self.order_label.configure(font=('Arial', 16, 'bold'))
        self.total_label.configure(font=('Arial', 14))

        # Restore input field sizes
        self.table_number.configure(width=5)
        self.person_spinbox.configure(width=5)

        # Adjust VIP-related element sizes
        self.locker_code_label.configure(font=('Arial', 12))
        self.unlock_entry.configure(width=6)

        # Restore drop area size
        self.drop_frame.pack(fill=tk.X, padx=5, pady=5, ipady=10)
        self.drop_label.pack(pady=20)

        # Rearrange buttons - basic order buttons in a horizontal layout
        for button in [self.clear_button, self.checkout_button, self.split_bill_button]:
            button.pack_forget()
        self.clear_button.pack(side=tk.LEFT, padx=3)
        self.checkout_button.pack(side=tk.LEFT, padx=3)
        self.split_bill_button.pack(side=tk.LEFT, padx=3)

        # VIP feature buttons in a horizontal layout
        for button in [self.vip_balance_button, self.pay_from_account_button, self.topup_button]:
            button.pack_forget()
        self.vip_balance_button.pack(side=tk.LEFT, padx=3)
        self.pay_from_account_button.pack(side=tk.LEFT, padx=3)
        self.topup_button.pack(side=tk.LEFT, padx=3)

        # Logout button
        self.logout_button.pack_forget()
        self.logout_button.pack(side=tk.LEFT, padx=3)

        # Adjust canvas to expand appropriately
        self.menu_canvas.configure(height=0)  # Let it expand naturally

    def apply_desktop_layout(self):
        """Apply desktop layout"""
        # Original desktop proportions
        self.root.grid_columnconfigure(0, weight=4)  # Menu takes 4/5
        self.root.grid_columnconfigure(1, weight=1)  # Order takes 1/5

        # Ensure the order frame is in the correct position
        self.order_frame.grid_forget()
        self.order_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Full-size category buttons
        for cat_btn in self.category_buttons.values():
            cat_btn.configure(padding=(5, 3))

        # Use the maximum number of columns for menu items
        self.max_menu_cols = 3  # Desktop: 3 columns

        # Standard font sizes
        self.menu_label.configure(font=('Arial', 16, 'bold'))
        self.order_label.configure(font=('Arial', 16, 'bold'))
        self.total_label.configure(font=('Arial', 14))

        # Standard input field sizes
        self.table_number.configure(width=5)
        self.person_spinbox.configure(width=5)

        # Standard VIP-related element sizes
        self.locker_code_label.configure(font=('Arial', 12))
        self.unlock_entry.configure(width=6)

        # Standard drop area size
        self.drop_frame.pack(fill=tk.X, padx=5, pady=5, ipady=10)
        self.drop_label.pack(pady=20)

        # Standard button layout
        # Basic order buttons
        for button in [self.clear_button, self.checkout_button, self.split_bill_button]:
            button.pack_forget()
        self.clear_button.pack(side=tk.LEFT, padx=5)
        self.checkout_button.pack(side=tk.LEFT, padx=5)
        self.split_bill_button.pack(side=tk.LEFT, padx=5)

        # VIP feature buttons
        for button in [self.vip_balance_button, self.pay_from_account_button, self.topup_button]:
            button.pack_forget()
        self.vip_balance_button.pack(side=tk.LEFT, padx=5)
        self.pay_from_account_button.pack(side=tk.LEFT, padx=5)
        self.topup_button.pack(side=tk.LEFT, padx=5)

        # Logout button
        self.logout_button.pack_forget()
        self.logout_button.pack(side=tk.LEFT, padx=5)

        # Fully expand the menu area
        self.menu_canvas.configure(height=0)

    def rebuild_menu_after_resize(self, category):
        """Rebuild the menu using the current category after window resize"""
        # Save the current category
        old_category = self.selected_category.get()
        
        # Set the category (trigger rebuild if different)
        if category != old_category:
            self.selected_category.set(category)
        else:
            # If the category is the same, manually trigger rebuild
            if hasattr(self, 'on_category_change_callback'):
                self.on_category_change_callback()
    
    def create_menu_items(self, items, categories):
        """Create draggable menu item widgets for better usability and responsive design"""
        # Clear existing widgets
        for widget in self.menu_scrollable_frame.winfo_children():
            widget.destroy()
        
        # Clear existing category buttons
        for widget in self.categories_row1.winfo_children():
            widget.destroy()
        for widget in self.categories_row2.winfo_children():
            widget.destroy()
        
        self.category_buttons = {}
        
        # Add the "All" category to the first row
        all_btn = ttk.Radiobutton(self.categories_row1, text=self.get_text("all"), value="All",
                                variable=self.selected_category)
        all_btn.pack(side=tk.LEFT, padx=5)
        self.category_buttons["All"] = all_btn
        
        # Distribute categories evenly across two rows
        total_categories = len(categories)
        half_categories = total_categories // 2 + (1 if total_categories % 2 != 0 else 0)
        
        # Add the first half of categories to the first row
        for i, category in enumerate(categories[:half_categories]):
            # Use translated category names
            translated_cat = self.model.get_translated_category(category, self.current_lang)
            cat_btn = ttk.Radiobutton(self.categories_row1, text=translated_cat, value=category,
                                    variable=self.selected_category)
            cat_btn.pack(side=tk.LEFT, padx=5)
            self.category_buttons[category] = cat_btn
        
        # Add the second half of categories to the second row
        for category in categories[half_categories:]:
            # Use translated category names
            translated_cat = self.model.get_translated_category(category, self.current_lang)
            cat_btn = ttk.Radiobutton(self.categories_row2, text=translated_cat, value=category,
                                    variable=self.selected_category)
            cat_btn.pack(side=tk.LEFT, padx=5)
            self.category_buttons[category] = cat_btn
        
        # Create menu items
        current_category = self.selected_category.get()

        # Determine the number of columns based on the current layout
        max_cols = getattr(self, 'max_menu_cols', 3)  # Default to 3 if not set

        row = 0
        col = 0
        
        # Filter items by the selected category if not "All"
        display_items = items if current_category == "All" else [item for item in items if item.category == current_category]
        
        # Configure grid with evenly distributed columns
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
            
            # Create an inner frame for better styling
            inner_frame = ttk.Frame(item_frame, padding=3)
            inner_frame.pack(fill=tk.BOTH, expand=True)
            
            # Item name and price - adjust font size based on layout
            name_label = ttk.Label(inner_frame, text=f"{item.name}",
                                 font=('Arial', font_size_name, 'bold'))
            name_label.pack(pady=(3, 0), fill=tk.BOTH, expand=True)
            
            price_label = ttk.Label(inner_frame, text=f"${item.price:.2f}",
                                  font=('Arial', font_size_price))
            price_label.pack(pady=(0, 3), fill=tk.BOTH, expand=True)
            
            # Store a reference to the item in the widget
            item_frame.item = item
            inner_frame.item = item
            name_label.item = item
            price_label.item = item
            
            # Make all elements draggable
            for widget in [item_frame, inner_frame, name_label, price_label]:
                widget.bind("<ButtonPress-1>", lambda e, i=item: self.on_drag_start(e, i))
                widget.bind("<B1-Motion>", self.on_drag_motion)
                widget.bind("<ButtonRelease-1>", self.on_drag_release)
            
            # Store widget references
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
        
        # Create drag-and-drop image
        self.drag_image = tk.Toplevel(self.root)
        self.drag_image.overrideredirect(True)
        self.drag_image.attributes('-topmost', True)
        self.drag_image.attributes('-alpha', 0.7)
        
        # Create a more visible drag-and-drop image
        frame = ttk.Frame(self.drag_image, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Adjust font size of drag-and-drop image based on current layout
        if self.current_layout == "mobile":
            font_size = 10
        else:
            font_size = 11

        label = ttk.Label(frame, text=f"{item.name}\n${item.price:.2f}",
                        background='lightblue', font=('Arial', font_size, 'bold'), padding=10)
        label.pack(fill=tk.BOTH, expand=True)
        
        # Place the drag-and-drop image at the pointer location
        x, y = self.root.winfo_pointerxy()
        self.drag_image.geometry(f"+{x}+{y}")
        
        # Highlight drop zones
        self.highlight_drop_zones(True)

    def on_drag_motion(self, event):
        """Handle drag-and-drop motion"""
        if hasattr(self, 'drag_image'):
            x, y = self.root.winfo_pointerxy()
            self.drag_image.geometry(f"+{x}+{y}")

    def on_drag_release(self, event):
        """Handle drag-and-drop release"""
        if hasattr(self, 'drag_image'):
            # Get current position
            x, y = self.root.winfo_pointerxy()
            
            # Check if released over a drop zone
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
            
            # Check individual tabs (if present)
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
            
            # Destroy drag-and-drop image
            self.drag_image.destroy()
            delattr(self, 'drag_image')
            
            # Remove drop zone highlights
            self.highlight_drop_zones(False)
            
            # If released in a valid zone, trigger item addition
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
            # Highlight individual drop zones (if visible)
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
        """Handle item drop into the order"""
        # This will connect to the controller to add the item
        if hasattr(self, 'on_add_item_callback'):
            self.on_add_item_callback(item, person_idx)

    def set_on_add_item_callback(self, callback):
        """Set callback for adding items to the order"""
        self.on_add_item_callback = callback

    def set_on_remove_item_callback(self, callback):
        """Set callback for removing items"""
        self.on_remove_item_callback = callback

    def set_on_decrease_quantity_callback(self, callback):
        """Set callback for decreasing item quantity"""
        self.on_decrease_quantity_callback = callback

    def update_individual_tabs(self, num_people):
        """Update individual order tabs"""
        # Remove existing individual pages
        for tab in list(self.individual_trees.keys()):
            if tab not in [f"Person {i+1}" for i in range(num_people)]:
                self.order_notebook.forget(self.individual_trees[tab]['frame'])
                del self.individual_trees[tab]
        
        # Add or update individual pages
        for i in range(num_people):
            person_name = f"Person {i+1}"
            translated_name = f"{self.get_text('person')} {i+1}"

            if person_name not in self.individual_trees:
                # Create new page
                person_frame = ttk.Frame(self.order_notebook)
                self.order_notebook.add(person_frame, text=translated_name)
                
                # Create drop zone for this person
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
                
                # Create treeview for this page
                person_tree = ttk.Treeview(person_frame, columns=('Name', 'Quantity', 'Price'), show='headings')
                person_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
                
                person_tree.heading('Name', text=self.get_text("order_table")["name"])
                person_tree.heading('Quantity', text=self.get_text("order_table")["quantity"])
                person_tree.heading('Price', text=self.get_text("order_table")["price"])
                
                # Adjust column widths based on layout
                if self.current_layout == "mobile":
                    person_tree.column('Name', width=80)
                    person_tree.column('Quantity', width=40)
                    person_tree.column('Price', width=60)
                else:
                    person_tree.column('Name', width=150)
                    person_tree.column('Quantity', width=80)
                    person_tree.column('Price', width=100)

                # Save references
                self.individual_trees[person_name] = {
                    'frame': person_frame,
                    'tree': person_tree,
                    'drop_frame': person_drop_frame
                }
                # Bind events
                person_tree.bind("<Button-3>", lambda e, t=person_tree, idx=i: self.show_individual_order_context_menu(e, t, idx))

    def show_individual_order_context_menu(self, event, tree, person_index):
        """Show context menu for individual orders"""
        item_id = tree.identify_row(event.y)
        if item_id:
            tree.selection_set(item_id)

            context_menu = tk.Menu(self.root, tearoff=0)
            context_menu.add_command(
                label=self.get_text("delete_item"),
                command=lambda: self.on_delete_individual_item(item_id, tree, person_index)
            )
            context_menu.add_command(
                label=self.get_text("decrease_quantity"),
                command=lambda: self.on_decrease_individual_quantity(item_id, tree, person_index)
            )

            context_menu.post(event.x_root, event.y_root)

    def on_delete_individual_item(self, item_id, tree, person_index):
        """Delete an item from an individual order"""
        if item_id:
            item_name = tree.item(item_id, 'values')[0]
            # Notify the controller via callback
            if hasattr(self, 'on_remove_item_callback'):
                self.on_remove_item_callback(item_name, person_index)

    def on_decrease_individual_quantity(self, item_id, tree, person_index):
        """Decrease the quantity of an item in an individual order"""
        if item_id:
            # Get item name and current quantity
            values = tree.item(item_id, 'values')
            item_name = values[0]
            current_qty = int(values[1])

            if current_qty > 1:
                # Notify the controller via callback to decrease quantity
                if hasattr(self, 'on_decrease_quantity_callback'):
                    self.on_decrease_quantity_callback(item_name, person_index)
            else:
                # If quantity is 1, directly delete the item
                self.on_delete_individual_item(item_id, tree, person_index)

    def update_order_display(self, order_items, total, split_items=None):
        """Update order display, including total order and individual orders"""
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

        # If split bill information is available, update individual order displays
        if split_items:
            for person_idx, (items, subtotal) in enumerate(split_items):
                person_name = f"Person {person_idx+1}"
                if person_name in self.individual_trees:
                    tree = self.individual_trees[person_name]['tree']
                    # Clear existing items
                    for item in tree.get_children():
                        tree.delete(item)
                    # Add new items
                    for item, quantity in items:
                        tree.insert('', 'end', values=(item.name, quantity, f"${item.price * quantity:.2f}"))
        
        self.total_label.config(text=f"{self.get_text('total')}: ${total:.2f}")

    def show_message(self, message):
        """Display a message dialog"""
        messagebox.showinfo(self.get_text("information"), message)

    def display_split_bills(self, split_bills):
        """Display split bill window"""
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
            
            # Add horizontal scrollbar
            tree_scrollbar_x = ttk.Scrollbar(frame, orient="horizontal", command=bill_tree.xview)
            bill_tree.configure(xscrollcommand=tree_scrollbar_x.set)
            tree_scrollbar_x.pack(fill="x")
            
            bill_tree.heading('Name', text=self.get_text("order_table")["name"])
            bill_tree.heading('Quantity', text=self.get_text("order_table")["quantity"])
            bill_tree.heading('Price', text=self.get_text("order_table")["price"])
            
            # Set column widths based on layout
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
        
        # Add print and close buttons
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
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.root = view.root
        self.current_order = Order()
        self.update_locker_code()
        
        # Set callbacks for adding items via drag-and-drop
        self.view.set_on_add_item_callback(self.add_to_order_drag_drop)
        self.view.set_on_remove_item_callback(self.remove_from_order)
        self.view.set_on_decrease_quantity_callback(self.decrease_item_quantity)

        # Bind events
        self.view.clear_button.config(command=self.clear_order)
        self.view.checkout_button.config(command=self.checkout)
        self.view.split_bill_button.config(command=self.split_bill)
        self.view.add_person_btn.config(command=self.add_person)
        self.view.remove_person_btn.config(command=self.remove_person)
        self.view.selected_category.trace("w", self.on_category_change)
        self.view.vip_balance_button.config(command=self.vip_balance)
        self.view.pay_from_account_button.config(command=self.pay_from_account)
        self.view.unlock_button.config(command=self.unlock_fridge)
        self.view.topup_button.config(command=self.topup_account)
        self.view.logout_button.config(command=self.logout)
     
        # Initialize order
        self.reset_order()
        
        # Initialize menu display
        self.initialize_menu()

        # Update person selection range
        self.update_person_spinbox_range()

        # Set callback for category changes
        self.view.on_category_change_callback = self.on_category_change
    
    def remove_from_order(self, item_name, person_index=None):
        """Remove an item from the order"""
        # Find the corresponding menu item
        menu_items = self.model.get_menu_items()
        target_item = next((item for item in menu_items if item.name == item_name), None)

        if target_item:
            # Remove from the order
            people_count = self.view.people_count.get()

            if people_count > 1 and person_index is not None:
                # Remove from the specified person's order
                self.current_order.remove_item(target_item.id, sub_order_index=person_index)
            else:
                # Remove from the total order
                self.current_order.remove_item(target_item.id)

            # Update display
            self.update_all_displays()

    def decrease_item_quantity(self, item_name, person_index=None):
        """Decrease the quantity of an item in the order"""
        # Find the corresponding menu item
        menu_items = self.model.get_menu_items()
        target_item = next((item for item in menu_items if item.name == item_name), None)

        if target_item:
            # Decrease the quantity in the order (remove 1)
            people_count = self.view.people_count.get()

            if people_count > 1 and person_index is not None:
                # Decrease from the specified person's order
                self.current_order.remove_item(target_item.id, quantity=1, sub_order_index=person_index)
            else:
                # Decrease from the total order
                self.current_order.remove_item(target_item.id, quantity=1)

            # Update the display
            self.update_all_displays()

    def unlock_fridge(self):
        """Verify the combination lock code, update the code if correct"""
        code = self.view.unlock_entry.get()
        vip_account = self.model.vip_account

        if not code.isdigit():
            self.view.show_message(self.view.get_text("enter_valid_code"))
            return

        if self.model.locker.verify_code(int(code)):
            if self.model.vip_account >= 20:
                self.model.vip_account -= 20
                self.view.show_message(self.view.get_text("unlocked").format(self.model.vip_account))
                self.model.locker.update_code()  # Update the code after success
                self.update_locker_code()  # Update the display with the new code
            else:
                self.view.show_message(self.view.get_text("not_enough_balance").format(self.model.vip_account))
        else:
            self.view.show_message(self.view.get_text("wrong_code"))

    def update_locker_code(self):
        """Update the locker code display in the UI"""
        new_code = self.model.locker.lock_code
        self.view.update_locker_code(new_code)

    def initialize_menu(self):
        """Initialize the menu and categories"""
        menu_items = self.model.get_menu_items()
        categories = sorted(set(item.category for item in menu_items))
        self.view.create_menu_items(menu_items, categories)

    def on_category_change(self, *args):
        """Handle category change"""
        self.initialize_menu()

    def reset_order(self):
        # Create a new order instance
        self.current_order = Order()
        # Reset the tab display
        self.view.update_individual_tabs(1)
        # Update all displays
        self.update_all_displays()

    def add_person(self):
        current_count = self.view.people_count.get()
        self.view.people_count.set(current_count + 1)
        self.update_person_spinbox_range()
        if len(self.current_order.sub_orders) < current_count + 1:
            self.current_order.sub_orders.append([])
        # Update the order display tabs
        self.view.update_individual_tabs(current_count + 1)
        # Update all order displays
        self.update_all_displays()

    def remove_person(self):
        current_count = self.view.people_count.get()
        if current_count > 1:
            self.view.people_count.set(current_count - 1)
            self.update_person_spinbox_range()
            if len(self.current_order.sub_orders) > current_count - 1:
                self.current_order.sub_orders.pop()
            # Update the order display tabs
            self.view.update_individual_tabs(current_count - 1)
            # Update all order displays
            self.update_all_displays()

    def update_all_displays(self):
        """Update all order displays"""
        all_items = self.current_order.get_all_items()
        split_bills = self.current_order.get_split_bills()
        self.view.update_order_display(all_items, self.current_order.total, split_bills)        

    def update_person_spinbox_range(self):
        current_count = self.view.people_count.get()
        self.view.person_spinbox.config(from_=1, to=current_count)
        if self.view.current_person.get() > current_count:
            self.view.current_person.set(current_count)

    def add_to_order_drag_drop(self, menu_item, person_index=None):
        """Add an item to the order via drag-and-drop"""
        if menu_item:
            people_count = self.view.people_count.get()
            if people_count > 1 and person_index is not None:
                self.current_order.add_item(menu_item, sub_order_index=person_index)
            else:
                self.current_order.add_item(menu_item)

            self.update_all_displays()
            
    def split_bill(self):
        if self.view.people_count.get() <= 1:
            self.view.show_message(self.view.get_text("not_group_order"))
            return

        split_bills = self.current_order.get_split_bills()
        if not split_bills or all(not items for items, _ in split_bills):
            self.view.show_message(self.view.get_text("no_items_to_split"))
            return

        self.view.display_split_bills(split_bills)

    def clear_order(self):
        self.reset_order()
        self.view.people_count.set(1)  # Reset the number of people
        self.update_person_spinbox_range()

    def checkout(self):
        if not self.current_order.get_all_items():
            self.view.show_message(self.view.get_text("order_is_empty"))
            return

        # Set the table number from the view
        self.current_order.table_number = self.view.table_number.get() if self.view.table_number.get() else None
        
        table_info = f" {self.view.get_text('for_table')} {self.current_order.table_number}" if self.current_order.table_number else ""
        group_info = f" {self.view.get_text('group_order_msg')}" if self.current_order.is_group_order() else ""

        self.view.show_message(f"{self.view.get_text('order_completed')}{table_info}{group_info} {self.view.get_text('total')}: ${self.current_order.total:.2f}")
        self.clear_order()

    def vip_balance(self):
        """Check VIP balance and display it"""
        self.view.show_message(self.view.get_text("your_vip_balance").format(self.model.vip_account))
    
    def pay_from_account(self):
        if not self.current_order.get_all_items():
            self.view.show_message(self.view.get_text("order_is_empty"))
            return

        total_cost = self.current_order.total
        
        if self.model.vip_account >= total_cost:
            self.model.vip_account -= total_cost
            table_info = f" {self.view.get_text('for_table')} {self.current_order.table_number}" if self.current_order.table_number else ""
            group_info = f" {self.view.get_text('group_order_msg')}" if self.current_order.is_group_order() else ""
            
            self.view.show_message(f"{self.view.get_text('order_completed')}{table_info}{group_info} {self.view.get_text('total')}: ${total_cost:.2f}\n{self.view.get_text('your_vip_balance').format(self.model.vip_account)}")
            self.clear_order()
        else:
            self.view.show_message(self.view.get_text("insufficient_balance"))

    def topup_account(self):
        """Top up VIP account"""
        amount = simpledialog.askinteger(
            self.view.get_text("top_up"),
            self.view.get_text("top_up_prompt"),
            minvalue=1
        )
        
        if amount is not None:  # Ensure the user did not click cancel
            self.model.vip_account += amount  # Increase balance
            messagebox.showinfo(
                self.view.get_text("success"),
                self.view.get_text("recharged").format(self.model.vip_account)
            )

    def logout(self):
        """Log out and return to the login interface"""
        confirm = messagebox.askyesno(
            self.view.get_text("logout"),
            self.view.get_text("confirm_logout")
        )
        if confirm:
            self.root.quit()  # End the Tkinter event loop
            self.root.destroy()  # Destroy the Tkinter main window
            subprocess.Popen([sys.executable, "login_interface.py"], start_new_session=True)  # Launch the login window

# main
def main():
    root = tk.Tk()
    # Create a style for highlighting drop zones
    style = ttk.Style()
    style.configure("Highlight.TLabelframe", background="lightblue")

    # Initialize the model, view, and controller
    model = MenuModel()
    view = POSView(root, model)
    controller = POSController(model, view)

    # Set the view's reference to the controller
    view.controller = controller

    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
