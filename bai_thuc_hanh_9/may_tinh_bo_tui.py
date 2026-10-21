import tkinter as tk
from tkinter import messagebox

def tinh_toan(phep_tinh):
    try:
        a = float(o_so_a.get())
        b = float(o_so_b.get())

        if phep_tinh == "+":
            ket_qua = a + b
        elif phep_tinh == "-":
            ket_qua = a - b
        elif phep_tinh == "*":
            ket_qua = a * b
        elif phep_tinh == "/":
            if b == 0:
                messagebox.showerror(
                    "Loi", "Khong the chia cho 0."
                )
                return
            ket_qua = a / b

        nhan_ket_qua.config(
            text=f"Ket qua: {ket_qua:g}"
        )

    except ValueError:
        messagebox.showerror(
            "Loi", "Vui long nhap hai so hop le."
        )

cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("320x300")

tk.Label(
    cua_so,
    text="MAY TINH BO TUI",
    font=("Arial", 15, "bold")
).pack(pady=12)

tk.Label(cua_so, text="So thu nhat:").pack()
o_so_a = tk.Entry(cua_so)
o_so_a.pack(pady=4)

tk.Label(cua_so, text="So thu hai:").pack()
o_so_b = tk.Entry(cua_so)
o_so_b.pack(pady=4)

khung_nut = tk.Frame(cua_so)
khung_nut.pack(pady=10)

for ky_hieu in ["+", "-", "*", "/"]:
    tk.Button(
        khung_nut,
        text=ky_hieu,
        width=4,
        command=lambda p=ky_hieu: tinh_toan(p)
    ).pack(side="left", padx=3)

nhan_ket_qua = tk.Label(
    cua_so, text="Ket qua:", font=("Arial", 12)
)
nhan_ket_qua.pack(pady=10)

cua_so.mainloop()
