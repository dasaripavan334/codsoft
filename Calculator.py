import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x500")
        self.root.config(bg='#34495e')

        
        self.display = tk.Entry(root, font=('Helvetica', 20), borderwidth=2, relief='groove', bg='#ecf0f1', fg='#2c3e50')
        self.display.pack(pady=20, padx=20, fill='both')

        
        self.button_frame = tk.Frame(root, bg='#34495e')
        self.button_frame.pack()

        
        self.create_number_buttons()

        
        self.create_operation_buttons()

       
        self.create_control_buttons()

    def create_number_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('0', 4, 1)
        ]
        for (text, row, col) in buttons:
            button = tk.Button(self.button_frame, text=text, width=5, height=2, command=lambda t=text: self.append_to_display(t), bg='#7f8c8d', fg='#ecf0f1', font=('Helvetica', 16, 'bold'), bd=0, relief='ridge')
            button.grid(row=row, column=col, padx=10, pady=10)

    def create_operation_buttons(self):
        operations = [
            ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3)
        ]
        for (text, row, col) in operations:
            button = tk.Button(self.button_frame, text=text, width=5, height=2, command=lambda t=text: self.append_to_display(t), bg='#27ae60', fg='#ecf0f1', font=('Helvetica', 16, 'bold'), bd=0, relief='ridge')
            button.grid(row=row, column=col, padx=10, pady=10)

    def create_control_buttons(self):
        clear_button = tk.Button(self.button_frame, text="C", width=5, height=2, command=self.clear_display, bg='#e74c3c', fg='#ecf0f1', font=('Helvetica', 16, 'bold'), bd=0, relief='ridge')
        clear_button.grid(row=4, column=0, padx=10, pady=10)

        equals_button = tk.Button(self.button_frame, text="=", width=5, height=2, command=self.calculate_result, bg='#f39c12', fg='#ecf0f1', font=('Helvetica', 16, 'bold'), bd=0, relief='ridge')
        equals_button.grid(row=4, column=2, padx=10, pady=10)

    def append_to_display(self, value):
        self.display.insert(tk.END, value)

    def clear_display(self):
        self.display.delete(0, tk.END)

    def calculate_result(self):
        try:
            result = eval(self.display.get())
            self.clear_display()
            self.display.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input\n{e}")
            self.clear_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()
