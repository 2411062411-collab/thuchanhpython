so_luot_truy_cap = 0


def tang_luot_truy_cap():
    global so_luot_truy_cap

    so_luot_truy_cap += 1


def vi_du_bien_local():
    so_luot_truy_cap = 100
    print("Biến local:", so_luot_truy_cap)


tang_luot_truy_cap()
tang_luot_truy_cap()

print("Số lượt truy cập:", so_luot_truy_cap)

vi_du_bien_local()

print("Sau hàm local, biến global vẫn là:", so_luot_truy_cap)


danh_sach_so = [1, 2, 3, 4, 5]

binh_phuong = list(
    map(lambda x: x ** 2, danh_sach_so)
)

print("Bình phương:", binh_phuong)


so_chan = list(
    filter(lambda x: x % 2 == 0, danh_sach_so)
)

print("Số chẵn:", so_chan)


danh_sach_sv = [
    {"ten": "An", "diem": 8.5},
    {"ten": "Binh", "diem": 7.0},
    {"ten": "Chi", "diem": 9.2}
]


sap_xep_theo_diem = sorted(
    danh_sach_sv,
    key=lambda sv: sv["diem"],
    reverse=True
)

print("Danh sách sinh viên sau khi sắp xếp:")

for sv in sap_xep_theo_diem:
    print(sv["ten"], "-", sv["diem"])


print("\n--- Giam dan ---")

for sv in sap_xep_theo_diem:
    print(sv["ten"], "-", sv["diem"])