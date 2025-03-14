# model
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
            # 檢查子訂單索引是否有效
            if sub_order_index >= len(self.sub_orders):
                return False
                
            # 在子訂單中尋找該項目
            for i, (item, item_qty) in enumerate(self.sub_orders[sub_order_index]):
                if item.id == item_id:
                    # 如果要刪除的數量小於項目數量，則減少數量
                    if quantity < item_qty:
                        self.sub_orders[sub_order_index][i] = (item, item_qty - quantity)
                        self.total -= item.price * quantity
                    # 否則刪除整個項目
                    else:
                        actual_qty = item_qty  # 實際刪除的數量不超過現有數量
                        self.sub_orders[sub_order_index].pop(i)
                        self.total -= item.price * actual_qty
                    return True
        else:
            # 在普通訂單中尋找該項目
            for i, (item, item_qty) in enumerate(self.items):
                if item.id == item_id:
                    # 如果要刪除的數量小於項目數量，則減少數量
                    if quantity < item_qty:
                        self.items[i] = (item, item_qty - quantity)
                        self.total -= item.price * quantity
                    # 否則刪除整個項目
                    else:
                        actual_qty = item_qty  # 實際刪除的數量不超過現有數量
                        self.items.pop(i)
                        self.total -= item.price * actual_qty
                    return True
        
        return False  # 找不到項目

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
        self.current_language = "English"  # 預設語言
        
        # 多語言翻譯字典
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
                "all": "Alla",
                "choose_person": "Välj Person"
            }
        }
    
    def get_languages(self):
        """獲取可用的語言列表"""
        return self.languages
    
    def set_language(self, language):
        """設置當前語言"""
        if language in self.languages:
            self.current_language = language
            return True
        return False
    
    def get_current_language(self):
        """獲取當前語言"""
        return self.current_language
    
    def get_text(self, key):
        """獲取當前語言的文本"""
        return self.translations.get(self.current_language, {}).get(key, key)


class MenuModel:
    def __init__(self):
        # 翻譯後的類別名稱
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
        """獲取翻譯後的類別名稱"""
        return self.category_translations.get(category, {}).get(language, category)

# view
import tkinter as tk
from tkinter import ttk, messagebox

class POSView:
    def __init__(self, root, language_model):
        self.root = root
        self.root.title("Bar POS System")
        self.root.geometry("1430x600")
        
        # 儲存語言模型
        self.language_model = language_model
        
        # 設定列權重來控制左右兩邊的比例
        root.columnconfigure(0, weight=4)  # 菜單佔 4/5
        root.columnconfigure(1, weight=1)  # 訂單佔 1/5
        root.rowconfigure(0, weight=1)
        
        # 添加語言選擇框架
        self.language_frame = ttk.Frame(root)
        self.language_frame.grid(row=0, column=0, sticky="nw", padx=5, pady=5)
        
        ttk.Label(self.language_frame, text=self.get_text("language_selection"), 
                 font=('Arial', 10)).pack(side=tk.LEFT, padx=(0, 5))
        
        # 創建語言選擇下拉框
        self.language_var = tk.StringVar(value=self.language_model.get_current_language())
        self.language_combobox = ttk.Combobox(self.language_frame, 
                                             textvariable=self.language_var,
                                             values=self.language_model.get_languages(),
                                             state="readonly",
                                             width=15)
        self.language_combobox.pack(side=tk.LEFT)
        self.language_combobox.bind("<<ComboboxSelected>>", self.on_language_change)
        
        # 創建主框架使用 grid 而非 pack
        self.menu_frame = ttk.Frame(root)
        self.menu_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=(40, 5))  # 調整頂部間距
        
        self.order_frame = ttk.Frame(root)
        self.order_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        # 菜單部分
        self.menu_label = ttk.Label(self.menu_frame, text="Menu", font=('Arial', 16, 'bold'))
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
        self.order_title_label = ttk.Label(self.order_frame, text=self.get_text("order"), font=('Arial', 16, 'bold'))
        self.order_title_label.pack()
        
        # 訂單控制項
        order_config_frame = ttk.Frame(self.order_frame)
        order_config_frame.pack(fill=tk.X, pady=5)
        
        self.table_number_label = ttk.Label(order_config_frame, text=f"{self.get_text('table_number')}:")
        self.table_number_label.pack(side=tk.LEFT, padx=5)
        self.table_number = ttk.Entry(order_config_frame, width=5)
        self.table_number.pack(side=tk.LEFT, padx=5)
        
        # 團體人數控制
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

        # 添加新的人員編號
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
        
        # 創建 notebook
        self.order_notebook = ttk.Notebook(self.order_frame)
        self.order_notebook.pack(fill=tk.BOTH, expand=True)
        
        # 總訂單頁籤
        self.total_order_frame = ttk.Frame(self.order_notebook)
        self.order_notebook.add(self.total_order_frame, text=self.get_text("total"))
        
        # 創建拖放區域框架
        self.drop_frame = ttk.LabelFrame(self.total_order_frame, text=self.get_text("drop_items_here"))
        self.drop_frame.pack(fill=tk.X, padx=5, pady=5, ipady=10)
        
        # 拖放區域的標籤
        self.drop_label = ttk.Label(self.drop_frame, 
                                  text=self.get_text("drag_hint"), 
                                  font=('Arial', 10), foreground='gray')
        self.drop_label.pack(pady=20)
        
        # 創建總訂單樹狀視圖
        self.order_tree = ttk.Treeview(self.total_order_frame, columns=('Name', 'Quantity', 'Price'), show='headings')
        self.order_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.order_tree.heading('Name', text=self.get_text("name"))
        self.order_tree.heading('Quantity', text=self.get_text("quantity"))
        self.order_tree.heading('Price', text=self.get_text("price"))
        
        # 個人訂單框架 (將動態填充)
        self.individual_trees = {}  # 儲存每個人的樹狀視圖
        
        # 總計標籤
        self.total_label = ttk.Label(self.order_frame, text=f"{self.get_text('total')}: $0.00", font=('Arial', 14))
        self.total_label.pack(pady=10)
        
        # 按鈕
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
        
        # 用來儲存菜單項目部件的字典
        self.menu_item_widgets = {}

        # Bind window resize event
        self.root.bind("<Configure>", self.on_window_resize)

        self.order_tree.bind("<<TreeviewSelect>>", self.on_order_item_selected)
    
    def get_text(self, key):
        """獲取當前語言的文本"""
        return self.language_model.get_text(key)
    
    def on_language_change(self, event):
        """當語言選擇變更時"""
        selected_language = self.language_var.get()
        if self.language_model.set_language(selected_language):
            # 更新所有介面文字
            self.update_interface_text()
            
            # 通知控制器語言已變更
            if hasattr(self, 'on_language_change_callback'):
                self.on_language_change_callback()
    
    def set_on_language_change_callback(self, callback):
        """設置語言變更的回調函數"""
        self.on_language_change_callback = callback
    
    def update_interface_text(self):
        """更新所有介面文字為當前語言"""
        # 更新頂部菜單
        self.menu_label.config(text=self.get_text("menu"))
        
        # 更新訂單部分
        self.order_title_label.config(text=self.get_text("order"))
        self.table_number_label.config(text=f"{self.get_text('table_number')}:")
        self.persons_label.config(text=f"{self.get_text('persons')}:")
        self.choose_person_label.config(text=f"{self.get_text('choose_person')}:")
        
        # 更新拖放區域
        self.drop_frame.config(text=self.get_text("drop_items_here"))
        self.drop_label.config(text=self.get_text("drag_hint"))
        
        # 更新訂單樹狀視圖
        self.order_tree.heading('Name', text=self.get_text("name"))
        self.order_tree.heading('Quantity', text=self.get_text("quantity"))
        self.order_tree.heading('Price', text=self.get_text("price"))
        
        # 更新訂單頁籤
        self.order_notebook.tab(0, text=self.get_text("total_order"))
        
        # 更新個人訂單頁籤
        for i, (person_name, person_data) in enumerate(self.individual_trees.items()):
            translated_name = f"{self.get_text('person')} {i+1}"
            self.order_notebook.tab(person_data['frame'], text=translated_name)
            if 'drop_frame' in person_data:
                person_data['drop_frame'].config(text=f"{self.get_text('drop_items_here')} - {translated_name}")
            
            # 更新個人樹狀視圖
            person_data['tree'].heading('Name', text=self.get_text("name"))
            person_data['tree'].heading('Quantity', text=self.get_text("quantity"))
            person_data['tree'].heading('Price', text=self.get_text("price"))
        
        # 更新按鈕
        self.clear_button.config(text=self.get_text("clear"))
        self.checkout_button.config(text=self.get_text("checkout"))
        self.split_bill_button.config(text=self.get_text("split_bill"))
        self.delete_button.config(text=self.get_text("delete_item"))
        
        # 更新總計標籤
        total_value = self.total_label.cget("text").split("$")[1]
        self.total_label.config(text=f"{self.get_text('total')}: ${total_value}")
        
        # 更新類別按鈕（根據菜單模型翻譯類別名稱）
        if hasattr(self, 'menu_model') and hasattr(self, 'on_category_change_callback'):
            self.update_category_buttons()
            self.on_category_change_callback()

    def on_order_item_selected(self, event):
        """當訂單項目被選中時處理"""
        # 這個方法可以用來日後添加更多功能，比如顯示項目詳情等
        pass

    def set_on_delete_button_callback(self, callback):
        """設置刪除按鈕的回調"""
        self.delete_button.config(command=callback)

    def on_delete_button_clicked(self):
        """處理刪除按鈕點擊事件"""
        # 獲取當前標籤頁
        current_tab = self.order_notebook.select()
        
        # 檢查當前是總訂單還是個人訂單
        if current_tab == str(self.total_order_frame):
            # 總訂單頁面
            selection = self.order_tree.selection()
            if selection:
                item_id = selection[0]
                item_name = self.order_tree.item(item_id, 'values')[0]
                if hasattr(self, 'on_remove_item_callback'):
                    self.on_remove_item_callback(item_name)
        else:
            # 個人訂單頁面
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
        """設置菜單模型以便翻譯類別"""
        self.menu_model = menu_model

    def show_order_context_menu(self, event):
        """顯示訂單項目的右鍵選單"""
        # 獲取點擊的項目
        item_id = self.order_tree.identify_row(event.y)
        if item_id:
            # 選中被點擊的項目
            self.order_tree.selection_set(item_id)
            
            # 創建右鍵選單
            context_menu = tk.Menu(self.root, tearoff=0)
            context_menu.add_command(label=self.get_text("delete_item"), 
                                command=lambda: self.on_delete_item(item_id))
            context_menu.add_command(label=self.get_text("decrease_quantity"), 
                                command=lambda: self.on_decrease_quantity(item_id))
            
            # 顯示選單
            context_menu.post(event.x_root, event.y_root)

    def on_delete_item(self, item_id):
        """刪除訂單中的項目"""
        if item_id:
            # 獲取項目名稱
            item_name = self.order_tree.item(item_id, 'values')[0]
            
            # 通過回調通知控制器
            if hasattr(self, 'on_remove_item_callback'):
                # 從當前顯示的標籤頁決定是刪除總訂單還是個人訂單
                current_tab = self.order_notebook.select()
                
                if current_tab == str(self.total_order_frame):
                    # 總訂單頁面
                    self.on_remove_item_callback(item_name)
                else:
                    # 個人訂單頁面
                    for idx, (tab_name, tab_data) in enumerate(self.individual_trees.items()):
                        if current_tab == str(tab_data['frame']):
                            self.on_remove_item_callback(item_name, idx)
                            break

    def on_decrease_quantity(self, item_id):
        """減少項目數量"""
        if item_id:
            # 獲取項目名稱和當前數量
            values = self.order_tree.item(item_id, 'values')
            item_name = values[0]
            current_qty = int(values[1])
            
            if current_qty > 1:
                # 通過回調通知控制器減少數量
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
                # 如果數量是1，則直接刪除
                self.on_delete_item(item_id)

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
    
    def update_category_buttons(self):
        """更新類別按鈕的文字"""
        current_language = self.language_model.get_current_language()
        if hasattr(self, 'menu_model'):
            for category, button in self.category_buttons.items():
                if category == "All":
                    button.config(text=self.get_text("all"))
                else:
                    translated_cat = self.menu_model.get_translated_category(category, current_language)
                    button.config(text=translated_cat)
    
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
            # 使用翻譯後的類別名稱
            translated_cat = self.menu_model.get_translated_category(category, current_language) if hasattr(self, 'menu_model') else category
            cat_btn = ttk.Radiobutton(self.categories_row1, text=translated_cat, value=category, 
                                    variable=self.selected_category)
            cat_btn.pack(side=tk.LEFT, padx=5)
            self.category_buttons[category] = cat_btn
        
        # Add second half of categories to row 2
        for category in categories[half_categories:]:
            # 使用翻譯後的類別名稱
            translated_cat = self.menu_model.get_translated_category(category, current_language) if hasattr(self, 'menu_model') else category
            cat_btn = ttk.Radiobutton(self.categories_row2, text=translated_cat, value=category, 
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
            translated_name = f"{self.get_text('person')} {i+1}"
            
            if person_name not in self.individual_trees:
                # Create a new page
                person_frame = ttk.Frame(self.order_notebook)
                self.order_notebook.add(person_frame, text=translated_name)
                
                # Create a drop zone for this person
                person_drop_frame = ttk.LabelFrame(person_frame, 
                                                 text=f"{self.get_text('drop_items_here')} - {translated_name}")
                person_drop_frame.pack(fill=tk.X, padx=5, pady=5, ipady=10)
                
                person_drop_label = ttk.Label(person_drop_frame, 
                                           text=f"{self.get_text('drag_hint')} - {translated_name}",
                                           font=('Arial', 10), foreground='gray')
                person_drop_label.pack(pady=20)
                
                # Create the treeview for this page
                person_tree = ttk.Treeview(person_frame, columns=('Name', 'Quantity', 'Price'), show='headings')
                person_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
                
                person_tree.heading('Name', text=self.get_text("name"))
                person_tree.heading('Quantity', text=self.get_text("quantity"))
                person_tree.heading('Price', text=self.get_text("price"))
                
                # Save reference
                self.individual_trees[person_name] = {
                    'frame': person_frame,
                    'tree': person_tree,
                    'drop_frame': person_drop_frame
                }
                # 在 update_individual_tabs 方法中，創建 person_tree 後添加
                person_tree.bind("<<TreeviewSelect>>", self.on_order_item_selected)

    def show_individual_order_context_menu(self, event, tree, person_index):
        """顯示個人訂單項目的右鍵選單"""
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
        """設置刪除項目的回調"""
        self.on_remove_item_callback = callback

    def set_on_decrease_quantity_callback(self, callback):
        """設置減少數量的回調"""
        self.on_decrease_quantity_callback = callback

    def on_delete_individual_item(self, item_id, tree, person_index):
        """從個人訂單中刪除項目"""
        if item_id:
            # 獲取項目名稱
            item_name = tree.item(item_id, 'values')[0]
            
            # 通過回調通知控制器
            if hasattr(self, 'on_remove_item_callback'):
                self.on_remove_item_callback(item_name, person_index)

    def on_decrease_individual_quantity(self, item_id, tree, person_index):
        """減少個人訂單中的項目數量"""
        if item_id:
            # 獲取項目名稱和當前數量
            values = tree.item(item_id, 'values')
            item_name = values[0]
            current_qty = int(values[1])
            
            if current_qty > 1:
                # 通過回調通知控制器減少數量
                if hasattr(self, 'on_decrease_quantity_callback'):
                    self.on_decrease_quantity_callback(item_name, person_index)
            else:
                # 如果數量是1，則直接刪除
                self.on_delete_individual_item(item_id, tree, person_index)

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
        
        self.total_label.config(text=f"{self.get_text('total')}: ${total:.2f}")

    def show_message(self, message):
        messagebox.showinfo(self.get_text("information"), message)

    def display_split_bills(self, split_bills):
        split_bill_window = tk.Toplevel(self.root)
        split_bill_window.title(self.get_text("split_bill"))
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
                ttk.Label(frame, text=f"{self.get_text('subtotal')}: $0.00", font=('Arial', 12, 'bold')).pack(anchor=tk.E, padx=10, pady=5)
                continue
            
            bill_tree = ttk.Treeview(frame, columns=('Name', 'Quantity', 'Price'), show='headings', height=5)
            bill_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
            
            # Add a horizontal scroll bar
            tree_scrollbar_x = ttk.Scrollbar(frame, orient="horizontal", command=bill_tree.xview)
            bill_tree.configure(xscrollcommand=tree_scrollbar_x.set)
            tree_scrollbar_x.pack(fill="x")
            
            bill_tree.heading('Name', text=self.get_text("name"))
            bill_tree.heading('Quantity', text=self.get_text("quantity"))
            bill_tree.heading('Price', text=self.get_text("price"))
            
            # Set column width
            bill_tree.column('Name', width=150, minwidth=100)
            bill_tree.column('Quantity', width=80, minwidth=60)
            bill_tree.column('Price', width=100, minwidth=80)
            
            for item, quantity in items:
                bill_tree.insert('', 'end', values=(item.name, quantity, f"${item.price * quantity:.2f}"))
                
            ttk.Label(frame, text=f"{self.get_text('subtotal')}: ${subtotal:.2f}", font=('Arial', 12, 'bold')).pack(anchor=tk.E, padx=10, pady=5)
        
        # Add Print and Close buttons
        button_frame = ttk.Frame(scrollable_frame)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(button_frame, text=self.get_text("print_bills"), 
                 command=lambda: self.show_message(self.get_text("printing_bills"))).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text=self.get_text("close"), 
                 command=split_bill_window.destroy).pack(side=tk.RIGHT, padx=5)

# controller
class POSController:
    def __init__(self, menu_model, view, language_model):
        self.menu_model = menu_model
        self.view = view
        self.language_model = language_model
        self.current_order = Order()

        # 設置語言模型到視圖
        self.view.set_menu_model(self.menu_model)
        
        # 設置語言變更回調
        self.view.set_on_language_change_callback(self.on_language_change)

        # 設置回調
        self.view.set_on_add_item_callback(self.add_to_order_drag_drop)
        self.view.set_on_delete_button_callback(self.view.on_delete_button_clicked)
        self.view.set_on_remove_item_callback(self.remove_from_order)
        self.view.set_on_decrease_quantity_callback(self.decrease_item_quantity)

        # 綁定事件
        self.view.clear_button.config(command=self.clear_order)
        self.view.checkout_button.config(command=self.checkout)
        self.view.split_bill_button.config(command=self.split_bill)
        self.view.add_person_btn.config(command=self.add_person)
        self.view.remove_person_btn.config(command=self.remove_person)
        self.view.selected_category.trace("w", self.on_category_change)

        # 設置類別變更回調
        self.view.on_category_change_callback = self.on_category_change

        # 初始化訂單
        self.reset_order()
        
        # 初始化菜單顯示
        self.initialize_menu()

        # 更新人數選擇範圍
        self.update_person_spinbox_range()

    def on_language_change(self):
        """處理語言變更"""
        # 更新菜單顯示（類別翻譯）
        self.initialize_menu()
        # 更新訂單顯示
        self.update_all_displays()

    def remove_from_order(self, item_name, person_index=None):
        """從訂單中移除項目"""
        # 找到對應的菜單項目
        menu_items = self.menu_model.get_menu_items()
        target_item = next((item for item in menu_items if item.name == item_name), None)
        
        if target_item:
            # 從訂單中刪除
            people_count = self.view.people_count.get()
            
            if people_count > 1 and person_index is not None:
                # 從指定人的訂單中刪除
                self.current_order.remove_item(target_item.id, sub_order_index=person_index)
            else:
                # 從總訂單中刪除
                self.current_order.remove_item(target_item.id)
                
            # 更新顯示
            self.update_all_displays()

    def decrease_item_quantity(self, item_name, person_index=None):
        """減少項目數量"""
        # 找到對應的菜單項目
        menu_items = self.menu_model.get_menu_items()
        target_item = next((item for item in menu_items if item.name == item_name), None)
        
        if target_item:
            # 從訂單中減少數量（刪除1個）
            people_count = self.view.people_count.get()
            
            if people_count > 1 and person_index is not None:
                # 從指定人的訂單中減少
                self.current_order.remove_item(target_item.id, quantity=1, sub_order_index=person_index)
            else:
                # 從總訂單中減少
                self.current_order.remove_item(target_item.id, quantity=1)
                
            # 更新顯示
            self.update_all_displays()

    def initialize_menu(self):
        """初始化菜單及類別"""
        menu_items = self.menu_model.get_menu_items()
        categories = sorted(set(item.category for item in menu_items))
        self.view.create_menu_items(menu_items, categories)

    def on_category_change(self, *args):
        """處理類別變更"""
        self.initialize_menu()

    def reset_order(self):
        # 創建新的訂單實例
        self.current_order = Order()
        # 重置分頁顯示
        self.view.update_individual_tabs(1)
        # 更新所有顯示
        self.update_all_displays()

    def add_person(self):
        current_count = self.view.people_count.get()
        self.view.people_count.set(current_count + 1)
        self.update_person_spinbox_range()
        if len(self.current_order.sub_orders) < current_count + 1:
            self.current_order.sub_orders.append([])
        # 更新訂單分頁顯示
        self.view.update_individual_tabs(current_count + 1)
        # 更新所有訂單顯示
        self.update_all_displays()

    def remove_person(self):
        current_count = self.view.people_count.get()
        if current_count > 1:
            self.view.people_count.set(current_count - 1)
            self.update_person_spinbox_range()
            if len(self.current_order.sub_orders) > current_count - 1:
                self.current_order.sub_orders.pop()
            # 更新訂單分頁顯示
            self.view.update_individual_tabs(current_count - 1)
            # 更新所有訂單顯示
            self.update_all_displays()

    def update_all_displays(self):
        """更新所有訂單顯示"""
        all_items = self.current_order.get_all_items()
        split_bills = self.current_order.get_split_bills()
        self.view.update_order_display(all_items, self.current_order.total, split_bills)        

    def update_person_spinbox_range(self):
        current_count = self.view.people_count.get()
        self.view.person_spinbox.config(from_=1, to=current_count)
        if self.view.current_person.get() > current_count:
            self.view.current_person.set(current_count)

    def add_to_order_drag_drop(self, menu_item, person_index=None):
        """從拖放添加項目至訂單"""
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
        self.view.people_count.set(1)  # 重置人數
        self.update_person_spinbox_range()

    def checkout(self):
        if not self.current_order.get_all_items():
            self.view.show_message(self.language_model.get_text("order_is_empty"))
            return

        # 從視圖設置桌號
        self.current_order.table_number = self.view.table_number.get() if self.view.table_number.get() else None
        
        table_info = f" {self.language_model.get_text('for_table')} {self.current_order.table_number}" if self.current_order.table_number else ""
        group_info = f" ({self.language_model.get_text('group_order')})" if self.current_order.is_group_order() else ""

        self.view.show_message(f"{self.language_model.get_text('order')}{table_info}{group_info} {self.language_model.get_text('completed')}! {self.language_model.get_text('total')}: ${self.current_order.total:.2f}")
        self.clear_order()

# main
def main():
    import tkinter as tk
    from tkinter import ttk
    
    root = tk.Tk()
    
    # 創建突出顯示的下拉區域樣式
    style = ttk.Style()
    style.configure("Highlight.TLabelframe", background="lightblue")
    
    # 初始化模型
    menu_model = MenuModel()
    language_model = LanguageModel()
    
    # 初始化視圖（注入語言模型）
    view = POSView(root, language_model)
    
    # 初始化控制器
    controller = POSController(menu_model, view, language_model)
    
    root.mainloop()

if __name__ == "__main__":
    main()
