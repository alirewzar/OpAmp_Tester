import tkinter as tk
from tkinter import ttk
import math

# Function to calculate CMRR
def calculate_cmrr():
    try:
        vout1_mv = float(entry_vout1.get())
        vout2_mv = float(entry_vout2.get())
        r6 = float(entry_r6.get())
        r2 = float(entry_r2.get())

        vout1 = vout1_mv / 1000  # Convert from mV to V
        vout2 = vout2_mv / 1000  # Convert from mV to V
        delta_vout = abs(vout1 - vout2)

        gain = (r6 / r2 + 1) * 20
        cmrr = 20 * math.log10(gain / delta_vout)
        result_var.set(f"CMRR = {cmrr:.2f} dB")
    except ValueError:
        result_var.set("Invalid input")
    except ZeroDivisionError:
        result_var.set("∆V_out cannot be 0")

# Create the main window
root = tk.Tk()
root.title("CMRR Calculator")
root.configure(bg='black')
root.geometry("450x450")

# Style configuration
style = ttk.Style()
style.theme_use("default")
style.configure("TLabel", background="black", foreground="white", font=("Arial", 14))
style.configure("TButton", background="black", foreground="white", font=("Arial", 12))
style.configure("TEntry", fieldbackground="black", foreground="white", font=("Arial", 12))

# Input fields
fields = [
    ("Vout1 (mV):", "0.0"),
    ("Vout2 (mV):", "10.0"),
    ("R6 (Ohms):", "99800"),
    ("R2 (Ohms):", "120.3"),
]

entries = []

for label_text, default in fields:
    label = ttk.Label(root, text=label_text)
    label.pack(pady=(10, 0))
    entry = ttk.Entry(root)
    entry.insert(0, default)
    entry.pack(pady=(0, 5))
    entries.append(entry)

entry_vout1, entry_vout2, entry_r6, entry_r2 = entries

# Result label
result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var, font=("Arial", 16, "bold"))
result_label.pack(pady=20)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate CMRR", command=calculate_cmrr)
calculate_button.pack(pady=15)

# Run the app
root.mainloop()