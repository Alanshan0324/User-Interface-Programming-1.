# model
import random
import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
import sys
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
            while len(self.sub_orders) <= (sub_order_index or 0):
                self.sub_orders.append([])
            
            self.sub_orders[sub_order_index].append((item, quantity))
        else:
            self.items.append((item, quantity))
        
        self.total += item.price * quantity

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
        return random.randint(1000, 9999)  # 生成 4 位數密碼

    def verify_code(self, code):
        return code == self.lock_code

    def update_code(self):
        self.lock_code = self.generate_code()  # 成功購買後更新密碼
    def unlock(self):
        # 假設你從輸入框中獲取用戶輸入的密碼
        entered_code = int(self.unlock_entry.get())
        if self.verify_code(entered_code):
            print("解鎖成功！")
        else:
            print("密碼錯誤！")


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

            #special menu
            MenuItem(71, "Lobster Bisque", 30.00, "Special Menu"),
            MenuItem(72, "Foie Gras", 35.00, "Special Menu"),
            MenuItem(73, "Black Truffle Risotto", 60.00, "Special Menu"),
            MenuItem(74, "Gold Leaf Dessert", 55.00, "Special Menu"),          
        


        ]
    def get_menu_items(self):
        return self.menu_items

    def get_item_by_id(self, item_id):
        return next((item for item in self.menu_items if item.id == item_id), None)
    
# view
import tkinter as tk
from tkinter import ttk, messagebox

class POSView:
    def __init__(self, root,model):
        
        self.root = root
        self.model = model
        self.current_lang = "English"
        self.root.title("VIP POS System")
        self.root.geometry("1430x600")
        
        # 設定列權重來控制左右兩邊的比例
        root.columnconfigure(0, weight=4)  # 菜單佔 4/5
        root.columnconfigure(1, weight=1)  # 訂單佔 1/5
        root.rowconfigure(0, weight=1)


        
    

        # 創建主框架使用 grid 而非 pack
        self.menu_frame = ttk.Frame(root)
        self.menu_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        self.order_frame = ttk.Frame(root)
        self.order_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.title_frame = ttk.Frame(self.menu_frame)
        self.title_frame.pack(fill=tk.X)
        # 菜單部分
        self.menu_label = ttk.Label(self.title_frame, text=LANGUAGES[self.current_lang]["menu"], 
                                    font=('Arial', 16, 'bold'))
        self.menu_label.pack()

       
        
        # 創建菜單類別框架 (更好的視覺組織)
        self.categories_frame = ttk.Frame(self.menu_frame)
        self.categories_frame.pack(fill=tk.X, pady=5)
        
        # 分為兩行顯示的類別按鈕框架
        self.categories_row1 = ttk.Frame(self.categories_frame)
        self.categories_row1.pack(fill=tk.X)
        
        self.categories_row2 = ttk.Frame(self.categories_frame)
        self.categories_row2.pack(fill=tk.X, pady=(5, 0))
        
        # 類別按鈕
        self.category_buttons = {}
        self.selected_category = tk.StringVar(value="All")
        
        # 菜單項目框架與滾動條
        self.menu_items_frame = ttk.Frame(self.menu_frame)
        self.menu_items_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # 用於滾動的 Canvas
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
        
        # 訂單部分與 notebook
        self.order_label = ttk.Label(self.order_frame, text="Current Order", font=('Arial', 16, 'bold'))
        self.order_label.pack()
        
        self.language_frame = ttk.Frame(self.title_frame)
        self.language_frame.pack()  # Frame 也用 grid


        self.label_choose_language = ttk.Label(self.language_frame, 
                                                text=LANGUAGES[self.current_lang]["choose_language"],
                                                font=("Arial", 10))
        self.label_choose_language.grid(row=0, column=0, padx=(0, 5), sticky="w")

        self.language_var = tk.StringVar(self.root)
        self.language_var.set(self.current_lang)  # 預設語言


        self.language_menu = ttk.OptionMenu(self.language_frame, 
            self.language_var,
            *LANGUAGES.keys(), 
            command=self.change_language)
        self.language_menu.grid(row=0, column=1, padx=5, sticky="e")
        self.update_language_menu()
        
        # 訂單控制項
        order_config_frame = ttk.Frame(self.order_frame)
        order_config_frame.pack(fill=tk.X, pady=5)
        
        self.table_text = ttk.Label(order_config_frame, text=LANGUAGES[self.current_lang]["table_number"]+":")
        self.table_text.pack(side=tk.LEFT, padx=5)
        self.table_number = ttk.Entry(order_config_frame, width=5)
        self.table_number.pack(side=tk.LEFT, padx=5)
        
        # 團體人數控制
        self.group_control_frame = ttk.Frame(order_config_frame)
        self.group_control_frame.pack(side=tk.LEFT, padx=10)
        
        
        self.person_text = ttk.Label(self.group_control_frame, text=LANGUAGES[self.current_lang]["persons"]+":")
        self.person_text.pack(side=tk.LEFT, padx=5)
        self.people_count = tk.IntVar(value=1)
        self.people_count_label = ttk.Label(self.group_control_frame, textvariable=self.people_count)
        self.people_count_label.pack(side=tk.LEFT, padx=5)
        
        self.add_person_btn = ttk.Button(self.group_control_frame, text="+", width=2)
        self.add_person_btn.pack(side=tk.LEFT, padx=2)
        
        self.remove_person_btn = ttk.Button(self.group_control_frame, text="-", width=2)
        self.remove_person_btn.pack(side=tk.LEFT, padx=2)

        # 添加新的人員編號
        self.current_person = tk.IntVar(value=1)
        self.choose_person_text = ttk.Label(self.group_control_frame, text=LANGUAGES[self.current_lang]["choose_person"]+":")
        self.choose_person_text.pack(side=tk.LEFT, padx=5)
        self.person_spinbox = ttk.Spinbox(
            self.group_control_frame, 
            from_=1, 
            to=1, 
            width=5,
            textvariable=self.current_person
        )
        self.person_spinbox.pack(side=tk.LEFT, padx=5)
        
        # 創建 notebook
        self.order_notebook = ttk.Notebook(self.order_frame)
        self.order_notebook.pack(fill=tk.BOTH, expand=True)
        
        # 總訂單頁籤
        self.total_order_frame = ttk.Frame(self.order_notebook)
        self.order_notebook.add(self.total_order_frame, text=LANGUAGES[self.current_lang]["total_order"])
        
        # 創建拖放區域框架
        self.drop_frame = ttk.LabelFrame(self.total_order_frame, text=LANGUAGES[self.current_lang]["drop_items_here"])
        self.drop_frame.pack(fill=tk.X, padx=5, pady=5, ipady=10)
        
        # 拖放區域的標籤
        self.drop_label = ttk.Label(self.drop_frame, text=LANGUAGES[self.current_lang]["drag_hint"], 
                                  font=('Arial', 10), foreground='gray')
        self.drop_label.pack(pady=20)
        
        # 創建總訂單樹狀視圖
        self.order_tree = ttk.Treeview(self.total_order_frame, columns=('Name', 'Quantity', 'Price'), show='headings')
        self.order_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
       
        self.order_tree.heading('Name', text=["name"])
        self.order_tree.heading('Quantity', text=["quantity"])
        self.order_tree.heading('Price', text=["price"])
        
        # 個人訂單框架 (將動態填充)
        self.individual_trees = {}  # 儲存每個人的樹狀視圖
        
        
        # 創建一個 Frame 來容納這四個元件
        self.total_frame = ttk.Frame(self.order_frame)
        self.total_frame.pack(pady=10)

        # 總計標籤
        self.total_label = ttk.Label(self.total_frame, text="Total: $0.00", font=('Arial', 14))
        self.total_label.pack(side="left", padx=10)

        # Locker Code Label（顯示密碼）
        self.locker_code_label = ttk.Label(self.total_frame, text="Locker Code: Hidden", font=('Arial', 12))
        self.locker_code_label.pack(side="left", padx=10)

        # 密碼輸入框
        self.unlock_entry = ttk.Entry(self.total_frame, show="*")
        self.unlock_entry.pack(side="left", padx=10)

        # 解鎖按鈕
        self.unlock_button = ttk.Button(self.total_frame, text="Unlock Fridge")
        self.unlock_button.pack(side="left", padx=10)

       
        # 按鈕
        self.button_frame = ttk.Frame(self.order_frame)
        self.button_frame.pack(fill=tk.X, pady=5)
        
        self.clear_button = ttk.Button(self.button_frame, text="Clear Order")
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        self.checkout_button = ttk.Button(self.button_frame, text="Checkout")
        self.checkout_button.pack(side=tk.LEFT, padx=5)

        self.split_bill_button = ttk.Button(self.button_frame, text="Split Bill")
        self.split_bill_button.pack(side=tk.LEFT, padx=5)

        self.vip_balance_button = ttk.Button(self.button_frame, text=" Show VIP balance")
        self.vip_balance_button.pack(side=tk.LEFT, padx=5)
        
        self.pay_from_account_button = ttk.Button(self.button_frame, text="Pay from account")
        self.pay_from_account_button.pack(side=tk.LEFT, padx=5)

        self.topup_button = ttk.Button(self.button_frame, text="Top up account")
        self.topup_button.pack(side=tk.LEFT, padx=5)

        self.logout_button = ttk.Button(self.button_frame, text=" log out")
        self.logout_button.pack(side=tk.LEFT, padx=5)

        


        
        # 用來儲存菜單項目部件的字典
        self.menu_item_widgets = {}

        # Bind window resize event
        self.root.bind("<Configure>", self.on_window_resize)
    def change_language(self, selected_lang):
        """ 切換語言並更新 UI """
        self.current_lang = selected_lang
        translations = LANGUAGES[self.current_lang]
        for category, button in self.category_buttons.items():
            button.config(text=translations["categories"].get(category, category))

        self.label_choose_language.config(text=translations["choose_language"])
        self.menu_label.config(text=translations["menu"])
        self.order_label.config(text=translations["current_order"])
        self.total_label.config(text=f"{translations['total']}: $0.00")
        self.checkout_button.config(text=translations["checkout"])
        self.clear_button.config(text=translations["clear_order"])
        self.split_bill_button.config(text=translations["split_bill"])
        self.vip_balance_button.config(text=translations["show_vip_balance"])
        self.pay_from_account_button.config(text=translations["pay_from_account"])
        self.topup_button.config(text=translations["top_up"])
        self.logout_button.config(text=translations["logout"])
        self.unlock_button.config(text=translations["unlock"])
        self.table_text.config(text=translations["table_number"])
        self.person_text.config(text=translations["persons"])
        self.choose_person_text.config(text=translations["choose_person"])
        self.order_notebook.tab(0, text=translations["total_order"])
        self.drop_frame.config(text=translations["drop_items_here"])
        self.drop_label.config(text=translations["drag_hint"])
        self.order_tree.heading('Name', text=translations["order_table"]["name"])
        self.order_tree.heading('Quantity', text=translations["order_table"]["quantity"])
        self.order_tree.heading('Price', text=translations["order_table"]["price"])
        self.update_menu_categories()
        self.update_language_menu()
   
    def update_language_menu(self):
        menu = self.language_menu["menu"]
        menu.delete(0, "end")  # 先清除舊選項
        
        for lang in LANGUAGES.keys():
            menu.add_command(label=lang, command=lambda value=lang: self.language_var.set(value) or self.change_language(value))

    def update_menu_categories(self):
        
        translations = LANGUAGES[self.current_lang]["categories"]
        for category, button in self.category_buttons.items():
            button.config(text=translations.get(category, category))


    def update_locker_code(self, code):
        
        print(f"Locker Code: {code}")

    def on_window_resize(self, event):
        """Handle window resize to adjust menu layout"""
        # Only process events from the root window, not child widgets
        if event.widget == self.root:
            # If the window width has significantly changed, re-layout the menu
            # Get current selected category
            current_category = self.selected_category.get()
            
            # Trigger category change to rebuild the menu with the current category
            # We wait a short time to ensure the window resize is complete
            self.root.after(100, lambda: self.rebuild_menu_after_resize(current_category))

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
    
    def create_menu_items(self, items, categories):
        """Create draggable menu item widgets with improved usability"""
        # Clear existing widgets
        for widget in self.menu_scrollable_frame.winfo_children():
            widget.destroy()
        
        # Clear existing category buttons if any
        for widget in self.categories_row1.winfo_children():
            widget.destroy()
        for widget in self.categories_row2.winfo_children():
            widget.destroy()
        
        self.category_buttons = {}
        
        # Add "All" category first in row 1
        all_btn = ttk.Radiobutton(self.categories_row1, text="All", value="All", 
                                variable=self.selected_category)
        all_btn.pack(side=tk.LEFT, padx=5)
        self.category_buttons["All"] = all_btn
        
        # Split categories evenly between two rows
        total_categories = len(categories)
        half_categories = total_categories // 2 + (1 if total_categories % 2 != 0 else 0)
        
        # Add first half of categories to row 1
        for i, category in enumerate(categories[:half_categories]):
            cat_btn = ttk.Radiobutton(self.categories_row1, text=category, value=category, 
                                    variable=self.selected_category)
            cat_btn.pack(side=tk.LEFT, padx=5)
            self.category_buttons[category] = cat_btn
        
        # Add second half of categories to row 2
        for category in categories[half_categories:]:
            cat_btn = ttk.Radiobutton(self.categories_row2, text=category, value=category, 
                                    variable=self.selected_category)
            cat_btn.pack(side=tk.LEFT, padx=5)
            self.category_buttons[category] = cat_btn
        
        # Create menu items
        current_category = self.selected_category.get()
        row = 0
        col = 0
        max_cols = 3  # Number of items per row
        
        # Filter items by selected category if not "All"
        display_items = items if current_category == "All" else [item for item in items if item.category == current_category]
        
        for item in display_items:
            if col >= max_cols:
                col = 0
                row += 1
                
            # Create a frame for each menu item
            item_frame = ttk.Frame(self.menu_scrollable_frame, relief="raised", borderwidth=2)
            item_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            
            # Set minimum size to make buttons larger
            item_frame.columnconfigure(0, minsize=120)
            item_frame.rowconfigure(0, minsize=80)
            
            # Create a container inside the frame for better styling
            inner_frame = ttk.Frame(item_frame, padding=5)
            inner_frame.pack(fill=tk.BOTH, expand=True)
            
            # Item name with the price
            name_label = ttk.Label(inner_frame, text=f"{item.name}", font=('Arial', 12, 'bold'))
            name_label.pack(pady=(5, 0), fill=tk.BOTH, expand=True)
            
            price_label = ttk.Label(inner_frame, text=f"${item.price:.2f}", font=('Arial', 10))
            price_label.pack(pady=(0, 5), fill=tk.BOTH, expand=True)
            
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
        
        label = ttk.Label(frame, text=f"{item.name}\n${item.price:.2f}",
                        background='lightblue', font=('Arial', 11, 'bold'), padding=10)
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
            if person_name not in self.individual_trees:
                # Create a new page
                person_frame = ttk.Frame(self.order_notebook)
                self.order_notebook.add(person_frame, text=person_name)
                
                # Create a drop zone for this person
                person_drop_frame = ttk.LabelFrame(person_frame, text=f"Drop Items Here for {person_name}")
                person_drop_frame.pack(fill=tk.X, padx=5, pady=5, ipady=10)
                
                person_drop_label = ttk.Label(person_drop_frame, text=f"Drag menu items here to add to {person_name}'s order",
                                           font=('Arial', 10), foreground='gray')
                person_drop_label.pack(pady=20)
                
                # Create the treeview for this page
                person_tree = ttk.Treeview(person_frame, columns=('Name', 'Quantity', 'Price'), show='headings')
                person_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
                
                person_tree.heading('Name', text='Name')
                person_tree.heading('Quantity', text='Quantity')
                person_tree.heading('Price', text='Price')
                
                # Save reference
                self.individual_trees[person_name] = {
                    'frame': person_frame,
                    'tree': person_tree,
                    'drop_frame': person_drop_frame
                }

    def update_order_display(self, order_items, total, split_items=None):
        """Update order display, including total orders and individual orders"""
        # Update total order display
        for item in self.order_tree.get_children():
            self.order_tree.delete(item)
        for item, quantity in order_items:
            self.order_tree.insert('', 'end', values=(item.name, quantity, f"${item.price * quantity:.2f}"))
        
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
        
        self.total_label.config(text=f"Total: ${total:.2f}")

    def show_message(self, message):
        messagebox.showinfo("Information", message)

    def display_split_bills(self, split_bills):
        split_bill_window = tk.Toplevel(self.root)
        split_bill_window.title("Split Bills")
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
            frame = ttk.LabelFrame(scrollable_frame, text=f"Person {i}")
            frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
            
            if not items:  # Check if there are items
                ttk.Label(frame, text="No items").pack(pady=10)
                ttk.Label(frame, text=f"Subtotal: $0.00", font=('Arial', 12, 'bold')).pack(anchor=tk.E, padx=10, pady=5)
                continue
            
            bill_tree = ttk.Treeview(frame, columns=('Name', 'Quantity', 'Price'), show='headings', height=5)
            bill_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
            
            # Add a horizontal scroll bar
            tree_scrollbar_x = ttk.Scrollbar(frame, orient="horizontal", command=bill_tree.xview)
            bill_tree.configure(xscrollcommand=tree_scrollbar_x.set)
            tree_scrollbar_x.pack(fill="x")
            
            bill_tree.heading('Name', text='Name')
            bill_tree.heading('Quantity', text='Quantity')
            bill_tree.heading('Price', text='Price')
            
            # Set column width
            bill_tree.column('Name', width=150, minwidth=100)
            bill_tree.column('Quantity', width=80, minwidth=60)
            bill_tree.column('Price', width=100, minwidth=80)
            
            for item, quantity in items:
                bill_tree.insert('', 'end', values=(item.name, quantity, f"${item.price * quantity:.2f}"))
                
            ttk.Label(frame, text=f"Subtotal: ${subtotal:.2f}", font=('Arial', 12, 'bold')).pack(anchor=tk.E, padx=10, pady=5)
        
        # Add Print and Close buttons
        button_frame = ttk.Frame(scrollable_frame)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(button_frame, text="Print Bills", command=lambda: self.show_message("Printing bills...")).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Close", command=split_bill_window.destroy).pack(side=tk.RIGHT, padx=5)


# controller
class POSController:
    def __init__(self, model, view):
        
        self.model = model
        self.view = view
        self.root = view.root
        self.current_order = Order()
        self.update_locker_code()
        
        
        # Set callback for adding items through drag and drop
        self.view.set_on_add_item_callback(self.add_to_order_drag_drop)

        # Bind Events
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
        
        # Initialize menu display with categories
        self.initialize_menu()

        # Update the number of people to select
        self.update_person_spinbox_range()

        # Set the callback for category change
        self.view.on_category_change_callback = self.on_category_change
    

    def unlock_fridge(self):
        """驗證組合鎖密碼，正確則更新密碼"""
        code = self.view.unlock_entry.get()
        vip_account = self.model.vip_account

        if not code.isdigit():
            self.view.show_message("Please enter a valid 4-digit code.")
            return

        if self.model.locker.verify_code(int(code)):
           
        
            if self.model.vip_account >= 20:
                self.model.vip_account -= 20
                self.view.show_message(f"Unlocked! Enjoy your drink. Remaining balance: {self.model.vip_account} USD")
                self.model.locker.update_code()  # 成功後變更密碼
                self.update_locker_code()  # 更新顯示的新密碼
            else:
                self.view.show_message(f"Not enough balance! Remaining balance: {self.model.vip_account} USD. Please add more.")
        else:
            self.view.show_message("Wrong code! Try again.")
    def update_locker_code(self):
        """更新 UI 上的密碼顯示"""
        new_code = self.model.locker.lock_code
        self.view.update_locker_code(new_code)


    def initialize_menu(self):
        """Initialize menu with categories"""
        menu_items = self.model.get_menu_items()
        categories = sorted(set(item.category for item in menu_items))
        self.view.create_menu_items(menu_items, categories)

    def on_category_change(self, *args):
        """Handle category change"""
        self.initialize_menu()

    def reset_order(self):
        # Create a new order instance
        self.current_order = Order()
        # Reset paging display
        self.view.update_individual_tabs(1)
        # Update All Displays
        self.update_all_displays()

    def add_person(self):
        current_count = self.view.people_count.get()
        self.view.people_count.set(current_count + 1)
        self.update_person_spinbox_range()
        if len(self.current_order.sub_orders) < current_count + 1:
            self.current_order.sub_orders.append([])
        # Update order display paging
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
            # Update order display paging
            self.view.update_individual_tabs(current_count - 1)
            # Update all order display
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
        """Add item to order from drag and drop"""
        if menu_item:
            people_count = self.view.people_count.get()
            if people_count > 1 and person_index is not None:
                self.current_order.add_item(menu_item, sub_order_index=person_index)
            else:
                self.current_order.add_item(menu_item)

            self.update_all_displays()
            
    def split_bill(self):
        if self.view.people_count.get() <= 1:
            self.view.show_message("This is not a group order.")
            return

        split_bills = self.current_order.get_split_bills()
        if not split_bills or all(not items for items, _ in split_bills):
            self.view.show_message("No items to split")
            return

        self.view.display_split_bills(split_bills)

    def clear_order(self):
        self.reset_order()
        self.view.people_count.set(1)  # reset people count
        self.update_person_spinbox_range()

    def checkout(self):
        if not self.current_order.get_all_items():
            self.view.show_message("The order is empty")
            return

        # Set table number from view
        self.current_order.table_number = self.view.table_number.get() if self.view.table_number.get() else None
        
        table_info = f" for table {self.current_order.table_number}" if self.current_order.table_number else ""
        group_info = " (Group order)" if self.current_order.is_group_order() else ""

        self.view.show_message(f"Order{table_info}{group_info} completed! Total: ${self.current_order.total:.2f}")
        self.clear_order()
    def vip_balance(self):
        """檢查 VIP 餘額並顯示"""
        
        self.view.show_message(f"Your VIP balance is: ${self.model.vip_account:.2f}")
    
    def pay_from_account(self):
        if not self.current_order.get_all_items():
            self.view.show_message("The order is empty")
            return

        total_cost = sum(item.price * qty for item, qty in self.current_order.get_all_items())
        
        if self.model.vip_account >= total_cost:
            self.model.vip_account -= total_cost
            table_info = f" for table {self.current_order.table_number}" if self.current_order.table_number else ""
            group_info = " (Group order)" if self.current_order.is_group_order() else ""
            
            self.view.show_message(f"Order{table_info}{group_info} completed! Total: ${total_cost:.2f}Remaining VIP balance: ${self.model.vip_account:.2f}")
            self.clear_order()
        else:
            self.view.show_message("Insufficient VIP balance!")
    def topup_account(self):

        amount = simpledialog.askinteger("Top-up", "Enter amount to top-up:", minvalue=1)
        
        if amount is not None:  # 確保用戶沒有點擊取消
            self.model.vip_account += amount  # 增加餘額
           
            messagebox.showinfo("Success", f"Recharged!\n New Balance: {self.model.vip_account} USD")
    def logout(self):
        """登出並回到登入介面"""
        confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if confirm:
            
   
            self.root.quit()  # 結束 Tkinter 事件循環
            self.root.destroy()  # 銷毀 Tkinter 主視窗
            subprocess.Popen([sys.executable, "login_interface.py"], start_new_session=True)  # 啟動新視窗
   

   

# main
def main():
    root = tk.Tk()
    
    # Create a style for highlighted drop zones
    style = ttk.Style()
    style.configure("Highlight.TLabelframe", background="lightblue")
    
    model = MenuModel()
    view = POSView(root,model)
    controller = POSController(model, view)
    view.controller = controller
    root.mainloop()

if __name__ == "__main__":
    main()
