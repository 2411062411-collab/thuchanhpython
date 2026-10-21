import tkinter as tk
from tkinter import messagebox

danh_sach_cong_viec = []

def lam_moi_listbox():
    listbox_cong_viec.delete(0, tk.END)

    for noi_dung, da_hoan_thanh in danh_sach_cong_viec:
        trang_thai = "[Da xong]" if da_hoan_thanh else "[Chua xong]"
        listbox_cong_viec.insert(
            tk.END, f"{trang_thai} - {noi_dung}"
        )

def them_cong_viec():
    noi_dung = bien_cong_viec.get().strip()

    if not noi_dung:
        messagebox.showerror(
            "Loi", "Vui long nhap noi dung cong viec."
        )
        return

    danh_sach_cong_viec.append([noi_dung, False])
    bien_cong_viec.set("")
    lam_moi_listbox()

def xoa_cong_viec():
    lua_chon = listbox_cong_viec.curselection()

    if not lua_chon:
        messagebox.showwarning(
            "Thong bao", "Vui long chon cong viec can xoa."
        )
        return

    del danh_sach_cong_viec[lua_chon[0]]
    lam_moi_listbox()

def danh_dau_hoan_thanh():
    lua_chon = listbox_cong_viec.curselection()

    if not lua_chon:
        messagebox.showwarning(
            "Thong bao", "Vui long chon cong viec."
        )
        return

    danh_sach_cong_viec[lua_chon[0]][1] = True
    lam_moi_listbox()

cua_so = tk.Tk()
cua_so.title("Ung dung ghi chu cong viec")
cua_so.geometry("460x400")

tk.Label(
    cua_so,
    text="QUAN LY CONG VIEC",
    font=("Arial", 16, "bold")
).pack(pady=10)

bien_cong_viec = tk.StringVar()

tk.Entry(
    cua_so,
    textvariable=bien_cong_viec,
    width=42
).pack(padx=10, pady=8)

tk.Button(
    cua_so,
    text="Them cong viec",
    command=them_cong_viec
).pack(pady=5)

listbox_cong_viec = tk.Listbox(
    cua_so, width=52, height=10
)
listbox_cong_viec.pack(padx=10, pady=10)

khung_nut = tk.Frame(cua_so)
khung_nut.pack(pady=5)

tk.Button(
    khung_nut,
    text="Xoa",
    command=xoa_cong_viec
).grid(row=0, column=0, padx=5)

tk.Button(
    khung_nut,
    text="Danh dau hoan thanh",
    command=danh_dau_hoan_thanh
).grid(row=0, column=1, padx=5)

cua_so.mainloop()
