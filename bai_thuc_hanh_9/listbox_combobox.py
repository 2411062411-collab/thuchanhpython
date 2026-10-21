import tkinter as tk
from tkinter import ttk, messagebox

cua_so = tk.Tk()
cua_so.title("Listbox va Combobox")
cua_so.geometry("360x390")

# Bai tap 3.1: Listbox
tk.Label(
    cua_so, text="Bai 3.1 - Chon mon an",
    font=("Arial", 12, "bold")
).pack(pady=8)

listbox_mon_an = tk.Listbox(
    cua_so, selectmode="single", height=5
)

for mon in ["Banh mi", "Lau", "Pho", "Com", "Bun"]:
    listbox_mon_an.insert(tk.END, mon)

listbox_mon_an.pack(pady=5)

def xem_mon_an():
    lua_chon = listbox_mon_an.curselection()

    if not lua_chon:
        messagebox.showwarning(
            "Thong bao", "Vui long chon mon an."
        )
        return

    mon_an = listbox_mon_an.get(lua_chon[0])
    messagebox.showinfo("Ket qua", "Ban chon: " + mon_an)

tk.Button(
    cua_so, text="Xem mon da chon",
    command=xem_mon_an
).pack(pady=5)

# Bai tap 3.2: Combobox
tk.Label(
    cua_so, text="Bai 3.2 - Chon thanh pho",
    font=("Arial", 12, "bold")
).pack(pady=(18, 5))

combobox_thanh_pho = ttk.Combobox(
    cua_so,
    values=["Ha Noi", "Da Nang", "TP. HCM", "Hue"],
    state="readonly"
)

combobox_thanh_pho.current(0)
combobox_thanh_pho.pack(pady=5)

def xem_thanh_pho():
    messagebox.showinfo(
        "Ket qua",
        "Ban chon: " + combobox_thanh_pho.get()
    )

tk.Button(
    cua_so, text="Xac nhan thanh pho",
    command=xem_thanh_pho
).pack(pady=8)

cua_so.mainloop()
