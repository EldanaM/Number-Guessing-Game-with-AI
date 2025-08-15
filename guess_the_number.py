import random
import tkinter as tk
from tkinter import ttk, messagebox

class NumberGuesserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game with AI")
        self.root.geometry("500x400")
        
        # Create tabs
        self.notebook = ttk.Notebook(root)
        self.tab1 = ttk.Frame(self.notebook)  
        self.tab2 = ttk.Frame(self.notebook)  
        self.notebook.add(self.tab1, text="Player vs AI")
        self.notebook.add(self.tab2, text="AI vs Player")
        self.notebook.pack(expand=True, fill="both")
        
        self.setup_player_vs_ai_tab()
        
        self.setup_ai_vs_player_tab()

    def setup_player_vs_ai_tab(self):
        self.ai_number = random.randint(1, 100)
        self.player_attempts = 0
        
        frame = ttk.Frame(self.tab1)
        frame.pack(pady=20)
        
        self.label = ttk.Label(frame, text="Guess a number between 1 and 100:")
        self.label.pack()
        
        self.entry = ttk.Entry(frame)
        self.entry.pack(pady=10)
        
        self.guess_button = ttk.Button(frame, text="Check", command=self.check_player_guess)
        self.guess_button.pack()
        
        self.hint_label = ttk.Label(frame, text="")
        self.hint_label.pack(pady=10)
        
        self.new_game_button = ttk.Button(frame, text="New Game", command=self.new_player_game)
        self.new_game_button.pack()

    def setup_ai_vs_player_tab(self):
        self.low = 1
        self.high = 100
        self.ai_attempts = 0
        
        frame = ttk.Frame(self.tab2)
        frame.pack(pady=20)
        
        self.ai_label = ttk.Label(frame, text="Think of a number between 1 and 100. AI will guess it.")
        self.ai_label.pack()
        
        self.ai_guess_label = ttk.Label(frame, text="")
        self.ai_guess_label.pack(pady=10)
        
        button_frame = ttk.Frame(frame)
        button_frame.pack()
        
        self.higher_button = ttk.Button(button_frame, text="Higher", command=lambda: self.process_ai_feedback("higher"))
        self.higher_button.pack(side="left", padx=5)
        
        self.correct_button = ttk.Button(button_frame, text="Correct", command=lambda: self.process_ai_feedback("correct"))
        self.correct_button.pack(side="left", padx=5)
        
        self.lower_button = ttk.Button(button_frame, text="Lower", command=lambda: self.process_ai_feedback("lower"))
        self.lower_button.pack(side="left", padx=5)
        
        self.new_ai_game_button = ttk.Button(frame, text="New Game", command=self.new_ai_game)
        self.new_ai_game_button.pack(pady=10)
    
        self.new_ai_game()

    def check_player_guess(self):
        try:
            guess = int(self.entry.get())
            self.player_attempts += 1
            
            if guess == self.ai_number:
                self.hint_label.config(text=f"Victory! You guessed in {self.player_attempts} attempts.")
                self.guess_button.config(state="disabled")
            elif guess < self.ai_number:
                self.hint_label.config(text="Higher!")
            else:
                self.hint_label.config(text="Lower!")
                
            self.entry.delete(0, "end")
        except ValueError:
            messagebox.showerror("Error", "Please enter a number!")

    def new_player_game(self):
        self.ai_number = random.randint(1, 100)
        self.player_attempts = 0
        self.hint_label.config(text="")
        self.entry.delete(0, "end")
        self.guess_button.config(state="normal")

    def new_ai_game(self):
        self.low = 1
        self.high = 100
        self.ai_attempts = 0
        self.ai_guess_label.config(text="")
        self.make_ai_guess()

    def make_ai_guess(self):
        self.ai_guess = (self.low + self.high) // 2
        self.ai_attempts += 1
        self.ai_guess_label.config(text=f"AI guesses: {self.ai_guess} (Attempt {self.ai_attempts})")

    def process_ai_feedback(self, feedback):
        if feedback == "correct":
            messagebox.showinfo("AI Wins", f"AI guessed your number in {self.ai_attempts} attempts!")
            self.new_ai_game()
        elif feedback == "higher":
            self.low = self.ai_guess + 1
            self.make_ai_guess()
        else:
            self.high = self.ai_guess - 1
            self.make_ai_guess()

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuesserApp(root)
    root.mainloop()