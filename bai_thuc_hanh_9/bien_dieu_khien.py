import tkinter as tk

def hien_thi_thong_tin():
    print("Ho ten:", bien_ho_ten.get())
    print("Tuoi:", bien_tuoi.get())
    print("Dang di hoc:", bien_dang_di_hoc.get())

cua_so = tk.Tk()
cua_so.title("Bien dieu khien")
cua_so.geometry("360x230")

bien_ho_ten = tk.StringVar(value="Nguyen Dang Canh")
bien_tuoi = tk.IntVar(value=18)
bien_dang_di_hoc = tk.BooleanVar(value=False)

tk.Label(
    cua_so, text="Ho ten:"
).grid(row=0, column=0, padx=10, pady=10, sticky="w")

tk.Entry(
    cua_so, textvariable=bien_ho_ten
).grid(row=0, column=1, padx=10, pady=10)

tk.Label(
    cua_so, text="Tuoi:"
).grid(row=1, column=0, padx=10, pady=10, sticky="w")

tk.Entry(
    cua_so, textvariable=bien_tuoi
).grid(row=1, column=1, padx=10, pady=10)

tk.Checkbutton(
    cua_so,
    text="Dang di hoc",
    variable=bien_dang_di_hoc
).grid(row=2, column=0, columnspan=2, pady=10)

tk.Button(
    cua_so,
    text="Xem thong tin",
    command=hien_thi_thong_tin
).grid(row=3, column=0, columnspan=2, pady=10)

cua_so.mainloop()
