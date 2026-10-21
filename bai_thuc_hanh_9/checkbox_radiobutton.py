import tkinter as tk

def hien_thi_so_thich():
    so_thich = []
    if bien_doc_sach.get():
        so_thich.append("Doc sach")
    if bien_the_thao.get():
        so_thich.append("The thao")
    if bien_am_nhac.get():
        so_thich.append("Am nhac")

    if so_thich:
        print("So thich da chon:", ", ".join(so_thich))
    else:
        print("Ban chua chon so thich nao.")

def hien_thi_tai_khoan():
    nhan_ket_qua.config(
        text="Ban da chon: " + bien_tai_khoan.get()
    )

cua_so = tk.Tk()
cua_so.title("Checkbox va Radiobutton")
cua_so.geometry("340x390")

tk.Label(
    cua_so, text="Chon so thich:",
    font=("Arial", 12, "bold")
).pack(pady=10)

bien_doc_sach = tk.BooleanVar(value=False)
bien_the_thao = tk.BooleanVar(value=False)
bien_am_nhac = tk.BooleanVar(value=False)

tk.Checkbutton(
    cua_so, text="Doc sach",
    variable=bien_doc_sach
).pack(anchor="w", padx=30)

tk.Checkbutton(
    cua_so, text="The thao",
    variable=bien_the_thao
).pack(anchor="w", padx=30)

tk.Checkbutton(
    cua_so, text="Am nhac",
    variable=bien_am_nhac
).pack(anchor="w", padx=30)

tk.Button(
    cua_so, text="Xem lua chon",
    command=hien_thi_so_thich
).pack(pady=8)

tk.Label(
    cua_so, text="Chon loai tai khoan:",
    font=("Arial", 12, "bold")
).pack(pady=(15, 5))

bien_tai_khoan = tk.StringVar(value="Ca nhan")

tk.Radiobutton(
    cua_so, text="Ca nhan",
    variable=bien_tai_khoan,
    value="Ca nhan"
).pack(anchor="w", padx=30)

tk.Radiobutton(
    cua_so, text="Doanh nghiep",
    variable=bien_tai_khoan,
    value="Doanh nghiep"
).pack(anchor="w", padx=30)

tk.Button(
    cua_so, text="Xac nhan",
    command=hien_thi_tai_khoan
).pack(pady=8)

nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()

cua_so.mainloop()
