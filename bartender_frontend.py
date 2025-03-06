import tkinter as tk
from tkinter import messagebox
from bartender_backend import BartenderController, Employee
import subprocess
import sys

class BartenderFrontend:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Bartender Frontend")

        # Configure the root window for responsiveness.
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=1)

        # --- Product List Frame ---
        self.product_frame = tk.Frame(self.root, bd=2, relief=tk.SUNKEN)
        self.product_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.product_frame.rowconfigure(1, weight=1)
        self.product_frame.columnconfigure(0, weight=1)

        tk.Label(self.product_frame, text="Products", font=("Helvetica", 14)).grid(row=0, column=0, sticky="w", padx=5,
                                                                                   pady=5)
        self.product_listbox = tk.Listbox(self.product_frame)
        self.product_listbox.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.product_listbox.bind("<<ListboxSelect>>", self.on_product_select)
        tk.Button(self.product_frame, text="Refresh Products", command=self.refresh_products).grid(row=2, column=0,
                                                                                                   sticky="ew", padx=5,
                                                                                                   pady=5)

        # --- Control Frame ---
        self.control_frame = tk.Frame(self.root, bd=2, relief=tk.SUNKEN)
        self.control_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.control_frame.columnconfigure(0, weight=1)
        for i in range(20):
            self.control_frame.rowconfigure(i, weight=1)

        row = 0
        tk.Label(self.control_frame, text="Product ID:").grid(row=row, column=0, sticky="w", padx=5, pady=2);
        row += 1
        self.entry_product_id = tk.Entry(self.control_frame)
        self.entry_product_id.grid(row=row, column=0, sticky="ew", padx=5, pady=2);
        row += 1

        tk.Label(self.control_frame, text="New Price:").grid(row=row, column=0, sticky="w", padx=5, pady=2);
        row += 1
        self.entry_new_price = tk.Entry(self.control_frame)
        self.entry_new_price.grid(row=row, column=0, sticky="ew", padx=5, pady=2);
        row += 1
        tk.Button(self.control_frame, text="Modify Price", command=self.modify_price).grid(row=row, column=0,
                                                                                           sticky="ew", padx=5, pady=2);
        row += 1

        tk.Button(self.control_frame, text="Remove Product", command=self.remove_product).grid(row=row, column=0,
                                                                                               sticky="ew", padx=5,
                                                                                               pady=2);
        row += 1

        tk.Label(self.control_frame, text="New Stock:").grid(row=row, column=0, sticky="w", padx=5, pady=2);
        row += 1
        self.entry_new_stock = tk.Entry(self.control_frame)
        self.entry_new_stock.grid(row=row, column=0, sticky="ew", padx=5, pady=2);
        row += 1
        tk.Button(self.control_frame, text="Update Stock", command=self.update_stock).grid(row=row, column=0,
                                                                                           sticky="ew", padx=5, pady=2);
        row += 1

        tk.Button(self.control_frame, text="Undo (Global)", command=self.undo).grid(row=row, column=0, sticky="ew",
                                                                                    padx=5, pady=2);
        row += 1
        tk.Button(self.control_frame, text="Redo (Global)", command=self.redo).grid(row=row, column=0, sticky="ew",
                                                                                    padx=5, pady=2);
        row += 1

        # --- Order Management Controls ---
        tk.Label(self.control_frame, text="--- Order Management ---", fg="darkgreen").grid(row=row, column=0,
                                                                                           sticky="w", padx=5, pady=5);
        row += 1
        tk.Button(self.control_frame, text="Create New Order", command=self.create_order).grid(row=row, column=0,
                                                                                               sticky="ew", padx=5,
                                                                                               pady=2);
        row += 1

        tk.Label(self.control_frame, text="Quantity to Add:").grid(row=row, column=0, sticky="w", padx=5, pady=2);
        row += 1
        self.entry_quantity = tk.Entry(self.control_frame)
        self.entry_quantity.grid(row=row, column=0, sticky="ew", padx=5, pady=2);
        row += 1
        tk.Button(self.control_frame, text="Add Item to Order", command=self.add_item_to_order).grid(row=row, column=0,
                                                                                                     sticky="ew",
                                                                                                     padx=5, pady=2);
        row += 1

        tk.Label(self.control_frame, text="Quantity to Remove:").grid(row=row, column=0, sticky="w", padx=5, pady=2);
        row += 1
        self.entry_remove_quantity = tk.Entry(self.control_frame)
        self.entry_remove_quantity.grid(row=row, column=0, sticky="ew", padx=5, pady=2);
        row += 1
        tk.Button(self.control_frame, text="Remove Item from Order", command=self.remove_item_from_order).grid(row=row,
                                                                                                               column=0,
                                                                                                               sticky="ew",
                                                                                                               padx=5,
                                                                                                               pady=2);
        row += 1

        tk.Label(self.control_frame, text="Order Discount (%):").grid(row=row, column=0, sticky="w", padx=5, pady=2);
        row += 1
        self.entry_order_discount = tk.Entry(self.control_frame)
        self.entry_order_discount.grid(row=row, column=0, sticky="ew", padx=5, pady=2);
        row += 1
        tk.Button(self.control_frame, text="Apply Discount to Order Item", command=self.offer_discount_on_order).grid(
            row=row, column=0, sticky="ew", padx=5, pady=2);
        row += 1

        tk.Button(self.control_frame, text="Finish Order", command=self.finish_order).grid(row=row, column=0,
                                                                                           sticky="ew", padx=5, pady=2);
        row += 1
        tk.Button(self.control_frame, text="Order Undo", command=self.order_undo).grid(row=row, column=0, sticky="ew",
                                                                                       padx=5, pady=2);
        row += 1
        tk.Button(self.control_frame, text="Order Redo", command=self.order_redo).grid(row=row, column=0, sticky="ew",
                                                                                       padx=5, pady=2);
        row += 1

        tk.Label(self.control_frame, text="Current Order:", fg="purple").grid(row=row, column=0, sticky="w", padx=5,
                                                                              pady=5);
        row += 1
        self.order_listbox = tk.Listbox(self.control_frame)
        self.order_listbox.grid(row=row, column=0, sticky="nsew", padx=5, pady=2);
        row += 1
        tk.Button(self.control_frame, text="Log out", command=self.logout).grid(row=row, column=0, sticky="ew",
                                                                                       padx=5, pady=2);
        row += 1

        self.status_label = tk.Label(self.control_frame, text="", fg="blue")
        self.status_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)

        self.refresh_products()
        self.refresh_order()

    def refresh_products(self):
        self.product_listbox.delete(0, tk.END)
        for pid in self.controller.get_product_ids():
            p = self.controller.get_product(pid)
            text = f"ID: {p.id} | {p.name} | Price: {p.price} | Stock: {p.stock_count} | Available: {p.available}"
            self.product_listbox.insert(tk.END, text)

    def refresh_order(self):
        self.order_listbox.delete(0, tk.END)
        if self.controller.current_order:
            order = self.controller.current_order
            for item in order.items:
                self.order_listbox.insert(tk.END,
                                          f"{item['product'].name} x {item['quantity']} ({item['discount']}% off)")
            self.order_listbox.insert(tk.END, f"Total: {order.total()}")
        else:
            self.order_listbox.insert(tk.END, "No active order.")

    def on_product_select(self, event):
        selection = self.product_listbox.curselection()
        if selection:
            index = selection[0]
            text = self.product_listbox.get(index)
            try:
                id_part = text.split("|")[0].strip()  # e.g., "ID: 10001"
                product_id = id_part.split(":")[1].strip()
                self.entry_product_id.delete(0, tk.END)
                self.entry_product_id.insert(0, product_id)
            except (IndexError, ValueError):
                pass

    def remove_product(self):
        product_id_str = self.entry_product_id.get()
        if product_id_str:
            try:
                product_id = int(product_id_str)
                self.controller.remove_product_from_menu(product_id)
                self.status_label.config(text=f"Removed product {product_id} from menu.")
                self.refresh_products()
            except ValueError:
                messagebox.showerror("Error", "Product ID must be an integer.")

    def modify_price(self):
        product_id_str = self.entry_product_id.get()
        new_price_str = self.entry_new_price.get()
        if product_id_str and new_price_str:
            try:
                product_id = int(product_id_str)
                new_price = float(new_price_str)
                self.controller.modify_product_price(product_id, new_price)
                self.status_label.config(text=f"Modified product {product_id} price to {new_price}.")
                self.refresh_products()
            except ValueError:
                messagebox.showerror("Error", "Product ID must be integer and price must be a number.")

    def offer_discount_on_order(self):
        product_id_str = self.entry_product_id.get()
        discount_str = self.entry_order_discount.get()
        if product_id_str and discount_str:
            try:
                product_id = int(product_id_str)
                discount = float(discount_str)
                self.controller.offer_discount_on_order(product_id, discount)
                self.status_label.config(
                    text=f"Applied discount of {discount}% on order item for product {product_id}.")
                self.refresh_order()
            except ValueError:
                messagebox.showerror("Error", "Product ID must be integer and discount must be a number.")

    def update_stock(self):
        product_id_str = self.entry_product_id.get()
        new_stock_str = self.entry_new_stock.get()
        if product_id_str and new_stock_str:
            try:
                product_id = int(product_id_str)
                new_stock = int(new_stock_str)
                self.controller.update_stock(product_id, new_stock)
                self.status_label.config(text=f"Updated product {product_id} stock to {new_stock}.")
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
        product_id_str = self.entry_product_id.get()
        quantity_str = self.entry_quantity.get()
        if product_id_str and quantity_str:
            try:
                product_id = int(product_id_str)
                quantity = int(quantity_str)
                result = self.controller.add_item_to_current_order(product_id, quantity)
                if result is None:
                    messagebox.showerror("Error", "Insufficient stock to add item.")
                else:
                    self.status_label.config(text=f"Added product {product_id} x {quantity} to active order.")
                self.refresh_order()
            except ValueError:
                messagebox.showerror("Error", "Product ID and quantity must be integers.")

    def remove_item_from_order(self):
        product_id_str = self.entry_product_id.get()
        remove_qty_str = self.entry_remove_quantity.get()
        if product_id_str and remove_qty_str:
            try:
                product_id = int(product_id_str)
                remove_qty = int(remove_qty_str)
                self.controller.remove_item_from_current_order(product_id, remove_qty)
                self.status_label.config(text=f"Removed {remove_qty} of product {product_id} from active order.")
                self.refresh_order()
            except ValueError:
                messagebox.showerror("Error", "Product ID and removal quantity must be integers.")

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

    def run(self):
        self.root.mainloop()
    def logout(self):
        """登出並回到登入介面"""
        confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if confirm:
            
   
            self.root.quit()  # 結束 Tkinter 事件循環
            self.root.destroy()  # 銷毀 Tkinter 主視窗
            subprocess.Popen([sys.executable, "login_interface.py"], start_new_session=True)  # 啟動新視窗



if __name__ == "__main__":
    employee = Employee(1001, "Alice", "Bartender")
    controller = BartenderController(employee)
    controller.login_employee()
    frontend = BartenderFrontend(controller)
    frontend.run()
