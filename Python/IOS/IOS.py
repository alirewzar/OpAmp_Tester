import tkinter as tk
from tkinter import ttk

# Function to calculate I_bias and I_OS
def calculate_currents():
    try:
        v_outa = float(entry_vouta.get())
        v_outb = float(entry_voutb.get())
        v_outc = float(entry_voutc.get())
        r1 = float(entry_r1.get())
        r2 = float(entry_r2.get())
        r4 = float(entry_r4.get())
        r5 = float(entry_r5.get())

        common_ratio = (r1 + r2) / r2
        i_b_minus = (v_outa - v_outb) / (r5 * common_ratio)
        i_b_plus = (v_outc - v_outa) / (r4 * common_ratio)

        i_bias = (i_b_plus + i_b_minus) / 2
        i_os = i_b_plus - i_b_minus

        result_var.set(f"I_bias = {i_bias*1e9:.2f} nA\nI_OS = {i_os*1e9:.2f} nA")
    except ValueError:
        result_var.set("Invalid input")

# Create the main window
root = tk.Tk()
root.title("I_bias and I_OS Calculator")
root.configure(bg='black')
root.geometry("500x600")

# Style configuration
style = ttk.Style()
style.theme_use("default")
style.configure("TLabel", background="black", foreground="white", font=("Arial", 14))
style.configure("TButton", background="black", foreground="white", font=("Arial", 12))
style.configure("TEntry", fieldbackground="black", foreground="white", font=("Arial", 12))

# Input fields
fields = [
    ("V_OUTA (V):", "0.0"),
    ("V_OUTB (V):", "0.0"),
    ("V_OUTC (V):", "0.0"),
    ("R1 (Ohms):", "99900"),
    ("R2 (Ohms):", "118.9"),
    ("R4 (Ohms):", "997000"),
    ("R5 (Ohms):", "994000"),
]

entries = []

for label_text, default in fields:
    label = ttk.Label(root, text=label_text)
    label.pack(pady=(10, 0))
    entry = ttk.Entry(root)
    entry.insert(0, default)
    entry.pack(pady=(0, 5))
    entries.append(entry)

entry_vouta, entry_voutb, entry_voutc, entry_r1, entry_r2, entry_r4, entry_r5 = entries

# Result label
result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var, font=("Arial", 16, "bold"))
result_label.pack(pady=20)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate I_bias and I_OS", command=calculate_currents)
calculate_button.pack(pady=15)

# Run the app
root.mainloop()