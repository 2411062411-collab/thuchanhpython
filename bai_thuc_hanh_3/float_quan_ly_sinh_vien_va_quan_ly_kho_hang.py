danh_sach_sv = [
    (8.5, "An"),
    (7.0, "Binh"),
    (9.2, "Chi"),
    (6.5, "Dung")
]

print("\nDanh sách sinh viên ban đầu:")

for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")


danh_sach_sv.append((8.0, "Em"))

print("\nSau khi thêm sinh viên Em:")

for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")


danh_sach_sv.remove((7.0, "Binh"))

print("\nSau khi xóa sinh viên Binh:")

for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")


danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])

print("\nSau khi sửa điểm sinh viên ở vị trí 0:")

for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")


print("\nKiểm tra sinh viên (9.2, 'Chi'):")

if (9.2, "Chi") in danh_sach_sv:
    print("Sinh viên Chi có trong danh sách.")
else:
    print("Sinh viên Chi không có trong danh sách.")


danh_sach_sv.sort(key=lambda sv: sv[0])

print("\nDanh sách sinh viên sắp xếp tăng dần theo điểm:")

for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")


danh_sach_sv.sort(
    key=lambda sv: sv[0],
    reverse=True
)
print("\nDanh sách sinh viên sắp xếp giảm dần theo điểm:")

for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")




kho_hang = [
    ("Bàn phím", 250000, 10),
    ("Chuột", 150000, 20),
    ("Màn hình", 2500000, 5)
]


print("\nDanh sách kho hàng ban đầu:")

for ten, gia, so_luong in kho_hang:
    print(
        f"{ten} - Giá: {gia:,} VNĐ "
        f"- Số lượng: {so_luong}"
    )



kho_hang.append(
    ("Tai nghe", 300000, 15)
)

print("\nSau khi thêm Tai nghe:")

for ten, gia, so_luong in kho_hang:
    print(
        f"{ten} - Giá: {gia:,} VNĐ "
        f"- Số lượng: {so_luong}"
    )


kho_hang.remove(
    ("Chuột", 150000, 20)
)
print("\nSau khi xóa Chuột:")
for ten, gia, so_luong in kho_hang:
    print(
        f"{ten} - Giá: {gia:,} VNĐ "
        f"- Số lượng: {so_luong}"
    )-
tong_gia_tri = 0
for ten, gia, so_luong in kho_hang:

    tong_gia_tri = (
        tong_gia_tri
        + gia * so_luong
    )
print(
    f"\nTổng giá trị kho hàng: "
    f"{tong_gia_tri:,} VNĐ"
)
