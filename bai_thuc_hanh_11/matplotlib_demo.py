import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("diem_sinh_vien.csv")
dtb_mon = df.groupby("mon_hoc")["diem"].mean()

plt.figure(figsize=(6, 4))
plt.bar(dtb_mon.index, dtb_mon.values, color="skyblue")
plt.title("Diem trung binh theo mon hoc")
plt.xlabel("Mon hoc")
plt.ylabel("Diem trung binh")
plt.tight_layout()
plt.savefig("bieu_do_cot.png", dpi=150)
plt.show()

lan_kiem_tra = [1, 2, 3]
diem = [6.5, 7.5, 8.5]
plt.figure(figsize=(6, 4))
plt.plot(lan_kiem_tra, diem, marker="o", color="green")
plt.title("Xu huong diem qua cac lan kiem tra")
plt.xlabel("Lan kiem tra")
plt.ylabel("Diem")
plt.xticks(lan_kiem_tra)
plt.grid(True)
plt.tight_layout()
plt.savefig("bieu_do_duong.png", dpi=150)
plt.show()

print("Da tao bieu_do_cot.png va bieu_do_duong.png")
