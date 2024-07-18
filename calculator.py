import tkinter as tk
from tkinter import ttk

def button_click(event):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(event.widget.cget('text')))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expr = entry.get().replace('x', '*')
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('Clear', 5, 0), ('(', 5, 1), (')', 5, 2)
]

for (text, row, column) in buttons:
    button = ttk.Button(root, text=text, width=10)
    button.grid(row=row, column=column, padx=5, pady=5)
    button.bind('<Button-1>', button_click)

clear_button = ttk.Button(root, text='Clear', width=10, command=button_clear)
clear_button.grid(row=5, column=0, padx=5, pady=5)

equal_button = ttk.Button(root, text='=', width=22, command=button_equal)
equal_button.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
