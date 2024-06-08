import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("500x500")

        self.user_score = 0
        self.computer_score = 0

        self.choices = ["Rock", "Paper", "Scissors"]

        self.create_widgets()

    def create_widgets(self):
       
        self.title_label = tk.Label(self.root, text="Rock-Paper-Scissors", font=('Helvetica', 24, 'bold'))
        self.title_label.pack(pady=20)

        
        self.user_score_label = tk.Label(self.root, text="Your Score: 0", font=('Helvetica', 14))
        self.user_score_label.pack(pady=10)
        self.computer_score_label = tk.Label(self.root, text="Computer Score: 0", font=('Helvetica', 14))
        self.computer_score_label.pack(pady=10)

       
        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play("Rock"), font=('Helvetica', 16, 'bold'))
        self.rock_button.pack(pady=10)
        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play("Paper"), font=('Helvetica', 16, 'bold'))
        self.paper_button.pack(pady=10)
        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play("Scissors"), font=('Helvetica', 16, 'bold'))
        self.scissors_button.pack(pady=10)

        
        self.result_label = tk.Label(self.root, text="", font=('Helvetica', 16, 'bold'))
        self.result_label.pack(pady=20)

        
        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.reset, font=('Helvetica', 16, 'bold'))
        self.play_again_button.pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)
        
        self.result_label.config(text=f"You chose {user_choice}, Computer chose {computer_choice}.\n{result}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"

        if (user_choice == "Rock" and computer_choice == "Scissors") or \
           (user_choice == "Scissors" and computer_choice == "Paper") or \
           (user_choice == "Paper" and computer_choice == "Rock"):
            self.user_score += 1
            self.user_score_label.config(text=f"Your Score: {self.user_score}")
            return "You win!"
        else:
            self.computer_score += 1
            self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")
            return "You lose!"

    def reset(self):
        self.result_label.config(text="")
        self.user_score = 0
        self.computer_score = 0
        self.user_score_label.config(text="Your Score: 0")
        self.computer_score_label.config(text="Computer Score: 0")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
