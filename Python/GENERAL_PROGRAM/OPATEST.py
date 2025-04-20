import tkinter as tk
from tkinter import ttk
import math

# -------------------- Shared Styling --------------------
def configure_styles():
    style = ttk.Style()
    style.theme_use("default")
    style.configure("TLabel", background="black", foreground="white", font=("Arial", 14))
    style.configure("TButton", background="black", foreground="white", font=("Arial", 12))
    style.configure("TEntry", fieldbackground="black", foreground="white", font=("Arial", 12))

# -------------------- Vos Calculator Frame --------------------
def create_vos_frame(container, switch_to_main):
    frame = tk.Frame(container, bg='black')

    def calculate_Vos():
        try:
            vout = float(entry_vout.get())
            r6 = float(entry_r6.get())
            r2 = float(entry_r2.get())
            Vos = vout / ((r6 / r2) + 1)
            result_var.set(f"Vos = {Vos * 1000:.2f} mV")
        except ValueError:
            result_var.set("Invalid input")

    ttk.Label(frame, text="Vout (V):").pack(pady=(15, 0), fill='x')
    entry_vout = ttk.Entry(frame)
    entry_vout.insert(0, "0.0")
    entry_vout.pack(fill='x', padx=20)

    ttk.Label(frame, text="R6 (Ohms):").pack(pady=(10, 0), fill='x')
    entry_r6 = ttk.Entry(frame)
    entry_r6.insert(0, "99800")
    entry_r6.pack(fill='x', padx=20)

    ttk.Label(frame, text="R2 (Ohms):").pack(pady=(10, 0), fill='x')
    entry_r2 = ttk.Entry(frame)
    entry_r2.insert(0, "119.7")
    entry_r2.pack(fill='x', padx=20)

    result_var = tk.StringVar()
    ttk.Label(frame, textvariable=result_var, font=("Arial", 16, "bold")).pack(pady=20, fill='x')
    ttk.Button(frame, text="Calculate Vos", command=calculate_Vos).pack(pady=10, fill='x', padx=20)
    ttk.Button(frame, text="Back", command=switch_to_main).pack(pady=10, fill='x', padx=20)

    return frame

# -------------------- Ibias and IOS Calculator Frame --------------------
def create_ibias_frame(container, switch_to_main):
    frame = tk.Frame(container, bg='black')

    def calculate_ibias():
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
            result_var.set(f"I_bias = {i_bias * 1e9:.2f} nA\nI_OS = {i_os * 1e9:.2f} nA")
        except ValueError:
            result_var.set("Invalid input")

    fields = [
        ("V_OUTA (V):", "0.0"),
        ("V_OUTB (V):", "0.0"),
        ("V_OUTC (V):", "0.0"),
        ("R1 (Ohms):", "99900"),
        ("R2 (Ohms):", "118.9"),
        ("R4 (Ohms):", "997000"),
        ("R5 (Ohms):", "994000")
    ]

    entries = []
    for label_text, default in fields:
        ttk.Label(frame, text=label_text).pack(pady=(10, 0), fill='x')
        entry = ttk.Entry(frame)
        entry.insert(0, default)
        entry.pack(fill='x', padx=20)
        entries.append(entry)

    entry_vouta, entry_voutb, entry_voutc, entry_r1, entry_r2, entry_r4, entry_r5 = entries
    result_var = tk.StringVar()
    ttk.Label(frame, textvariable=result_var, font=("Arial", 16, "bold")).pack(pady=20, fill='x')
    ttk.Button(frame, text="Calculate I_bias and I_OS", command=calculate_ibias).pack(pady=10, fill='x', padx=20)
    ttk.Button(frame, text="Back", command=switch_to_main).pack(pady=10, fill='x', padx=20)

    return frame

# -------------------- CMRR Calculator Frame --------------------
def create_cmrr_frame(container, switch_to_main):
    frame = tk.Frame(container, bg='black')

    def calculate_cmrr():
        try:
            vout1_mv = float(entry_vout1.get())
            vout2_mv = float(entry_vout2.get())
            r6 = float(entry_r6.get())
            r2 = float(entry_r2.get())
            vout1 = vout1_mv / 1000
            vout2 = vout2_mv / 1000
            delta_vout = abs(vout1 - vout2)
            gain = (r6 / r2 + 1) * 20
            cmrr = 20 * math.log10(gain / delta_vout)
            result_var.set(f"CMRR = {cmrr:.2f} dB")
        except ValueError:
            result_var.set("Invalid input")
        except ZeroDivisionError:
            result_var.set("∆V_out cannot be 0")

    fields = [
        ("Vout1 (mV):", "0.0"),
        ("Vout2 (mV):", "10.0"),
        ("R6 (Ohms):", "99800"),
        ("R2 (Ohms):", "120.3")
    ]

    entries = []
    for label_text, default in fields:
        ttk.Label(frame, text=label_text).pack(pady=(10, 0), fill='x')
        entry = ttk.Entry(frame)
        entry.insert(0, default)
        entry.pack(fill='x', padx=20)
        entries.append(entry)

    entry_vout1, entry_vout2, entry_r6, entry_r2 = entries
    result_var = tk.StringVar()
    ttk.Label(frame, textvariable=result_var, font=("Arial", 16, "bold")).pack(pady=20, fill='x')
    ttk.Button(frame, text="Calculate CMRR", command=calculate_cmrr).pack(pady=10, fill='x', padx=20)
    ttk.Button(frame, text="Back", command=switch_to_main).pack(pady=10, fill='x', padx=20)

    return frame

# -------------------- PSRR Calculator Frame --------------------
def create_psrr_frame(container, switch_to_main):
    frame = tk.Frame(container, bg='black')

    def calculate_psrr():
        try:
            vout1_mv = float(entry_vout1.get())
            vout2_mv = float(entry_vout2.get())
            r6 = float(entry_r6.get())
            r2 = float(entry_r2.get())
            vout1 = vout1_mv / 1000
            vout2 = vout2_mv / 1000
            delta_vout = abs(vout1 - vout2)
            gain = (r6 / r2 + 1) * 1
            psrr = 20 * math.log10(gain / delta_vout)
            result_var.set(f"PSRR = {psrr:.2f} dB")
        except ValueError:
            result_var.set("Invalid input")
        except ZeroDivisionError:
            result_var.set("∆V_out cannot be 0")

    fields = [
        ("Vout1 (mV):", "0.0"),
        ("Vout2 (mV):", "10.0"),
        ("R6 (Ohms):", "99800"),
        ("R2 (Ohms):", "120.3")
    ]

    entries = []
    for label_text, default in fields:
        ttk.Label(frame, text=label_text).pack(pady=(10, 0), fill='x')
        entry = ttk.Entry(frame)
        entry.insert(0, default)
        entry.pack(fill='x', padx=20)
        entries.append(entry)

    entry_vout1, entry_vout2, entry_r6, entry_r2 = entries
    result_var = tk.StringVar()
    ttk.Label(frame, textvariable=result_var, font=("Arial", 16, "bold")).pack(pady=20, fill='x')
    ttk.Button(frame, text="Calculate PSRR", command=calculate_psrr).pack(pady=10, fill='x', padx=20)
    ttk.Button(frame, text="Back", command=switch_to_main).pack(pady=10, fill='x', padx=20)

    return frame

# -------------------- Main Menu Frame --------------------
def create_main_menu(container, switch_to_Vos, switch_to_ibias, switch_to_cmrr, switch_to_psrr):
    frame = tk.Frame(container, bg='black')
    ttk.Label(frame, text="Select Calculator:", font=("Arial", 16)).pack(pady=30, fill='x')
    ttk.Button(frame, text="Vos Calculator", command=switch_to_Vos).pack(pady=10, fill='x', padx=50)
    ttk.Button(frame, text="I_bias & I_OS Calculator", command=switch_to_ibias).pack(pady=10, fill='x', padx=50)
    ttk.Button(frame, text="CMRR Calculator", command=switch_to_cmrr).pack(pady=10, fill='x', padx=50)
    ttk.Button(frame, text="PSRR Calculator", command=switch_to_psrr).pack(pady=10, fill='x', padx=50)
    return frame

# -------------------- Main Application --------------------
root = tk.Tk()
root.title("Multi Calculator")
root.configure(bg='black')
root.geometry("600x700")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
configure_styles()

container = tk.Frame(root, bg="black")
container.grid(row=0, column=0, sticky="nsew")
container.rowconfigure(0, weight=1)
container.columnconfigure(0, weight=1)

frames = {}

def show_frame(name):
    frame = frames[name]
    frame.tkraise()

frames["main"] = create_main_menu(
    container,
    lambda: show_frame("Vos"),
    lambda: show_frame("ibias"),
    lambda: show_frame("cmrr"),
    lambda: show_frame("psrr")
)
frames["Vos"] = create_vos_frame(container, lambda: show_frame("main"))
frames["ibias"] = create_ibias_frame(container, lambda: show_frame("main"))
frames["cmrr"] = create_cmrr_frame(container, lambda: show_frame("main"))
frames["psrr"] = create_psrr_frame(container, lambda: show_frame("main"))

for frame in frames.values():
    frame.grid(row=0, column=0, sticky="nsew")

show_frame("main")
root.mainloop()
