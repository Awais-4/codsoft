import tkinter as tk
from tkinter import messagebox

class Todolist:
    def __init__(self, m):
        self.m = m
        self.m.title('Todo List')
        self.m.config(bg='lightgrey')
        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.m, text="Todo List", font=('Arial', 18), bg='lightgrey')
        title_label.pack(pady=10)

        self.te = tk.Entry(self.m, width=40, font=('Arial', 12), bg='white')
        self.te.pack(pady=10)

        self.addbtn = tk.Button(self.m, text='Add Task', command=self.add_task, bg='lightgreen', fg='black', font=('Arial', 12))
        self.addbtn.pack(pady=5)

        list_frame = tk.Frame(self.m)
        list_frame.pack(pady=10)

        self.tl = tk.Listbox(list_frame, width=50, height=10, font=('Arial', 12), bg='white')
        self.tl.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tl.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tl.yview)

        self.complete_button = tk.Button(self.m, text='Mark as Completed', command=self.comp, bg='lightgreen', fg='black', font=('Arial', 12))
        self.complete_button.pack(pady=5)

        self.delbtn = tk.Button(self.m, text='Remove Task', command=self.delt, bg='lightblue', fg='black', font=('Arial', 12))
        self.delbtn.pack(pady=5)

    def lb(self):
        self.tl.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            self.tl.insert(tk.END, f"{index}. {task}")

    def add_task(self):
        task = self.te.get().strip()
        if task:
            self.tasks.append(task)
            self.te.delete(0, tk.END)
            self.lb()
        else:
            messagebox.showwarning('Warning', 'Task cannot be empty')

    def comp(self):
        selected_task = self.tl.curselection()
        if selected_task:
            index = selected_task[0]
            if not self.tasks[index].startswith('[Completed]'):
                self.tasks[index] = f'[Completed] {self.tasks[index]}'
                self.lb()
        else:
            messagebox.showwarning('Warning', 'Please select a task to mark as completed')

    def delt(self):
        selected_task = self.tl.curselection()
        if selected_task:
            index = selected_task[0]
            del self.tasks[index]
            self.lb()
        else:
            messagebox.showwarning('Warning', 'Please select a task to delete')

def main():
    root = tk.Tk()
    app = Todolist(root)
    root.mainloop()

if __name__ == '__main__':
    main()
