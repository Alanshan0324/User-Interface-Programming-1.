import tkinter as tk
import sqlite3
from tkinter import messagebox, simpledialog, ttk
# 設定語言翻譯
translations = {
    'Chinese': {'beer': '啤酒', 'fries': '薯條', 'burger': '漢堡', 'order': '點餐', 'submit': '送出', 'clear': '清除', 'delete': '刪除', 'admin': '管理員', 'confirm': '確認', 'cancel': '取消'},
    'English': {'beer': 'Beer', 'fries': 'Fries', 'burger': 'Burger', 'order': 'Order', 'submit': 'Submit', 'clear': 'Clear', 'delete': 'Delete', 'admin': 'Admin', 'confirm': 'Confirm', 'cancel': 'Cancel'},
    'Swedish': {'beer': 'Öl', 'fries': 'Pommes', 'burger': 'Hamburgare', 'order': 'Beställ', 'submit': 'Skicka', 'clear': 'Rensa', 'delete': 'Ta bort', 'admin': 'Admin', 'confirm': 'Bekräfta', 'cancel': 'Avbryt'}
}

current_language = 'English'

def translate(key):
    return translations[current_language].get(key, key)

# 設定商品價格
menu_items = {'beer': 25, 'fries': 15, 'burger': 20}

# 建立使用者帳號
accounts = {f"{i:04d}": f"{i:04d}" for i in range(1, 11)}  # 0001-0010
admin_account = {"admin": "admin"}
orders = {f"{i:04d}": [] for i in range(1, 11)}

class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Ordering System")
        self.create_login_screen()
    
    def create_login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Account").pack()
        self.account_entry = tk.Entry(self.root)
        self.account_entry.pack()
        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack()
        tk.Button(self.root, text="Login", command=self.login).pack()
    
    def login(self):
        account = self.account_entry.get()
        password = self.password_entry.get()
        
        if account in accounts and accounts[account] == password:
            self.create_order_screen(account)
        elif account in admin_account and admin_account[account] == password:
            self.create_admin_screen()
        else:
            messagebox.showerror("Error", "Invalid login")

    def create_order_screen(self, account):
        self.clear_screen()
        self.current_account = account
        
        tk.Label(self.root, text=f"Table {account} Ordering").pack()
        self.order_listbox = tk.Listbox(self.root)
        self.order_listbox.pack()
        
        self.create_menu_list()
        
        tk.Button(self.root, text=translate('submit'), command=self.submit_order).pack()
        tk.Button(self.root, text=translate('delete'), command=self.delete_selected_item).pack()
        tk.Button(self.root, text=translate('clear'), command=self.clear_order).pack()
        tk.Button(self.root, text="Logout", command=self.create_login_screen).pack()
    
    def create_menu_list(self):
        self.menu_listbox = tk.Listbox(self.root)
        for item, price in menu_items.items():
            self.menu_listbox.insert(tk.END, f"{translate(item)} ({price} SEK)")
        self.menu_listbox.pack()
        self.menu_listbox.bind("<Double-Button-1>", self.add_to_order)
    
    def add_to_order(self, event):
        selection = self.menu_listbox.curselection()
        if selection:
            item_text = self.menu_listbox.get(selection[0])
            self.order_listbox.insert(tk.END, item_text)
    
    def delete_selected_item(self):
        selected = self.order_listbox.curselection()
        if selected:
            self.order_listbox.delete(selected[0])
    
    def submit_order(self):
        if messagebox.askyesno(translate('confirm'), "Are you sure you want to submit the order?"):
            orders[self.current_account] = list(self.order_listbox.get(0, tk.END))
            messagebox.showinfo("Success", "Order submitted!")
    
    def clear_order(self):
        self.order_listbox.delete(0, tk.END)
    
    def create_admin_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Admin Panel").pack()
        self.admin_listbox = tk.Listbox(self.root)
        self.admin_listbox.pack()
        
        for table, order in orders.items():
            self.admin_listbox.insert(tk.END, f"Table {table}: {', '.join(order)}")
        
        tk.Button(self.root, text="Edit Order", command=self.edit_order).pack()
        tk.Button(self.root, text="Add Menu Item", command=self.add_menu_item).pack()
        tk.Button(self.root, text="Logout", command=self.create_login_screen).pack()
    
    def edit_order(self):
        selected = self.admin_listbox.curselection()
        if selected:
            table = self.admin_listbox.get(selected[0]).split(":")[0].split()[1]
            new_order = tk.simpledialog.askstring("Edit Order", "Enter new order items separated by commas:")
            if new_order is not None:
                orders[table] = new_order.split(', ')
                self.create_admin_screen()
    
    def add_menu_item(self):
        new_item = tk.simpledialog.askstring("New Menu Item", "Enter new item name:")
        new_price = tk.simpledialog.askinteger("New Menu Item", "Enter price:")
        if new_item and new_price:
            menu_items[new_item] = new_price
            self.create_admin_screen()
    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()
