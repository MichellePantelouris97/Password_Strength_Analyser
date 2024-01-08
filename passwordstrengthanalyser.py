import tkinter as tk
from tkinter import ttk, messagebox
import re

class PasswordAnalyser:
    def __init__(self, master):
        self.master = master
        master.title("Password Analyser")

        # Set the background colour to teal
        master.configure(bg="#008080")

        # Remove the window icon
        master.iconbitmap(default="")

        self.create_widgets()

    def create_widgets(self):
        # Header 
        header_label = ttk.Label(self.master, text="Analyse Password Strength", font=("Helvetica", 16, "bold"), background="#008080", foreground="black")
        header_label.pack(pady=20)

        # Password Entry
        self.password_entry = ttk.Entry(self.master, show="•", font=("Helvetica", 12), style="Teal.TEntry")
        self.password_entry.pack(pady=10, ipadx=10, ipady=10)

        # Analyse Button
        analyze_button = ttk.Button(self.master, text="Analyse", command=self.analyse_password, style="Teal.TButton")
        analyze_button.pack(pady=20)

        # Modern style using themed Tkinter
        style = ttk.Style()
        style.configure("Teal.TEntry", foreground="black", background="#008080")
        style.configure("Teal.TButton", font=("Helvetica", 12, "bold"), padding=10, foreground="black", background="#008080")

    def analyse_password(self):
        password = self.password_entry.get()
        result = self.password_analyser(password)
        self.display_result(result)

    def password_analyser(self, password):
        # Password analysis requirements
        check_length_of_password = len(password) >= 8
        uppercase__character_checker = any(char.isupper() for char in password)
        lowercase__character_checker = any(char.islower() for char in password)
        numerical_character_checker = any(char.isdigit() for char in password)
        special_character_checker = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]_-', password))

        strength = "Strong" if all([check_length_of_password, uppercase__character_checker, lowercase__character_checker, numerical_character_checker, special_character_checker]) else "Weak"

        feedback = {
            "Length Check": check_length_of_password,
            "Uppercase Check": uppercase__character_checker,
            "Lowercase Check": lowercase__character_checker,
            "Digit Check": numerical_character_checker,
            "Special Character Check": special_character_checker,
            "Overall Strength": strength
        }

        return feedback

    def display_result(self, result):
        # Display result in a messagebox
        result_text = "\n".join([f"{key}: {'✔' if value else '❌'}" for key, value in result.items()])
        messagebox.showinfo("Analysis Result", f"Password Analysis:\n\n{result_text}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordAnalyser(root)
    root.mainloop()
