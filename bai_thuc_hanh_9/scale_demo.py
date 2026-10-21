import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Scale")
cua_so.geometry("350x180")

nhan_gia_tri = tk.Label(
    cua_so, text="Gia tri hien tai: 50"
)
nhan_gia_tri.pack(pady=12)

def cap_nhat_gia_tri(gia_tri):
    nhan_gia_tri.config(
        text=f"Gia tri hien tai: {int(float(gia_tri))}"
    )

thanh_truot = tk.Scale(
    cua_so,
    from_=0,
    to=100,
    orient="horizontal",
    command=cap_nhat_gia_tri,
    length=280
)

thanh_truot.set(50)
thanh_truot.pack(pady=10)

cua_so.mainloop()
