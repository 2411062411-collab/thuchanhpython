import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Ví dụ Frame")
cua_so.geometry("400x300")

khung_tren = tk.Frame(
    cua_so,
    bg="lightblue",
    height=100
)
khung_tren.pack(fill="x")
khung_tren.pack_propagate(False)

khung_duoi = tk.Frame(
    cua_so,
    bg="lightyellow"
)
khung_duoi.pack(fill="both", expand=True)

tk.Label(
    khung_tren,
    text="Khu vực tiêu đề",
    bg="lightblue"
).pack(pady=10)

tk.Label(
    khung_duoi,
    text="Khu vực nội dung",
    bg="lightyellow"
).pack(pady=10)

cua_so.mainloop()
