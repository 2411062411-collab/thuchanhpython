import tkinter as tk


def xu_ly_submit():
    ho_ten = entry_ho_ten.get().strip()
    tuoi = entry_tuoi.get().strip()
    email = entry_email.get().strip()

    if not ho_ten or not tuoi or not email:
        nhan_ket_qua.config(
            text="Vui lòng nhập đầy đủ thông tin!",
            fg="red"
        )
        return

    if not tuoi.isdigit() or int(tuoi) <= 0:
        nhan_ket_qua.config(
            text="Tuổi phải là số nguyên dương!",
            fg="red"
        )
        return

    if "@" not in email or "." not in email:
        nhan_ket_qua.config(
            text="Email không hợp lệ!",
            fg="red"
        )
        return

    nhan_ket_qua.config(
        text=(
            f"Họ tên: {ho_ten}\n"
            f"Tuổi: {tuoi}\n"
            f"Email: {email}"
        ),
        fg="blue"
    )


def xoa_thong_tin():
    entry_ho_ten.delete(0, tk.END)
    entry_tuoi.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    nhan_ket_qua.config(text="")


cua_so = tk.Tk()
cua_so.title("Form nhập thông tin")
cua_so.geometry("400x280")
cua_so.resizable(False, False)

tk.Label(cua_so, text="Họ tên:").grid(
    row=0, column=0, padx=10, pady=10, sticky="w"
)
entry_ho_ten = tk.Entry(cua_so, width=30)
entry_ho_ten.grid(row=0, column=1, padx=10, pady=10)

tk.Label(cua_so, text="Tuổi:").grid(
    row=1, column=0, padx=10, pady=10, sticky="w"
)
entry_tuoi = tk.Entry(cua_so, width=30)
entry_tuoi.grid(row=1, column=1, padx=10, pady=10)

tk.Label(cua_so, text="Email:").grid(
    row=2, column=0, padx=10, pady=10, sticky="w"
)
entry_email = tk.Entry(cua_so, width=30)
entry_email.grid(row=2, column=1, padx=10, pady=10)

tk.Button(
    cua_so,
    text="Submit",
    command=xu_ly_submit
).grid(row=3, column=0, pady=15)

tk.Button(
    cua_so,
    text="Xóa",
    command=xoa_thong_tin
).grid(row=3, column=1, pady=15)

nhan_ket_qua = tk.Label(
    cua_so,
    text="",
    font=("Arial", 11),
    fg="blue"
)
nhan_ket_qua.grid(
    row=4, column=0, columnspan=2, pady=10
)

cua_so.mainloop()
