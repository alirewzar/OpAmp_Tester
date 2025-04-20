import tkinter as tk
from tkinter import ttk

# Function to calculate Vof
def calculate_vof():
    try:
        vout = float(entry_vout.get())
        r6 = float(entry_r6.get())
        r2 = float(entry_r2.get())

        vof = vout / ((r6 / r2) + 1)
        vof_mv = vof * 1000  # Convert to millivolts
        result_var.set(f"Vof = {vof_mv:.2f} mV")
    except ValueError:
        result_var.set("Invalid input")

# Create the main window
root = tk.Tk()
root.title("Vof Calculator")
root.configure(bg='black')
root.geometry("400x350")

# Style configuration
style = ttk.Style()
style.theme_use("default")
style.configure("TLabel", background="black", foreground="white", font=("Arial", 14))
style.configure("TButton", background="black", foreground="white", font=("Arial", 12))
style.configure("TEntry", fieldbackground="black", foreground="white", font=("Arial", 12))

# Vout input
label_vout = ttk.Label(root, text="Vout (V):")
label_vout.pack(pady=(15, 0))
entry_vout = ttk.Entry(root)
entry_vout.insert(0, "0.0")
entry_vout.pack(pady=(0, 10))

# R6 input
label_r6 = ttk.Label(root, text="R6 (Ohms):")
label_r6.pack(pady=(10, 0))
entry_r6 = ttk.Entry(root)
entry_r6.insert(0, "998000")
entry_r6.pack(pady=(0, 10))

# R2 input
label_r2 = ttk.Label(root, text="R2 (Ohms):")
label_r2.pack(pady=(10, 0))
entry_r2 = ttk.Entry(root)
entry_r2.insert(0, "119.7")
entry_r2.pack(pady=(0, 10))

# Result label
result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var, font=("Arial", 16, "bold"))
result_label.pack(pady=20)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate Vof", command=calculate_vof)
calculate_button.pack(pady=15)

# Run the app
root.mainloop()