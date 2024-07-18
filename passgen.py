import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

def generate_password():
    length = length_var.get()
    try:
        length = int(length)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")
        return
    
    if length <= 0:
        messagebox.showerror("Error", "Password length should be greater than zero.")
        return
    
    characters = ""
    if uppercase_var.get():
        characters += string.ascii_uppercase
    if lowercase_var.get():
        characters += string.ascii_lowercase
    if digits_var.get():
        characters += string.digits
    if punctuation_var.get():
        characters += string.punctuation
    
    if not characters:
        messagebox.showerror("Error", "Please select at least one character set.")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    password_var.set(password)

def copy_to_clipboard():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Password Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

root = tk.Tk()
root.title("Password Generator")

style = ttk.Style()
style.configure('TFrame', background='#f0f0f0')
style.configure('TButton', font=('Arial', 12))
style.configure('TCheckbutton', font=('Arial', 12))
style.configure('TLabel', font=('Arial', 12))

length_var = tk.StringVar()
password_var = tk.StringVar()

main_frame = ttk.Frame(root, padding=(20, 10))
main_frame.grid(row=0, column=0, sticky='nsew')

length_label = ttk.Label(main_frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
length_entry = ttk.Entry(main_frame, textvariable=length_var, width=10)
length_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

uppercase_var = tk.BooleanVar()
uppercase_checkbox = ttk.Checkbutton(main_frame, text="Uppercase", variable=uppercase_var, style='TCheckbutton')
uppercase_checkbox.grid(row=1, column=0, padx=10, pady=5, sticky='w')

lowercase_var = tk.BooleanVar()
lowercase_checkbox = ttk.Checkbutton(main_frame, text="Lowercase", variable=lowercase_var, style='TCheckbutton')
lowercase_checkbox.grid(row=2, column=0, padx=10, pady=5, sticky='w')

digits_var = tk.BooleanVar()
digits_checkbox = ttk.Checkbutton(main_frame, text="Digits", variable=digits_var, style='TCheckbutton')
digits_checkbox.grid(row=3, column=0, padx=10, pady=5, sticky='w')

punctuation_var = tk.BooleanVar()
punctuation_checkbox = ttk.Checkbutton(main_frame, text="Punctuation", variable=punctuation_var, style='TCheckbutton')
punctuation_checkbox.grid(row=4, column=0, padx=10, pady=5, sticky='w')

generate_button = ttk.Button(main_frame, text="Generate Password", command=generate_password, style='TButton')
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

copy_button = ttk.Button(main_frame, text="Copy to Clipboard", command=copy_to_clipboard, style='TButton')
copy_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

password_label = ttk.Label(main_frame, text="Generated Password:")
password_label.grid(row=7, column=0, padx=10, pady=5, sticky='w')

password_entry = ttk.Entry(main_frame, textvariable=password_var, width=30, state='readonly')
password_entry.grid(row=7, column=1, padx=10, pady=5, sticky='w')

root.mainloop()
