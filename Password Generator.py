import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        self.root.config(bg='#2c3e50')

        
        self.title_label = tk.Label(
            root, text="Password Generator", font=('Helvetica', 18, 'bold'), bg='#2c3e50', fg='#ecf0f1')
        self.title_label.pack(pady=10)

       
        self.length_label = tk.Label(
            root, text="Password Length:", font=('Helvetica', 12), bg='#2c3e50', fg='#ecf0f1')
        self.length_label.pack(pady=5)
        self.length_entry = tk.Entry(
            root, width=10, font=('Helvetica', 12), bg='#ecf0f1', borderwidth=2, relief='groove')
        self.length_entry.pack(pady=5)

        
        self.complexity_var = tk.StringVar(value="Easy")

        self.easy_radio = tk.Radiobutton(
            root, text="Easy", variable=self.complexity_var, value="Easy", font=('Helvetica', 12), bg='#2c3e50', fg='#ecf0f1', selectcolor='#34495e')
        self.easy_radio.pack(pady=2)

        self.medium_radio = tk.Radiobutton(
            root, text="Medium", variable=self.complexity_var, value="Medium", font=('Helvetica', 12), bg='#2c3e50', fg='#ecf0f1', selectcolor='#34495e')
        self.medium_radio.pack(pady=2)

        self.strong_radio = tk.Radiobutton(
            root, text="Strong", variable=self.complexity_var, value="Strong", font=('Helvetica', 12), bg='#2c3e50', fg='#ecf0f1', selectcolor='#34495e')
        self.strong_radio.pack(pady=2)

       
        self.generate_button = tk.Button(
            root, text="Generate Password", command=self.generate_password, bg='#27ae60', fg='#ecf0f1', font=('Helvetica', 14, 'bold'), bd=0, relief='ridge')
        self.generate_button.pack(pady=20)

        
        self.result_label = tk.Label(root, text="", bg='#2c3e50', fg='#ecf0f1', font=('Helvetica', 14, 'bold'))
        self.result_label.pack(pady=10)

    def generate_password(self):
        length = self.length_entry.get()
        if not length.isdigit():
            messagebox.showerror("Invalid input", "Password length must be a number.")
            return

        length = int(length)
        if length <= 0:
            messagebox.showerror("Invalid input", "Password length must be greater than 0.")
            return

        complexity = self.complexity_var.get()

        if complexity == "Easy":
            chars = string.ascii_lowercase
        elif complexity == "Medium":
            chars = string.ascii_letters + string.digits
        elif complexity == "Strong":
            chars = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(chars) for _ in range(length))
        self.result_label.config(text=password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
