import tkinter as tk
from tkinter import messagebox
import re


class PasswordStrengthChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Password Complexity Checker")
        self.root.geometry("500x420")
        self.root.config(bg="#1e1e2f")

        # Title Label
        tk.Label(root, text="Password Strength Checker", font=("Helvetica", 16, "bold"),
                 bg="#1e1e2f", fg="#00FFFF").pack(pady=15)

        # Instruction Label
        tk.Label(root, text="Enter your password below:", bg="#1e1e2f", fg="white",
                 font=("Arial", 12)).pack(pady=5)

        # Password Entry
        self.password_entry = tk.Entry(root, show="*", font=("Arial", 14), width=30, justify="center")
        self.password_entry.pack(pady=10)

        # Checkbox to Show/Hide Password
        self.show_password_var = tk.BooleanVar()
        show_password_checkbox = tk.Checkbutton(
            root, text="Show Password", variable=self.show_password_var,
            command=self.toggle_password_visibility, bg="#1e1e2f",
            fg="white", selectcolor="#1e1e2f", font=("Arial", 10)
        )
        show_password_checkbox.pack(pady=5)

        # Button to check strength
        tk.Button(root, text="Check Strength", command=self.check_password_strength,
                  bg="#2196F3", fg="white", font=("Arial", 12), width=15).pack(pady=10)

        # Feedback Label
        self.strength_label = tk.Label(root, text="", bg="#1e1e2f", fg="white",
                                       font=("Arial", 12, "bold"))
        self.strength_label.pack(pady=10)

        # Tips Section
        self.tips_label = tk.Label(root, text="", bg="#1e1e2f", fg="#FFD700",
                                   font=("Arial", 10), justify="left", wraplength=450)
        self.tips_label.pack(pady=10)

        # Show Entered Password Label
        self.entered_password_label = tk.Label(root, text="", bg="#1e1e2f", fg="#00FFFF",
                                               font=("Arial", 11, "italic"))
        self.entered_password_label.pack(pady=5)

    def toggle_password_visibility(self):
        """Show or hide the password text"""
        if self.show_password_var.get():
            self.password_entry.config(show="")  # Show password
        else:
            self.password_entry.config(show="*")  # Hide password

    def check_password_strength(self):
        password = self.password_entry.get()
        self.entered_password_label.config(text=f"Entered Password: {password}")

        if not password:
            messagebox.showerror("Error", "Please enter a password!")
            return

        score = 0
        tips = []

        # Check criteria
        if len(password) >= 8:
            score += 1
        else:
            tips.append("❌ Use at least 8 characters.")

        if re.search(r"[A-Z]", password):
            score += 1
        else:
            tips.append("❌ Add at least one uppercase letter.")

        if re.search(r"[a-z]", password):
            score += 1
        else:
            tips.append("❌ Add at least one lowercase letter.")

        if re.search(r"[0-9]", password):
            score += 1
        else:
            tips.append("❌ Add at least one number.")

        if re.search(r"[@$!%*?&#^]", password):
            score += 1
        else:
            tips.append("❌ Add at least one special character (@, #, $, etc.)")

        # Determine strength
        if score <= 2:
            strength = "Weak 🔴"
            color = "red"
        elif score == 3 or score == 4:
            strength = "Moderate 🟡"
            color = "orange"
        else:
            strength = "Strong 🟢"
            color = "green"

        # Display results
        self.strength_label.config(text=f"Password Strength: {strength}", fg=color)

        if score < 5:
            self.tips_label.config(text="\n".join(tips))
        else:
            self.tips_label.config(text="✅ Excellent! Your password is strong and secure.")

        # Optional popup for weak passwords
        if score <= 2:
            messagebox.showwarning("Weak Password", "Your password is weak! Please make it stronger.")


def main():
    root = tk.Tk()
    app = PasswordStrengthChecker(root)
    root.mainloop()


if __name__ == "__main__":
    main()
