#VIP Customers (Enlgish)

import tkinter as tk
from tkinter import messagebox
import random

# Sample user accounts (user_id -> {name, balance})
accounts = {
    "user001": {"name": "Alice", "balance": 100.0},
    "user002": {"name": "Bob", "balance": 50.0},
}

# Special drink combo codes (each drink has a unique code that changes after use)
special_drinks = {
    "Special Beer": {"code": "1234", "is_used": False},
    "Special Cocktail": {"code": "5678", "is_used": False},
}

# Current logged-in user
current_user = None

def login():
    global current_user
    user_id = entry_user_id.get()
    
    if user_id in accounts:
        current_user = user_id
        label_welcome.config(text=f"Welcome, {accounts[user_id]['name']}!")
        button_login.config(state="disabled")
        button_logout.config(state="normal")
        button_order_food.config(state="normal")
        button_view_balance.config(state="normal")
        button_special_drinks.config(state="normal")
        button_add_to_account.config(state="normal")
    else:
        messagebox.showerror("Login Error", "User ID not found!")

def logout():
    global current_user
    current_user = None
    label_welcome.config(text="Please log in")
    button_login.config(state="normal")
    button_logout.config(state="disabled")
    button_order_food.config(state="disabled")
    button_view_balance.config(state="disabled")
    button_special_drinks.config(state="disabled")
    button_add_to_account.config(state="disabled")

def view_balance():
    if current_user:
        balance = accounts[current_user]["balance"]
        messagebox.showinfo("Account Balance", f"Your balance is: ${balance}")
    else:
        messagebox.showerror("Error", "Please log in first!")

def order_food():
    if current_user:
        menu_items = ["Burger ($10)", "Pizza ($15)", "Fries ($5)"]
        item = random.choice(menu_items)  # Random food item for simplicity
        price = int(item.split('($')[1].split(')')[0])
        accounts[current_user]["balance"] -= price
        messagebox.showinfo("Order Confirmation", f"You ordered: {item}")
    else:
        messagebox.showerror("Error", "Please log in first!")

def special_drinks():
    if current_user:
        # Code for fetching a special drink (requires combination lock)
        drink = random.choice(list(special_drinks.keys()))
        code = special_drinks[drink]["code"]
        user_code = simpledialog.askstring("Enter Code", f"Enter code for {drink}:")
        
        if user_code == code:
            special_drinks[drink]["is_used"] = True
            messagebox.showinfo("Special Drink", f"You have successfully fetched {drink}!")
        else:
            messagebox.showerror("Incorrect Code", "Wrong code entered!")
    else:
        messagebox.showerror("Error", "Please log in first!")

def add_to_account():
    if current_user:
        amount = simpledialog.askfloat("Add Funds", "Enter the amount to add to your account:")
        if amount and amount > 0:
            accounts[current_user]["balance"] += amount
            messagebox.showinfo("Account Updated", f"Your new balance is: ${accounts[current_user]['balance']}")
        else:
            messagebox.showerror("Invalid Amount", "Please enter a valid amount!")
    else:
        messagebox.showerror("Error", "Please log in first!")

# Set up the main window
root = tk.Tk()
root.title("VIP Bar Ordering System")
root.geometry("400x400")

# Label for welcome message
label_welcome = tk.Label(root, text="Please log in", font=("Arial", 14))
label_welcome.pack(pady=20)

# User ID input and login button
label_user_id = tk.Label(root, text="Enter your User ID:")
label_user_id.pack(pady=5)
entry_user_id = tk.Entry(root)
entry_user_id.pack(pady=5)

button_login = tk.Button(root, text="Login", command=login)
button_login.pack(pady=10)

# Logout button (initially disabled)
button_logout = tk.Button(root, text="Logout", command=logout, state="disabled")
button_logout.pack(pady=5)

# Other action buttons (initially disabled)
button_order_food = tk.Button(root, text="Order Food", command=order_food, state="disabled")
button_order_food.pack(pady=5)

button_view_balance = tk.Button(root, text="View Balance", command=view_balance, state="disabled")
button_view_balance.pack(pady=5)

button_special_drinks = tk.Button(root, text="Fetch Special Drink", command=special_drinks, state="disabled")
button_special_drinks.pack(pady=5)

button_add_to_account = tk.Button(root, text="Add to Account", command=add_to_account, state="disabled")
button_add_to_account.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()


#(VIP Customer Swedish)

import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# Exempel på användarkonton (user_id -> {name, balance})
konton = {
    "user001": {"namn": "Alice", "saldo": 100.0},
    "user002": {"namn": "Bob", "saldo": 50.0},
}

# Specialdrycker med kod (varje dryck har en unik kod som ändras efter användning)
specialdrycker = {
    "Specialöl": {"kod": "1234", "använd": False},
    "Specialcocktail": {"kod": "5678", "använd": False},
}

# Aktuell inloggad användare
aktuell_anvandare = None

def logga_in():
    global aktuell_anvandare
    anvandare_id = entry_anvandare_id.get()
    
    if anvandare_id in konton:
        aktuell_anvandare = anvandare_id
        label_valkommen.config(text=f"Välkommen, {konton[anvandare_id]['namn']}!")
        button_logga_in.config(state="disabled")
        button_logga_utm.config(state="normal")
        button_bestalla_mat.config(state="normal")
        button_saldo.config(state="normal")
        button_specialdrycker.config(state="normal")
        button_lagg_till_pengar.config(state="normal")
    else:
        messagebox.showerror("Inloggningsfel", "Användar-ID ej funnet!")

def logga_utm():
    global aktuell_anvandare
    aktuell_anvandare = None
    label_valkommen.config(text="Vänligen logga in")
    button_logga_in.config(state="normal")
    button_logga_utm.config(state="disabled")
    button_bestalla_mat.config(state="disabled")
    button_saldo.config(state="disabled")
    button_specialdrycker.config(state="disabled")
    button_lagg_till_pengar.config(state="disabled")

def visa_saldo():
    if aktuell_anvandare:
        saldo = konton[aktuell_anvandare]["saldo"]
        messagebox.showinfo("Kontosaldo", f"Ditt saldo är: ${saldo}")
    else:
        messagebox.showerror("Fel", "Vänligen logga in först!")

def bestalla_mat():
    if aktuell_anvandare:
        menyartiklar = ["Hamburgare ($10)", "Pizza ($15)", "Pommes frites ($5)"]
        item = random.choice(menyartiklar)  # Slumpmässig matartikel för enkelhetens skull
        pris = int(item.split('($')[1].split(')')[0])
        konton[aktuell_anvandare]["saldo"] -= pris
        messagebox.showinfo("Beställningsbekräftelse", f"Du har beställt: {item}")
    else:
        messagebox.showerror("Fel", "Vänligen logga in först!")

def specialdrycker():
    if aktuell_anvandare:
        # Kod för att hämta en specialdryck (kräver kombinationslås)
        dryck = random.choice(list(specialdrycker.keys()))
        kod = specialdrycker[dryck]["kod"]
        anvandar_kod = simpledialog.askstring("Ange kod", f"Ange kod för {dryck}:")
        
        if anvandar_kod == kod:
            specialdrycker[dryck]["använd"] = True
            messagebox.showinfo("Specialdryck", f"Du har framgångsrikt hämtat {dryck}!")
        else:
            messagebox.showerror("Fel kod", "Fel kod angiven!")
    else:
        messagebox.showerror("Fel", "Vänligen logga in först!")

def lagg_till_pengar():
    if aktuell_anvandare:
        belopp = simpledialog.askfloat("Lägg till pengar", "Ange beloppet du vill lägga till på ditt konto:")
        if belopp and belopp > 0:
            konton[aktuell_anvandare]["saldo"] += belopp
            messagebox.showinfo("Konto uppdaterat", f"Ditt nya saldo är: ${konton[aktuell_anvandare]['saldo']}")
        else:
            messagebox.showerror("Ogiltigt belopp", "Vänligen ange ett giltigt belopp!")
    else:
        messagebox.showerror("Fel", "Vänligen logga in först!")

# Skapa huvudfönstret
root = tk.Tk()
root.title("VIP Bar Beställningssystem")
root.geometry("400x400")

# Label för välkomstmeddelande
label_valkommen = tk.Label(root, text="Vänligen logga in", font=("Arial", 14))
label_valkommen.pack(pady=20)

# Användar-ID inmatning och logga in knapp
label_anvandare_id = tk.Label(root, text="Ange ditt Användar-ID:")
label_anvandare_id.pack(pady=5)
entry_anvandare_id = tk.Entry(root)
entry_anvandare_id.pack(pady=5)

button_logga_in = tk.Button(root, text="Logga in", command=logga_in)
button_logga_in.pack(pady=10)

# Logga ut knapp (initialt inaktiverad)
button_logga_utm = tk.Button(root, text="Logga ut", command=logga_utm, state="disabled")
button_logga_utm.pack(pady=5)

# Andra åtgärdsknappar (initialt inaktiverade)
button_bestalla_mat = tk.Button(root, text="Beställ mat", command=bestalla_mat, state="disabled")
button_bestalla_mat.pack(pady=5)

button_saldo = tk.Button(root, text="Visa saldo", command=visa_saldo, state="disabled")
button_saldo.pack(pady=5)

button_specialdrycker = tk.Button(root, text="Hämta specialdryck", command=specialdrycker, state="disabled")
button_specialdrycker.pack(pady=5)

button_lagg_till_pengar = tk.Button(root, text="Lägg till pengar", command=lagg_till_pengar, state="disabled")
button_lagg_till_pengar.pack(pady=5)

# Kör Tkinter event loop
root.mainloop()

#(VIP Customer Mandarin)

import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# 示例用户账户 (user_id -> {name, balance})
账户 = {
    "user001": {"姓名": "Alice", "余额": 100.0},
    "user002": {"姓名": "Bob", "余额": 50.0},
}

# 特殊饮品组合代码 (每种饮品有一个独特的代码，使用后会改变)
特殊饮品 = {
    "特饮啤酒": {"代码": "1234", "已用": False},
    "特饮鸡尾酒": {"代码": "5678", "已用": False},
}

# 当前登录的用户
当前用户 = None

def 登录():
    global 当前用户
    用户id = entry_用户id.get()
    
    if 用户id in 账户:
        当前用户 = 用户id
        label_欢迎.config(text=f"欢迎, {账户[用户id]['姓名']}!")
        button_登录.config(state="disabled")
        button_登出.config(state="normal")
        button_点餐.config(state="normal")
        button_余额.config(state="normal")
        button_特殊饮品.config(state="normal")
        button_充值.config(state="normal")
    else:
        messagebox.showerror("登录错误", "用户ID未找到!")

def 登出():
    global 当前用户
    当前用户 = None
    label_欢迎.config(text="请登录")
    button_登录.config(state="normal")
    button_登出.config(state="disabled")
    button_点餐.config(state="disabled")
    button_余额.config(state="disabled")
    button_特殊饮品.config(state="disabled")
    button_充值.config(state="disabled")

def 查看余额():
    if 当前用户:
        余额 = 账户[当前用户]["余额"]
        messagebox.showinfo("账户余额", f"您的余额是: ${余额}")
    else:
        messagebox.showerror("错误", "请先登录!")

def 点餐():
    if 当前用户:
        菜单项目 = ["汉堡 ($10)", "披萨 ($15)", "薯条 ($5)"]
        项目 = random.choice(菜单项目)  # 简单随机选择食物项
        价格 = int(项目.split('($')[1].split(')')[0])
        账户[当前用户]["余额"] -= 价格
        messagebox.showinfo("订单确认", f"您已点餐: {项目}")
    else:
        messagebox.showerror("错误", "请先登录!")

def 特殊饮品():
    if 当前用户:
        # 获取特殊饮品代码（需要输入组合锁）
        饮品 = random.choice(list(特殊饮品.keys()))
        代码 = 特殊饮品[饮品]["代码"]
        用户代码 = simpledialog.askstring("输入代码", f"请输入 {饮品} 的代码:")
        
        if 用户代码 == 代码:
            特殊饮品[饮品]["已用"] = True
            messagebox.showinfo("特殊饮品", f"您已成功获取 {饮品}!")
        else:
            messagebox.showerror("错误代码", "输入的代码不正确!")
    else:
        messagebox.showerror("错误", "请先登录!")

def 充值():
    if 当前用户:
        金额 = simpledialog.askfloat("充值", "请输入要充值的金额:")
        if 金额 and 金额 > 0:
            账户[当前用户]["余额"] += 金额
            messagebox.showinfo("账户更新", f"您的新余额是: ${账户[当前用户]['余额']}")
        else:
            messagebox.showerror("无效金额", "请输入有效的金额!")
    else:
        messagebox.showerror("错误", "请先登录!")

# 创建主窗口
root = tk.Tk()
root.title("VIP酒吧点餐系统")
root.geometry("400x400")

# 欢迎信息标签
label_欢迎 = tk.Label(root, text="请登录", font=("Arial", 14))
label_欢迎.pack(pady=20)

# 用户ID输入框和登录按钮
label_用户id = tk.Label(root, text="请输入您的用户ID:")
label_用户id.pack(pady=5)
entry_用户id = tk.Entry(root)
entry_用户id.pack(pady=5)

button_登录 = tk.Button(root, text="登录", command=登录)
button_登录.pack(pady=10)

# 登出按钮（初始状态为禁用）
button_登出 = tk.Button(root, text="登出", command=登出, state="disabled")
button_登出.pack(pady=5)

# 其他操作按钮（初始状态为禁用）
button_点餐 = tk.Button(root, text="点餐", command=点餐, state="disabled")
button_点餐.pack(pady=5)

button_余额 = tk.Button(root, text="查看余额", command=查看余额, state="disabled")
button_余额.pack(pady=5)

button_特殊饮品 = tk.Button(root, text="获取特殊饮品", command=特殊饮品, state="disabled")
button_特殊饮品.pack(pady=5)

button_充值 = tk.Button(root, text="充值", command=充值, state="disabled")
button_充值.pack(pady=5)

# 启动Tkinter事件循环
root.mainloop()

# (Bartender, Waiter and Waitress English)

import tkinter as tk
from tkinter import messagebox

# Sample users (bartender, waiter, waitress)
users = {
    "bartender01": {"name": "John", "role": "Bartender"},
    "waiter01": {"name": "Alice", "role": "Waiter"},
    "waitress01": {"name": "Emma", "role": "Waitress"}
}

# Sample menu items
menu = {
    "Beer": {"stock": 10},
    "Wine": {"stock": 5},
    "Cocktail": {"stock": 7},
    "Pizza": {"stock": 12},
}

# Current logged in user
current_user = None

# Function to log in
def log_in():
    global current_user
    user_id = entry_user_id.get()

    if user_id in users:
        current_user = user_id
        label_welcome.config(text=f"Welcome, {users[user_id]['name']} ({users[user_id]['role']})")
        button_log_in.config(state="disabled")
        button_log_out.config(state="normal")
        button_check_availability.config(state="normal")
        button_remove_item.config(state="normal")
    else:
        messagebox.showerror("Login Error", "User ID not found!")

# Function to log out
def log_out():
    global current_user
    current_user = None
    label_welcome.config(text="Please log in")
    button_log_in.config(state="normal")
    button_log_out.config(state="disabled")
    button_check_availability.config(state="disabled")
    button_remove_item.config(state="disabled")

# Function to check availability of products
def check_availability():
    if current_user:
        availability_message = "Product Availability:\n"
        for item, details in menu.items():
            availability_message += f"{item}: {details['stock']} left\n"
        messagebox.showinfo("Product Availability", availability_message)
    else:
        messagebox.showerror("Error", "Please log in first!")

# Function to remove a product temporarily from the menu
def remove_item():
    if current_user:
        item_to_remove = entry_remove_item.get()
        
        if item_to_remove in menu:
            menu[item_to_remove]["stock"] = 0  # Temporarily remove item by setting stock to 0
            messagebox.showinfo("Item Removed", f"{item_to_remove} has been temporarily removed from the menu.")
            check_for_low_stock(item_to_remove)
        else:
            messagebox.showerror("Error", f"{item_to_remove} is not on the menu.")
    else:
        messagebox.showerror("Error", "Please log in first!")

# Function to check if any item is running low
def check_for_low_stock(item):
    if menu[item]["stock"] <= 3:  # Notify if stock is 3 or less
        messagebox.showwarning("Low Stock Warning", f"Warning: {item} is running low on stock!")

# Create the main window
root = tk.Tk()
root.title("Bar System - Bartender, Waiter, and Waitress Login")
root.geometry("400x400")

# Welcome label
label_welcome = tk.Label(root, text="Please log in", font=("Arial", 14))
label_welcome.pack(pady=20)

# User ID input and login button
label_user_id = tk.Label(root, text="Enter your User ID:")
label_user_id.pack(pady=5)
entry_user_id = tk.Entry(root)
entry_user_id.pack(pady=5)

button_log_in = tk.Button(root, text="Log In", command=log_in)
button_log_in.pack(pady=10)

# Log out button (initially disabled)
button_log_out = tk.Button(root, text="Log Out", command=log_out, state="disabled")
button_log_out.pack(pady=5)

# Check availability button (initially disabled)
button_check_availability = tk.Button(root, text="Check Product Availability", command=check_availability, state="disabled")
button_check_availability.pack(pady=5)

# Remove item input and button (initially disabled)
label_remove_item = tk.Label(root, text="Enter item to remove temporarily:")
label_remove_item.pack(pady=5)
entry_remove_item = tk.Entry(root)
entry_remove_item.pack(pady=5)

button_remove_item = tk.Button(root, text="Remove Item", command=remove_item, state="disabled")
button_remove_item.pack(pady=10)

# Run Tkinter event loop
root.mainloop()

# (Bartender, Waiter and Waitress Swedish)

import tkinter as tk
from tkinter import messagebox

# Exempel på användarkonton (bartender, servitör, servitris)
användare = {
    "bartender01": {"namn": "John", "roll": "Bartender"},
    "servitör01": {"namn": "Alice", "roll": "Servitör"},
    "servitris01": {"namn": "Emma", "roll": "Servitris"}
}

# Exempel på menyartiklar
meny = {
    "Öl": {"lager": 10},
    "Vin": {"lager": 5},
    "Cocktail": {"lager": 7},
    "Pizza": {"lager": 12},
}

# Aktuell inloggad användare
aktuell_användare = None

# Funktion för att logga in
def logga_in():
    global aktuell_användare
    användar_id = entry_användar_id.get()

    if användar_id in användare:
        aktuell_användare = användar_id
        label_välkommen.config(text=f"Välkommen, {användare[användar_id]['namn']} ({användare[användar_id]['roll']})")
        button_logga_in.config(state="disabled")
        button_logga_ut.config(state="normal")
        button_kontrollera_lager.config(state="normal")
        button_ta_bort_artikel.config(state="normal")
    else:
        messagebox.showerror("Inloggningsfel", "Användar-ID ej funnet!")

# Funktion för att logga ut
def logga_ut():
    global aktuell_användare
    aktuell_användare = None
    label_välkommen.config(text="Vänligen logga in")
    button_logga_in.config(state="normal")
    button_logga_ut.config(state="disabled")
    button_kontrollera_lager.config(state="disabled")
    button_ta_bort_artikel.config(state="disabled")

# Funktion för att kontrollera tillgången på produkter
def kontrollera_lager():
    if aktuell_användare:
        lager_meddelande = "Produkt tillgång:\n"
        for artikel, detaljer in meny.items():
            lager_meddelande += f"{artikel}: {detaljer['lager']} kvar\n"
        messagebox.showinfo("Produkt Tillgång", lager_meddelande)
    else:
        messagebox.showerror("Fel", "Vänligen logga in först!")

# Funktion för att tillfälligt ta bort en produkt från menyn
def ta_bort_artikel():
    if aktuell_användare:
        artikel_till_bort = entry_ta_bort_artikel.get()
        
        if artikel_till_bort in meny:
            meny[artikel_till_bort]["lager"] = 0  # Tillfälligt ta bort artikel genom att sätta lagret till 0
            messagebox.showinfo("Artikel Borttagen", f"{artikel_till_bort} har tillfälligt tagits bort från menyn.")
            kontrollera_lågt_lager(artikel_till_bort)
        else:
            messagebox.showerror("Fel", f"{artikel_till_bort} finns inte på menyn.")
    else:
        messagebox.showerror("Fel", "Vänligen logga in först!")

# Funktion för att kontrollera om en artikel har lågt lager
def kontrollera_lågt_lager(artikel):
    if meny[artikel]["lager"] <= 3:  # Skicka varning om lagret är 3 eller mindre
        messagebox.showwarning("Lågt Lager Varning", f"Varning: {artikel} har lågt lager!")

# Skapa huvudfönstret
root = tk.Tk()
root.title("Bar System - Bartender, Servitör och Servitris Inloggning")
root.geometry("400x400")

# Välkomstetikett
label_välkommen = tk.Label(root, text="Vänligen logga in", font=("Arial", 14))
label_välkommen.pack(pady=20)

# Användar-ID inmatning och logga in knapp
label_användar_id = tk.Label(root, text="Ange ditt Användar-ID:")
label_användar_id.pack(pady=5)
entry_användar_id = tk.Entry(root)
entry_användar_id.pack(pady=5)

button_logga_in = tk.Button(root, text="Logga in", command=logga_in)
button_logga_in.pack(pady=10)

# Logga ut knapp (initialt inaktiverad)
button_logga_ut = tk.Button(root, text="Logga ut", command=logga_ut, state="disabled")
button_logga_ut.pack(pady=5)

# Kontrollera lager knapp (initialt inaktiverad)
button_kontrollera_lager = tk.Button(root, text="Kontrollera Produkt Tillgång", command=kontrollera_lager, state="disabled")
button_kontrollera_lager.pack(pady=5)

# Ta bort artikel inmatning och knapp (initialt inaktiverad)
label_ta_bort_artikel = tk.Label(root, text="Ange artikel att ta bort tillfälligt:")
label_ta_bort_artikel.pack(pady=5)
entry_ta_bort_artikel = tk.Entry(root)
entry_ta_bort_artikel.pack(pady=5)

button_ta_bort_artikel = tk.Button(root, text="Ta Bort Artikel", command=ta_bort_artikel, state="disabled")
button_ta_bort_artikel.pack(pady=10)

# Starta Tkinter event loop
root.mainloop()

#(# (Bartender, Waiter and Waitress Mandarin)

import tkinter as tk
from tkinter import messagebox

# 示例用户账户（bartender, waiter, waitress）
用户 = {
    "bartender01": {"姓名": "John", "角色": "Bartender"},
    "waiter01": {"姓名": "Alice", "角色": "Waiter"},
    "waitress01": {"姓名": "Emma", "角色": "Waitress"}
}

# 示例菜单项
菜单 = {
    "啤酒": {"库存": 10},
    "葡萄酒": {"库存": 5},
    "鸡尾酒": {"库存": 7},
    "比萨": {"库存": 12},
}

# 当前登录的用户
当前用户 = None

# 登录功能
def 登录():
    global 当前用户
    用户id = entry_用户id.get()

    if 用户id in 用户:
        当前用户 = 用户id
        label_欢迎.config(text=f"欢迎, {用户[用户id]['姓名']} ({用户[用户id]['角色']})")
        button_登录.config(state="disabled")
        button_登出.config(state="normal")
        button_检查库存.config(state="normal")
        button_移除商品.config(state="normal")
    else:
        messagebox.showerror("登录错误", "用户ID未找到!")

# 登出功能
def 登出():
    global 当前用户
    当前用户 = None
    label_欢迎.config(text="请登录")
    button_登录.config(state="normal")
    button_登出.config(state="disabled")
    button_检查库存.config(state="disabled")
    button_移除商品.config(state="disabled")

# 检查商品库存功能
def 检查库存():
    if 当前用户:
        库存信息 = "商品库存:\n"
        for 商品, 详情 in 菜单.items():
            库存信息 += f"{商品}: {详情['库存']} 个剩余\n"
        messagebox.showinfo("商品库存", 库存信息)
    else:
        messagebox.showerror("错误", "请先登录!")

# 移除商品功能
def 移除商品():
    if 当前用户:
        要移除的商品 = entry_移除商品.get()
        
        if 要移除的商品 in 菜单:
            菜单[要移除的商品]["库存"] = 0  # 暂时移除商品，通过将库存设置为0
            messagebox.showinfo("商品移除", f"{要移除的商品} 已从菜单中移除。")
            检查库存不足(要移除的商品)
        else:
            messagebox.showerror("错误", f"{要移除的商品} 不在菜单中。")
    else:
        messagebox.showerror("错误", "请先登录!")

# 检查库存是否不足
def 检查库存不足(商品):
    if 菜单[商品]["库存"] <= 3:  # 如果库存小于等于3，则显示警告
        messagebox.showwarning("库存不足警告", f"警告: {商品} 库存不足!")

# 创建主窗口
root = tk.Tk()
root.title("酒吧系统 - Bartender, Waiter 和 Waitress 登录")
root.geometry("400x400")

# 欢迎标签
label_欢迎 = tk.Label(root, text="请登录", font=("Arial", 14))
label_欢迎.pack(pady=20)

# 用户ID输入框和登录按钮
label_用户id = tk.Label(root, text="请输入您的用户ID:")
label_用户id.pack(pady=5)
entry_用户id = tk.Entry(root)
entry_用户id.pack(pady=5)

button_登录 = tk.Button(root, text="登录", command=登录)
button_登录.pack(pady=10)

# 登出按钮（初始状态为禁用）
button_登出 = tk.Button(root, text="登出", command=登出, state="disabled")
button_登出.pack(pady=5)

# 检查库存按钮（初始状态为禁用）
button_检查库存 = tk.Button(root, text="检查商品库存", command=检查库存, state="disabled")
button_检查库存.pack(pady=5)

# 移除商品输入框和按钮（初始状态为禁用）
label_移除商品 = tk.Label(root, text="请输入要移除的商品:")
label_移除商品.pack(pady=5)
entry_移除商品 = tk.Entry(root)
entry_移除商品.pack(pady=5)

button_移除商品 = tk.Button(root, text="移除商品", command=移除商品, state="disabled")
button_移除商品.pack(pady=10)

# 启动Tkinter事件循环
root.mainloop()
