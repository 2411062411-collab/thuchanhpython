import math

so_nguyen = 15
so_thuc = 4.2
so_phuc = 3 + 4j
print(type(so_nguyen), type(so_thuc), type(so_phuc))
print(float(so_nguyen))
print(int(so_thuc))

a = -7
b = 2.6789
c, d = 17, 5
print(abs(a))
print(round(b))
print(round(b, 2))
print(pow(c, 2))
print(divmod(c, d))

a_pt, b_pt, c_pt = 1, -3, 2
delta = b_pt ** 2 - 4 * a_pt * c_pt
x1 = (-b_pt + math.sqrt(delta)) / (2 * a_pt)
x2 = (-b_pt - math.sqrt(delta)) / (2 * a_pt)
print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")

cau = "Lap trinh Python rat thu vi"
print(cau[0])
print(cau[-1])
print(cau[4:10])
print(cau[:8])
print(cau[11:])
print(cau[::-1])
print(cau == cau[::-1])

ten = "Nam"
ten_moi = "T" + ten[1:]
print(ten_moi)

cau_2 = " Toi dang HOC Python rat vui "
print(cau_2.strip())
print(cau_2.strip().upper())
print(cau_2.strip().lower())
print(cau_2.strip().replace("HOC", "hoc"))
print(cau_2.strip().split())
print(len(cau_2.strip().split()))
print(cau_2.count("o"))
print(cau_2.find("Python"))
print(cau_2.strip().startswith("Toi"))
print(cau_2.strip().endswith("vui"))
print("-".join(["Python", "that", "thu", "vi"]))

ho_ten_tho = " nguyen van an "
ho_ten_sach = " ".join(ho_ten_tho.split()).title()
print(ho_ten_sach)