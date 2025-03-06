import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import sys
# Predefined user accounts
USER_CREDENTIALS = {
    "guest": "guest",
    "vipguest": "vipguest",
    "admin": "admin"
}

# Language dictionary
LANGUAGES = {
    "English": {"choose_language": "Choose Language:", "username": "Username:", "password": "Password:", "login": "Login", "logout": "Logout",
                 "guest_welcome": "Welcome, Guest! This is the guest interface.",
                 "vip_welcome": "Welcome, VIP Guest! This is the VIP interface.",
                 "admin_welcome": "Welcome, Admin! This is the admin interface.",
                 "login_failed": "Invalid username or password. Please try again."},
    "中文": {"choose_language": "選擇語言:", "username": "帳號:", "password": "密碼:", "login": "登入", "logout": "登出",
             "guest_welcome": "歡迎, Guest! 這是訪客介面。",
             "vip_welcome": "歡迎, VIP Guest! 這是VIP介面。",
             "admin_welcome": "歡迎, Admin! 這是管理員介面。",
             "login_failed": "帳號或密碼錯誤，請重試。"},
    "Svenska": {"choose_language": "Välj språk:", "username": "Användarnamn:", "password": "Lösenord:", "login": "Logga in", "logout": "Logga ut",
                 "guest_welcome": "Välkommen, Gäst! Detta är gästgränssnittet.",
                 "vip_welcome": "Välkommen, VIP Gäst! Detta är VIP-gränssnittet.",
                 "admin_welcome": "Välkommen, Admin! Detta är admin-gränssnittet.",
                 "login_failed": "Ogiltigt användarnamn eller lösenord. Försök igen."}
}

# Default language
current_lang = "English"

def change_language(*args):
    global current_lang
    current_lang = language_var.get()
    label_choose_language.config(text=LANGUAGES[current_lang]["choose_language"])
    label_username.config(text=LANGUAGES[current_lang]["username"])
    label_password.config(text=LANGUAGES[current_lang]["password"])
    btn_login.config(text=LANGUAGES[current_lang]["login"])



def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        frame_login.pack_forget()
        show_dashboard(username)
    else:
        messagebox.showerror("Login Failed", LANGUAGES[current_lang]["login_failed"])


    
def show_dashboard(username):
    root.withdraw()  
    if username == "guest":
        subprocess.run([sys.executable, "all_customer_order_interface.py"]) 
    elif username == "vipguest":
        subprocess.run([sys.executable, "vip_interface.py"])
    elif username == "admin":
       subprocess.run([sys.executable, "bartender_frontend.py"])
    
    root.destroy()

   

# Create the main application window
root = tk.Tk()
root.title("Login Interface")
root.geometry("1350x600")

# Create the login frame
frame_login = tk.Frame(root, padx=20, pady=20)
frame_login.pack()

# Language selection dropdown centered
frame_language = tk.Frame(frame_login)
frame_language.grid(row=0, column=0, columnspan=2, pady=10)

label_choose_language = tk.Label(frame_language, text=LANGUAGES[current_lang]["choose_language"])
label_choose_language.pack(side=tk.LEFT, padx=5)

language_var = tk.StringVar(root)
language_var.set(current_lang)  # Set default language
language_menu = tk.OptionMenu(frame_language, language_var, *LANGUAGES.keys(), command=change_language)
language_menu.pack(side=tk.LEFT)

# Username label and entry
label_username = tk.Label(frame_login, text=LANGUAGES[current_lang]["username"])
label_username.grid(row=1, column=0, padx=10, pady=10)
entry_username = tk.Entry(frame_login)
entry_username.grid(row=1, column=1, padx=10, pady=10)

# Password label and entry
label_password = tk.Label(frame_login, text=LANGUAGES[current_lang]["password"])
label_password.grid(row=2, column=0, padx=10, pady=10)
entry_password = tk.Entry(frame_login, show="*")  # Hide password input
entry_password.grid(row=2, column=1, padx=10, pady=10)

# Login button
btn_login = tk.Button(frame_login, text=LANGUAGES[current_lang]["login"], command=login)
btn_login.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
