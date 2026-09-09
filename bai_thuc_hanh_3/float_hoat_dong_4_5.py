print("\n--- Bài tập 4.1 ---")
toa_do = (3, 5)
print("Tọa độ:", toa_do)

print("\n--- Bài tập 4.2 ---")
x, y = toa_do
print("x =", x)
print("y =", y)


a, b = 10, 20
print("\nTrước khi đổi:")
print("a =", a)
print("b =", b)
a, b = b, a
print("Sau khi đổi:")
print("a =", a)
print("b =", b)

print("\n--- Bài tập 4.3 ---")
c, d = 17, 5
thuong, du = divmod(c, d)
print("Thương =", thuong)
print("Dư =", du)


import math
diem_goc = (0, 0)
cac_diem = [(0, 0), (3, 4), (6, 8)]
print("Điểm gốc:", diem_goc)
print("Danh sách các điểm:", cac_diem)
x0, y0 = diem_goc
for diem in cac_diem:
    x, y = diem
    khoang_cach = math.sqrt(
        (x - x0) ** 2 + (y - y0) ** 2
    )
    print(
        f"Điểm {diem} cách điểm gốc "
        f"{diem_goc}: {khoang_cach:.2f}"
    )
