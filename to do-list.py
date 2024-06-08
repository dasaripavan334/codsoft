import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x400")
        self.root.config(bg='#f0f0f0')

        self.tasks = []

        self.frame = tk.Frame(self.root, bg='#f0f0f0')
        self.frame.pack(pady=20)

        self.listbox = tk.Listbox(
            self.frame, 
            width=40, 
            height=10, 
            selectmode=tk.SINGLE, 
            bg='#e0e0e0', 
            fg='#000000', 
            bd=0, 
            font=('Helvetica', 12),
            highlightthickness=0,
            selectbackground='#a6a6a6',
            activestyle="none"
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(
            self.root, 
            width=40, 
            font=('Helvetica', 12),
            bg='#ffffff', 
            fg='#000000', 
            borderwidth=2, 
            relief='groove'
        )
        self.entry.pack(pady=10)

        self.button_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.button_frame.pack(pady=10)

        self.add_task_btn = tk.Button(
            self.button_frame, 
            text="Add Task", 
            width=15, 
            command=self.add_task,
            bg='#81c784', 
            fg='#ffffff', 
            font=('Helvetica', 10, 'bold'), 
            bd=0, 
            relief='ridge'
        )
        self.add_task_btn.grid(row=0, column=0, padx=5)

        self.update_task_btn = tk.Button(
            self.button_frame, 
            text="Update Task", 
            width=15, 
            command=self.update_task,
            bg='#64b5f6', 
            fg='#ffffff', 
            font=('Helvetica', 10, 'bold'), 
            bd=0, 
            relief='ridge'
        )
        self.update_task_btn.grid(row=0, column=1, padx=5)

        self.delete_task_btn = tk.Button(
            self.button_frame, 
            text="Delete Task", 
            width=15, 
            command=self.delete_task,
            bg='#e57373', 
            fg='#ffffff', 
            font=('Helvetica', 10, 'bold'), 
            bd=0, 
            relief='ridge'
        )
        self.delete_task_btn.grid(row=1, column=0, padx=5, pady=5)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
            print("Added task:", task)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            new_task = self.entry.get()
            if new_task != "":
                self.tasks[selected_task_index] = new_task
                self.listbox.delete(selected_task_index)
                self.listbox.insert(selected_task_index, new_task)
                self.entry.delete(0, tk.END)
                print("Updated task at index", selected_task_index, "to", new_task)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            task = self.tasks.pop(selected_task_index)
            self.listbox.delete(selected_task_index)
            print("Deleted task:", task)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
