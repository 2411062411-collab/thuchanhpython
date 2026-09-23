for i in range(1, 6):
    print(i)

diem_so = [8.5, 7.0, 9.2, 6.5]

for diem in diem_so:
    print("Điểm:", diem)


toa_do = (3, 5)

for gia_tri in toa_do:
    print("Tọa độ:", gia_tri)

sinh_vien = {
    "ten": "An",
    "tuoi": 20,
    "lop": "K65"
}

for mon, diem in sinh_vien.items():
    print(mon, ":", diem)

tu = "Python"

for ky_tu in tu:
    print(ky_tu)


n = 5

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

n = 5

giai_thua = 1
i = 1

while i <= n:
    giai_thua *= i
    i += 1

print(f"{n}! = {giai_thua}")

so = 4527

tong_chu_so = 0
so_tam = so

while so_tam > 0:
    chu_so = so_tam % 10
    tong_chu_so += chu_so
    so_tam //= 10

print(f"Tổng các chữ số của {so} là: {tong_chu_so}")