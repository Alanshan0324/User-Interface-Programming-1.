import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from controller import Controller, Employee
import subprocess
import sys
LANGUAGES = {
    'en': {  # English
       
        'logout': "Logout",
        'create_order_button': "Create Order",
        'add_item_button': "Add Item to Order",
        'remove_item_button': "Remove Item from Order",
        'finish_order_button': "Finish Order",
        'undo_button': "Undo",
        'redo_button': "Redo",
        'language_label': "Language",
        'product_label': "Products",
        'sort_label': "Sort by:",
        'product_id_label': "Product ID:",
        'new_price_label': "New Price:",
        'new_stock_label': "New Stock:",
        'quantity_label': "Quantity:",
        'remove_quantity_label': "Quantity to Remove:",
        'current_order_label': "Current Order:",
        'order_management_label': "--- Order Management ---",
        'refill_low_stock_button': "Refill Low Stock Items",
        'alert_security_button': "Alert Security",
        'refresh_products_button': "Refresh Products",
        'modify_price_button': "Modify Price",
        'remove_product_button': "Remove Product",
        'update_stock_button': "Update Stock",
        "order_undo": "Order Undo",
        "order_redo": "Order Redo",
        "do_accounting": "Do Accounting",
        "current_order": "Current Order:",
        # 其他按鈕和標籤文字...
    },
    'zh': {  # 中文
        
        'logout': "登出",
        'create_order_button': "創建訂單",
        'add_item_button': "添加項目",
        'remove_item_button': "移除項目",
        'finish_order_button': "完成訂單",
        'undo_button': "撤銷",
        'redo_button': "重做",
        'language_label': "語言",
        'product_label': "產品",
        'sort_label': "排序方式:",
        'product_id_label': "產品 ID:",
        'new_price_label': "新價格:",
        'new_stock_label': "新庫存:",
        'quantity_label': "數量:",
        'remove_quantity_label': "移除數量:",
        'current_order_label': "當前訂單:",
        'order_management_label': "--- 訂單管理 ---",
        'refill_low_stock_button': "補充低庫存商品",
        'alert_security_button': "警報安全",
        'refresh_products_button': "刷新產品",
        'modify_price_button': "修改價格",
        'remove_product_button': "移除產品",
        'update_stock_button': "更新庫存",
        "order_undo": "訂單撤銷",
        "order_redo": "訂單重做",
        'do_accounting': "做會計",
        "current_order": "當前訂單:",

        # 其他按鈕和標籤文字...
    },
    'sv': {  # Swedish
        
        'logout': "Logga ut",
        'create_order_button': "Skapa Order",
        'add_item_button': "Lägg till Artikel",
        'remove_item_button': "Ta bort Artikel",
        'finish_order_button': "Avsluta Order",
        'undo_button': "Ångra",
        'redo_button': "Gör om",
        'language_label': "Språk",
        'product_label': "Produkter",
        'sort_label': "Sortera efter:",
        'product_id_label': "Produkt ID:",
        'new_price_label': "Nytt Pris:",
        'new_stock_label': "Nytt Lager:",
        'quantity_label': "Kvantitet:",
        'do_accounting': "Gör bokföring",
        'remove_quantity_label': "Kvantitet att Ta Bort:",
        'current_order_label': "Aktuell Order:",
        'order_management_label': "--- Orderhantering ---",
        'refill_low_stock_button': "Fyll på Lågt Lager",
        'alert_security_button': "Larma Säkerhet",
        'refresh_products_button': "Uppdatera Produkter",
        'modify_price_button': "Ändra Pris",
        'remove_product_button': "Ta Bort Produkt",
        'update_stock_button': "Upp",
        "order_undo": "OrderÅngra",
        "order_redo": "OrderGör om",
        "current_order": "Aktuell Order:",



        # 其他按鈕和標籤文字...
    }
}

class BartenderFrontend:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.geometry("1430x1000")
        self.root.title("Bartender Frontend")
        self.root.minsize(600, 400)  # 設置最小視窗大小
        self.current_language = 'en'
        self.language_var = tk.StringVar(value=self.current_language)

        # 定義響應式設計的斷點
        self.breakpoints = {
            "mobile": 800,    # 寬度小於800px時使用手機佈局
            "tablet": 1200    # 寬度在800px到1200px之間使用平板佈局
        }
        
        # 追蹤當前佈局
        self.current_layout = "desktop"  # 默認桌面佈局

        # 為響應式設計配置根視窗
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)  # 為手機模式添加第二行
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=1)

        # --- 產品列表框架 ---
        self.product_frame = tk.Frame(self.root, bd=2, relief=tk.SUNKEN)
        self.product_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.product_frame.rowconfigure(1, weight=1)
        self.product_frame.columnconfigure(0, weight=1)
        self.product_frame.columnconfigure(1, weight=1)

        self.product_label= tk.Label(self.product_frame, text=self.controller.get_translation('product_label'), font=("Helvetica", 14))
        self.product_label.grid(row=0, column=0, sticky="w", padx=5,pady=5)
          # 語言選擇框架
        

        # 語言標籤
        self.language_label = ttk.Label(self.product_frame, text="Language:", font=("Arial", 10))
        self.language_label.grid(row=0, column=0, padx=(0, 5), sticky="e")
        self.language_var = tk.StringVar()
        
        # Set default value
        self.language_var.set(list(LANGUAGES.keys())[0])
        
        # 使用 OptionMenu 替代 Combobox
        self.language_menu = tk.OptionMenu(self.product_frame,
                                        self.language_var,   
                                        *LANGUAGES.keys()
                                        ,command=self.change_language)

        
        self.language_menu.grid(row=0, column=1, padx=(0, 5), sticky="w")
       
        
        
        
                                         
        self.sort_var = tk.StringVar(value="Name")
        self.sort_label =  tk.Label(self.product_frame, text=self.controller.get_translation('sort_label'))
        self.sort_label.grid(row=0, column=1, sticky="e", padx=5, pady=5)
        sort_options = ["Name", "Price", "Stock", "Availability", "Id"]
        self.sort_menu = tk.OptionMenu(self.product_frame, self.sort_var, *sort_options,
                                       command=lambda _: self.refresh_products())
        self.sort_menu.grid(row=0, column=2, sticky="e", padx=5, pady=5)

        self.product_listbox = tk.Listbox(self.product_frame)
        self.product_listbox.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.product_listbox.bind("<<ListboxSelect>>", self.on_product_select)
        self.refresh_products_button = tk.Button(self.product_frame, text=self.controller.get_translation('refresh_products_button'), command=self.refresh_products) 
        self.refresh_products_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        # --- 控制框架 ---
        self.control_frame = tk.Frame(self.root, bd=2, relief=tk.SUNKEN)
        self.control_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.control_frame.columnconfigure(0, weight=1)
        for i in range(20):
            self.control_frame.rowconfigure(i, weight=1)

        row = 0
        self.product_id_label = tk.Label(self.control_frame, text=self.controller.get_translation('product_id_label'))
        self.product_id_label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
        row += 1
        self.entry_product_id = tk.Entry(self.control_frame)
        self.entry_product_id.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1

        self.new_price_label = tk.Label(self.control_frame, text=self.controller.get_translation('new_price_label'))
        self.new_price_label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
        row += 1

        self.entry_new_price = tk.Entry(self.control_frame)
        self.entry_new_price.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1
        self.modify_price_button = tk.Button(self.control_frame,
                                             text=self.controller.get_translation('modify_price_button'),
                                             command=self.modify_price)
        self.modify_price_button.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1

        self.remove_product_button = tk.Button(self.control_frame, text=self.controller.get_translation('remove_product_button'), command=self.remove_product)
        self.remove_product_button.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1

        self.new_stock_label = tk.Label(self.control_frame, text=self.controller.get_translation('new_stock_label'))
        self.new_stock_label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
        row += 1
        self.entry_new_stock = tk.Entry(self.control_frame)
        self.entry_new_stock.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1
        self.update_stock_button = tk.Button(self.control_frame, text=self.controller.get_translation('update_stock_button'), command=self.update_stock) 
        self.update_stock_button.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1

        self.undo_button = tk.Button(self.control_frame, text=self.controller.get_translation('undo_button'), command=self.undo) 
        self.undo_button.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1
        self.redo_button = tk.Button(self.control_frame,  text=self.controller.get_translation('redo_button'), command=self.redo) 
        self.redo_button.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1

        # 補充低庫存商品按鈕
        self.refill_low_stock_button = tk.Button(self.control_frame, text=self.controller.get_translation('refill_low_stock_button'), command=self.refill_low_stock) 
        self.refill_low_stock_button.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1

        # 警報安全
        self.alert_security_button = tk.Button(self.control_frame, text=self.controller.get_translation('alert_security_button'), command=self.alert_security) 
        self.alert_security_button.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1

        # --- 訂單管理控制 ---
        self.order_management_label = tk.Label(self.control_frame, text=self.controller.get_translation('order_management_label'), fg="darkgreen")
        self.order_management_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
        row += 1
        self.create_order_button = tk.Button(self.control_frame, text=self.controller.get_translation('create_order_button'), command=self.create_order)
        self.create_order_button.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1

        self.quantity_label = tk.Label(self.control_frame, text=self.controller.get_translation('quantity_label'))
        self.quantity_label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
        row += 1
        self.entry_quantity = tk.Entry(self.control_frame)
        self.entry_quantity.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1
        self.add_item_button = tk.Button(self.control_frame, text=self.controller.get_translation('add_item_button'), command=self.add_item_to_order)
        self.add_item_button.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1

        self.remove_quantity_label = tk.Label(self.control_frame,text=self.controller.get_translation('remove_quantity_label'))
        self.remove_quantity_label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
        row += 1
        self.entry_remove_quantity = tk.Entry(self.control_frame)
        self.entry_remove_quantity.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1
        self.remove_item_button = tk.Button(self.control_frame, text=self.controller.get_translation('remove_item_button'), command=self.remove_item_from_order)
        self.remove_item_button.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1

        self.finish_order_button = tk.Button(self.control_frame, text=self.controller.get_translation('finish_order_button'), command=self.finish_order)
        self.finish_order_button.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1
        self.order_undo_button = tk.Button(self.control_frame, text=self.controller.get_translation('order_undo'), command=self.order_undo)
        self.order_undo_button.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1
        self.order_redo_button = tk.Button(self.control_frame, text=self.controller.get_translation('order_redo'), command=self.order_redo)
        self.order_redo_button.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1

        self.do_accounting_button = tk.Button(self.control_frame, text=self.controller.get_translation('do_accounting'), command=self.do_accounting)
        self.do_accounting_button.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1

        self.current_order_label = tk.Label(self.control_frame, text=self.controller.get_translation('current_order'), fg="purple")
        self.current_order_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
        row += 1
        self.order_listbox = tk.Listbox(self.control_frame)
        self.order_listbox.grid(row=row, column=0, sticky="nsew", padx=5, pady=2)
        row += 1

        self.status_label = tk.Label(self.control_frame, text="", fg="blue")
        self.status_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)

        self.logout_button = tk.Button(self.control_frame, text=self.controller.get_translation('logout'), command=self.logout) 
        self.logout_button.grid(row=row, column=0, sticky="ew", padx=5, pady=2)
        row += 1
        self
        # 存儲所有標籤和按鈕，用於響應式設計調整
        self.all_labels = []
        for widget in self.product_frame.winfo_children():
            if isinstance(widget, tk.Label):
                self.all_labels.append(widget)
        for widget in self.control_frame.winfo_children():
            if isinstance(widget, tk.Label):
                self.all_labels.append(widget)
        
        self.all_entries = [self.entry_product_id, self.entry_new_price, self.entry_new_stock,
                           self.entry_quantity, self.entry_remove_quantity]
        
        self.all_buttons = []
        for widget in self.product_frame.winfo_children():
            if isinstance(widget, tk.Button):
                self.all_buttons.append(widget)
        for widget in self.control_frame.winfo_children():
            if isinstance(widget, tk.Button):
                self.all_buttons.append(widget)
                
        # 綁定視窗大小調整事件
        self.root.bind("<Configure>", self.on_window_resize)

        self.refresh_products()
        self.refresh_order()
        self.update_ui_texts()

    def refresh_products(self):
        self.product_listbox.delete(0, tk.END)
        # Get all products from the controller
        products = [self.controller.get_product(pid) for pid in self.controller.get_product_ids()]

        sort_option = self.sort_var.get()
        if sort_option == "Name":
            products = sorted(products, key=lambda p: p.name.lower())
        elif sort_option == "Price":
            products = sorted(products, key=lambda p: p.price)
        elif sort_option == "Stock":
            products = sorted(products, key=lambda p: p.stock_count)
        elif sort_option == "Availability":
            products = sorted(products, key=lambda p: not p.available)
        elif sort_option == "Id":
            products = sorted(products, key=lambda p: int(p.id))


        for p in products:
            warning = " *** LOW STOCK ***" if int(p.stock_count) < 5 else ""
            text = (f"ID: {p.id} | {p.name} | Price: {p.price} | Stock: {p.stock_count} | "
                    f"Available: {p.available}{warning}")
            self.product_listbox.insert(tk.END, text)

    def refresh_order(self):
        self.order_listbox.delete(0, tk.END)
        if self.controller.current_order:
            order = self.controller.current_order
            for item in order.items:
                # Assuming each order item is a dict with keys: product, quantity, discount
                self.order_listbox.insert(
                    tk.END,
                    f"{item['product'].name} x {item['quantity']} ({item['discount']}% off)"
                )
            self.order_listbox.insert(tk.END, f"Total: {order.total()}")
        else:
            self.order_listbox.insert(tk.END, "No active order.")

    def on_product_select(self, event):
        selection = self.product_listbox.curselection()
        if selection:
            index = selection[0]
            text = self.product_listbox.get(index)
            try:
                # Expected format: "ID: <id> | ..."
                id_part = text.split("|")[0].strip()  # e.g., "ID: 1"
                product_id = id_part.split(":")[1].strip()
                self.entry_product_id.delete(0, tk.END)
                self.entry_product_id.insert(0, product_id)
            except (IndexError, ValueError):
                pass

    def remove_product(self):
        product_id_str = self.entry_product_id.get().strip()
        if product_id_str:
            # Use product_id_str directly (IDs are stored as strings)
            self.controller.remove_product_from_menu(product_id_str)
            self.status_label.config(text=f"Removed product {product_id_str} from menu.")
            self.refresh_products()

    def modify_price(self):
        product_id_str = self.entry_product_id.get().strip()
        new_price_str = self.entry_new_price.get().strip()  # now matches the widget name
        if product_id_str and new_price_str:
            try:
                new_price = float(new_price_str)
                self.controller.modify_product_price(product_id_str, new_price)
                self.status_label.config(text=f"Modified product {product_id_str} price to {new_price}.")
                self.refresh_products()
            except ValueError:
                messagebox.showerror("Error", "Product ID must be valid and price must be a number.")

    def update_stock(self):
        product_id_str = self.entry_product_id.get().strip()
        new_stock_str = self.entry_new_stock.get().strip()
        if product_id_str and new_stock_str:
            try:
                new_stock = int(new_stock_str)
                self.controller.update_stock(product_id_str, new_stock)
                self.status_label.config(text=f"Updated product {product_id_str} stock to {new_stock}.")
                self.refresh_products()
            except ValueError:
                messagebox.showerror("Error", "Product ID and new stock must be integers.")

    def undo(self):
        self.controller.undo()
        self.status_label.config(text="Undid last global action.")
        self.refresh_products()

    def redo(self):
        self.controller.redo()
        self.status_label.config(text="Redid last global action.")
        self.refresh_products()

    def create_order(self):
        new_order = self.controller.create_order()
        self.status_label.config(text=f"Created new active order (ID {new_order.order_id}).")
        self.refresh_order()

    def add_item_to_order(self):
        product_id_str = self.entry_product_id.get().strip()
        quantity_str = self.entry_quantity.get().strip()
        if product_id_str and quantity_str:
            try:
                quantity = int(quantity_str)
                # Use product_id_str as is.
                result = self.controller.add_item_to_current_order(product_id_str, quantity)
                if result is None:
                    messagebox.showerror("Error", "Insufficient stock to add item.")
                else:
                    self.status_label.config(text=f"Added product {product_id_str} x {quantity} to active order.")
                self.refresh_order()
            except ValueError:
                messagebox.showerror("Error", "Product ID and quantity must be valid.")

    def remove_item_from_order(self):
        product_id_str = self.entry_product_id.get().strip()
        remove_qty_str = self.entry_remove_quantity.get().strip()
        if product_id_str and remove_qty_str:
            try:
                remove_qty = int(remove_qty_str)
                self.controller.remove_item_from_current_order(product_id_str, remove_qty)
                self.status_label.config(text=f"Removed {remove_qty} of product {product_id_str} from active order.")
                self.refresh_order()
            except ValueError:
                messagebox.showerror("Error", "Product ID and removal quantity must be valid.")

    def finish_order(self):
        total = self.controller.finish_current_order()
        if total is not None:
            messagebox.showinfo("Order Finished", f"Order finished. Total: {total}.")
            self.status_label.config(text=f"Finished order with total {total}.")
            self.refresh_order()
            self.refresh_products()
        else:
            messagebox.showerror("Error", "No active order to finish.")

    def order_undo(self):
        self.controller.order_undo()
        self.status_label.config(text="Undid last order change.")
        self.refresh_order()

    def order_redo(self):
        self.controller.order_redo()
        self.status_label.config(text="Redid last order change.")
        self.refresh_order()

    def do_accounting(self):
        summary = self.controller.do_accounting()
        messagebox.showinfo("Accounting Summary", summary)

    def refill_low_stock(self):
        count = self.controller.refill_low_stock_items()
        self.status_label.config(text=f"Refilled {count} items with low stock.")
        self.refresh_products()

    def alert_security(self):
        self.status_label.config(text="Security alert sent.")

    def logout(self):
        """Logout and return to the login interface."""
        confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if confirm:
            self.root.quit()  # End Tkinter event loop
            self.root.destroy()  # Destroy main window
            subprocess.Popen([sys.executable, "login_interface.py"], start_new_session=True)

    def do_accounting(self):
        summary = self.controller.do_accounting()
        messagebox.showinfo("Accounting Summary", summary)

    def on_window_resize(self, event):
        """處理視窗大小調整事件，應用響應式佈局"""
        # 只處理來自根視窗的事件，而不是子部件
        if event.widget == self.root:
            width = event.width
            
            # 根據視窗寬度確定佈局
            if width < self.breakpoints["mobile"] and self.current_layout != "mobile":
                self.apply_mobile_layout()
                self.current_layout = "mobile"
            elif width >= self.breakpoints["mobile"] and width < self.breakpoints["tablet"] and self.current_layout != "tablet":
                self.apply_tablet_layout()
                self.current_layout = "tablet"
            elif width >= self.breakpoints["tablet"] and self.current_layout != "desktop":
                self.apply_desktop_layout()
                self.current_layout = "desktop"

    def apply_mobile_layout(self):
        """應用手機佈局，適用於小屏幕"""
        # 重新配置網格，使產品框架和控制框架垂直排列
        self.root.grid_columnconfigure(0, weight=1)  # 全寬
        self.root.grid_columnconfigure(1, weight=0)  # 隱藏/折疊
        
        # 從網格中移除兩個框架
        self.product_frame.grid_forget()
        self.control_frame.grid_forget()
        
        # 將產品框架放在上半部分（使其佔據50%的高度）
        # 將行0配置為佔比 1，確保產品框架佔據屏幕的上50%
        self.root.rowconfigure(0, weight=1)  
        self.root.rowconfigure(1, weight=1)  # 行1也佔比1，確保下半部分也有50%的空間
        
        # 重新放置產品框架在上半部分（第0行）
        self.product_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        # 重新放置控制框架在下半部分（第1行）
        self.control_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        
        # 設置產品框架的最小高度，確保它顯示足夠的內容
        self.product_listbox.config(height=10)
        
        # 減小字體大小
        for label in self.all_labels:
            current_font = label.cget("font")
            if isinstance(current_font, str) and current_font:
                parts = current_font.split()
                if len(parts) >= 2:
                    family = parts[0]
                    try:
                        size = max(8, int(parts[1]) - 2)  # 減小字體大小但不小於8
                        label.config(font=(family, size))
                    except (ValueError, IndexError):
                        pass
        
        # 縮小輸入欄位
        for entry in self.all_entries:
            entry.config(width=10)
        
        # 縮小訂單列表框的高度以節省空間
        self.order_listbox.config(height=4)
        
        # 減少按鈕的內邊距
        for button in self.all_buttons:
            button.grid_configure(padx=2, pady=1)

    def apply_tablet_layout(self):
        """應用平板佈局，適用於中等屏幕"""
        # 調整平板視圖的比例
        self.root.grid_columnconfigure(0, weight=2)  # 產品列表佔2/3
        self.root.grid_columnconfigure(1, weight=1)  # 控制面板佔1/3
        
        # 重置行配置為原始值
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=0)  # 禁用第二行
        
        # 恢復兩個框架到原始位置，但調整大小
        self.product_frame.grid_forget()
        self.control_frame.grid_forget()
        
        self.product_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.control_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        # 調整中等屏幕的字體大小
        for label in self.all_labels:
            current_font = label.cget("font")
            if isinstance(current_font, str) and current_font:
                parts = current_font.split()
                if len(parts) >= 2:
                    family = parts[0]
                    try:
                        size = max(10, int(parts[1]) - 1)  # 略微減小字體大小
                        label.config(font=(family, size))
                    except (ValueError, IndexError):
                        pass
        
        # 調整平板視圖的輸入大小
        for entry in self.all_entries:
            entry.config(width=12)
        
        # 調整平板視圖的列表框高度
        self.product_listbox.config(height=10)
        self.order_listbox.config(height=6)
        
        # 按鈕的適中內邊距
        for button in self.all_buttons:
            button.grid_configure(padx=3, pady=2)

    def apply_desktop_layout(self):
        """應用桌面佈局，適用於大屏幕"""
        # 原始桌面比例
        self.root.grid_columnconfigure(0, weight=3)  # 產品列表佔3/4
        self.root.grid_columnconfigure(1, weight=1)  # 控制面板佔1/4
        
        # 重置行配置
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=0)  # 禁用第二行
        
        # 確保框架處於正確位置
        self.product_frame.grid_forget()
        self.control_frame.grid_forget()
        
        self.product_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.control_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        # 恢復原始字體大小
        for label in self.all_labels:
            current_font = label.cget("font")
            if isinstance(current_font, str) and current_font:
                parts = current_font.split()
                if len(parts) >= 2:
                    family = parts[0]
                    try:
                        # 根據標籤上下文確定原始大小
                        if "Products" in label.cget("text") or "Current Order:" in label.cget("text"):
                            size = 14
                        else:
                            size = 12
                        label.config(font=(family, size))
                    except (ValueError, IndexError):
                        pass
        
        # 恢復輸入欄位大小
        for entry in self.all_entries:
            entry.config(width=15)
        
        # 列表框的完整高度
        self.product_listbox.config(height=15)
        self.order_listbox.config(height=8)
        
        # 按鈕的原始內邊距
        for button in self.all_buttons:
            button.grid_configure(padx=5, pady=2)

    

   
   
    def change_language(self, select_language):
        
        self.current_language = select_language
        selected_language = self.language_var.get()
        self.update_ui_texts()  # 更新 UI 文字


    def update_ui_texts(self):
        # 更新按鈕文字
        
        print(" update_ui_texts() 被呼叫了！")  # 測試：確認這個方法有執行
        self.controller.current_language = self.current_language
        self.update_stock_button.config(text=self.controller.get_translation('update_stock_button'))
        self.create_order_button.config(text=self.controller.get_translation('create_order_button'))
        self.add_item_button.config(text=self.controller.get_translation('add_item_button'))
        self.remove_item_button.config(text=self.controller.get_translation('remove_item_button'))
        self.finish_order_button.config(text=self.controller.get_translation('finish_order_button'))
        self.undo_button.config(text=self.controller.get_translation('undo_button'))
        self.redo_button.config(text=self.controller.get_translation('redo_button'))
        self.refill_low_stock_button.config(text=self.controller.get_translation('refill_low_stock_button'))
        self.alert_security_button.config(text=self.controller.get_translation('alert_security_button'))
        self.order_undo_button.config(text=self.controller.get_translation('order_undo'))
        self.order_redo_button.config(text=self.controller.get_translation('order_redo'))
        self.refresh_products_button.config(text=self.controller.get_translation('refresh_products_button'))
        self.modify_price_button.config(text=self.controller.get_translation('modify_price_button'))
        self.remove_product_button.config(text=self.controller.get_translation('remove_product_button'))
        self.logout_button.config(text=self.controller.get_translation('logout'))
        self.do_accounting_button.config(text=self.controller.get_translation('do_accounting'))

        # 更新標籤文字
        self.language_label.config(text=self.controller.get_translation('language_label'))
        self.product_label.config(text=self.controller.get_translation('product_label'))
        self.sort_label.config(text=self.controller.get_translation('sort_label'))
        self.product_id_label.config(text=self.controller.get_translation('product_id_label'))
        self.new_price_label.config(text=self.controller.get_translation('new_price_label'))
        self.new_stock_label.config(text=self.controller.get_translation('new_stock_label'))
        self.quantity_label.config(text=self.controller.get_translation('quantity_label'))
        self.remove_quantity_label.config(text=self.controller.get_translation('remove_quantity_label'))
        self.current_order_label.config(text=self.controller.get_translation('current_order_label'))
        self.order_management_label.config(text=self.controller.get_translation('order_management_label'))


    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    employee = Employee(1001, "Alice", "Bartender")
    
    controller = Controller(employee)
    controller.login_employee()
    frontend = BartenderFrontend(controller)
    frontend.run()
