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


class MenuModel:
    def __init__(self):
        # Sample menu data
        self.menu_items = [
            MenuItem(1, "Beer", 5.00, "Drinks"),
            MenuItem(2, "Wine", 7.00, "Drinks"),
            MenuItem(3, "Cocktail", 8.00, "Drinks"),
            MenuItem(4, "Nachos", 6.00, "Food"),
            MenuItem(5, "Wings", 10.00, "Food"),
            MenuItem(6, "Fries", 4.00, "Food")
        ]

    def get_menu_items(self):
        return self.menu_items

    def get_item_by_id(self, item_id):
        return next((item for item in self.menu_items if item.id == item_id), None)

# view
import tkinter as tk
from tkinter import ttk, messagebox

class POSView:
    def __init__(self, root):
        self.root = root
        self.root.title("Bar POS System")
        self.root.geometry("1350x600")
        
        # Create main frames
        self.menu_frame = ttk.Frame(root)
        self.menu_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.order_frame = ttk.Frame(root)
        self.order_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Menu section
        ttk.Label(self.menu_frame, text="Menu", font=('Arial', 16, 'bold')).pack()
        self.menu_tree = ttk.Treeview(self.menu_frame, columns=('ID', 'Name', 'Price', 'Category'), show='headings')
        self.menu_tree.pack(fill=tk.BOTH, expand=True)
        
        self.menu_tree.heading('ID', text='ID')
        self.menu_tree.heading('Name', text='Name')
        self.menu_tree.heading('Price', text='Price')
        self.menu_tree.heading('Category', text='Category')
        
        # Order section with notebook
        ttk.Label(self.order_frame, text="Current Order", font=('Arial', 16, 'bold')).pack()
        
        # Create notebook
        self.order_notebook = ttk.Notebook(self.order_frame)
        self.order_notebook.pack(fill=tk.BOTH, expand=True)
        
        # Total order tab
        self.total_order_frame = ttk.Frame(self.order_notebook)
        self.order_notebook.add(self.total_order_frame, text="Total Order")
        
        # Create total order tree
        self.order_tree = ttk.Treeview(self.total_order_frame, columns=('Name', 'Quantity', 'Price'), show='headings')
        self.order_tree.pack(fill=tk.BOTH, expand=True)
        
        self.order_tree.heading('Name', text='Name')
        self.order_tree.heading('Quantity', text='Quantity')
        self.order_tree.heading('Price', text='Price')
        
        # Individual orders frame (will be populated dynamically)
        self.individual_trees = {}  # Store each person's treeview
        
        # Total label (Shown below all pages)
        self.total_label = ttk.Label(self.order_frame, text="Total: $0.00", font=('Arial', 14))
        self.total_label.pack(pady=10)
        
        # Total label
        self.total_label = ttk.Label(self.order_frame, text="Total: $0.00", font=('Arial', 14))
        self.total_label.pack(pady=10)

        #table number and order type
        order_config_frame = ttk.Frame(self.order_frame)
        order_config_frame.pack(fill=tk.X, pady=5, before=self.order_tree)
        
        ttk.Label(order_config_frame, text="Table #:").pack(side=tk.LEFT, padx=5)
        self.table_number = ttk.Entry(order_config_frame, width=5)
        self.table_number.pack(side=tk.LEFT, padx=5)
        
        # group people control
        self.group_control_frame = ttk.Frame(order_config_frame)
        self.group_control_frame.pack(side=tk.LEFT, padx=10)
        
        ttk.Label(self.group_control_frame, text="人數:").pack(side=tk.LEFT, padx=5)
        self.people_count = tk.IntVar(value=1)
        self.people_count_label = ttk.Label(self.group_control_frame, textvariable=self.people_count)
        self.people_count_label.pack(side=tk.LEFT, padx=5)
        
        self.add_person_btn = ttk.Button(self.group_control_frame, text="+", width=2)
        self.add_person_btn.pack(side=tk.LEFT, padx=2)
        
        self.remove_person_btn = ttk.Button(self.group_control_frame, text="-", width=2)
        self.remove_person_btn.pack(side=tk.LEFT, padx=2)

        # add new person number
        self.current_person = tk.IntVar(value=1)
        ttk.Label(self.group_control_frame, text="choose person:").pack(side=tk.LEFT, padx=5)
        self.person_spinbox = ttk.Spinbox(
            self.group_control_frame, 
            from_=1, 
            to=1, 
            width=5,
            textvariable=self.current_person
        )
        self.person_spinbox.pack(side=tk.LEFT, padx=5)
        
        # Buttons
        self.button_frame = ttk.Frame(self.order_frame)
        self.button_frame.pack(fill=tk.X, pady=5)
        
        self.add_button = ttk.Button(self.button_frame, text="Add to Order")
        self.add_button.pack(side=tk.LEFT, padx=5)
        
        self.clear_button = ttk.Button(self.button_frame, text="Clear Order")
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        self.checkout_button = ttk.Button(self.button_frame, text="Checkout")
        self.checkout_button.pack(side=tk.LEFT, padx=5)

        self.split_bill_button = ttk.Button(self.button_frame, text="Split Bill")
        self.split_bill_button.pack(side=tk.LEFT, padx=5)

    def update_individual_tabs(self, num_people):
        """Update personal order paging"""
        # Remove an existing personal page
        for tab in list(self.individual_trees.keys()):
            if tab not in [f"Person {i+1}" for i in range(num_people)]:
                self.order_notebook.forget(self.individual_trees[tab]['frame'])
                del self.individual_trees[tab]
        
        # Add or update a personal page
        for i in range(num_people):
            person_name = f"Person {i+1}"
            if person_name not in self.individual_trees:
                # Create a new page
                person_frame = ttk.Frame(self.order_notebook)
                self.order_notebook.add(person_frame, text=person_name)
                
                # Create the treeview for this page
                person_tree = ttk.Treeview(person_frame, columns=('Name', 'Quantity', 'Price'), show='headings')
                person_tree.pack(fill=tk.BOTH, expand=True)
                
                person_tree.heading('Name', text='Name')
                person_tree.heading('Quantity', text='Quantity')
                person_tree.heading('Price', text='Price')
                
                # Save reference
                self.individual_trees[person_name] = {
                    'frame': person_frame,
                    'tree': person_tree
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
                    # Clear existing item
                    for item in tree.get_children():
                        tree.delete(item)
                    # Add New Item
                    for item, quantity in items:
                        tree.insert('', 'end', values=(item.name, quantity, f"${item.price * quantity:.2f}"))
        
        self.total_label.config(text=f"Total: ${total:.2f}")

    def add_person(self):
        current_count = self.sub_order_count.get()
        self.sub_order_count.set(current_count + 1)

    def remove_person(self):
        current_count = self.sub_order_count.get()
        if current_count > 1:
            self.sub_order_count.set(current_count - 1)

    def toggle_group_order(self):
        if self.is_group_order.get():
            self.sub_order_frame.pack(after=self.table_number.master, fill=tk.X, pady=5)
        else:
            self.sub_order_frame.pack_forget()

    def set_menu_items(self, items):
        for item in self.menu_tree.get_children():
            self.menu_tree.delete(item)
        for item in items:
            self.menu_tree.insert('', 'end', values=(item.id, item.name, f"${item.price:.2f}", item.category))

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
        
        #sub_bills
        for i, (items, subtotal) in enumerate(split_bills, 1):
            frame = ttk.LabelFrame(scrollable_frame, text=f"Person {i}")
            frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
            
            if not items:  # Check if there is a item
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
            
            #Set column width
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
        self.current_order = Order()

        # Bind Events
        self.view.add_button.config(command=self.add_to_order)
        self.view.clear_button.config(command=self.clear_order)
        self.view.checkout_button.config(command=self.checkout)
        self.view.split_bill_button.config(command=self.split_bill)
        self.view.add_person_btn.config(command=self.add_person)
        self.view.remove_person_btn.config(command=self.remove_person)

        # Initialize order
        self.reset_order()
        
        # Initialize menu display
        self.view.set_menu_items(self.model.get_menu_items())
        
        # Update the number of people to select
        self.update_person_spinbox_range()

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
        """Update all order display"""
        all_items = self.current_order.get_all_items()
        split_bills = self.current_order.get_split_bills()
        self.view.update_order_display(all_items, self.current_order.total, split_bills)        

    def update_person_spinbox_range(self):
        current_count = self.view.people_count.get()
        self.view.person_spinbox.config(from_=1, to=current_count)
        if self.view.current_person.get() > current_count:
            self.view.current_person.set(current_count)

    def add_to_order(self):
        selected_item = self.view.menu_tree.selection()
        if not selected_item:
            self.view.show_message("Please select the menu item.")
            return

        item_id = int(self.view.menu_tree.item(selected_item)['values'][0])
        menu_item = self.model.get_item_by_id(item_id)

        if menu_item:
            people_count = self.view.people_count.get()
            if people_count > 1:
                current_person = self.view.current_person.get() - 1
                self.current_order.add_item(menu_item, sub_order_index=current_person)
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
        self.view.people_count.set(1)  # reset people
        self.update_person_spinbox_range()

    def checkout(self):
        if not self.current_order.get_all_items():
            self.view.show_message("The order is empty")
            return

        table_info = f" for table {self.current_order.table_number}" if self.current_order.table_number else ""
        group_info = " (Group order)" if self.current_order.is_group_order() else ""

        self.view.show_message(f"Order{table_info}{group_info} completed! Total: ${self.current_order.total:.2f}")
        self.clear_order()

#main
def main():
    root = tk.Tk()
    model = MenuModel()
    view = POSView(root)
    controller = POSController(model, view)
    root.mainloop()

if __name__ == "__main__":
    main()
