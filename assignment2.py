import tkinter as tk
from tkinter import messagebox

# BMI Calculation
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid Input", "Weight and height must be greater than zero.")
            return

        bmi = weight / (height ** 2)
        category = get_bmi_category(bmi)

        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# BMI Category Logic
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# GUI Setup
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x300")
window.configure(bg="#f7f7f7")

# UI Elements
tk.Label(window, text="Weight (kg):", font=("Arial", 12), bg="#f7f7f7").pack(pady=5)
entry_weight = tk.Entry(window, font=("Arial", 12))
entry_weight.pack(pady=5)

tk.Label(window, text="Height (m):", font=("Arial", 12), bg="#f7f7f7").pack(pady=5)
entry_height = tk.Entry(window, font=("Arial", 12))
entry_height.pack(pady=5)

tk.Button(window, text="Calculate BMI", font=("Arial", 12), command=calculate_bmi, bg="#4CAF50", fg="white").pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14), bg="#f7f7f7", fg="blue")
result_label.pack(pady=10)

window.mainloop()
