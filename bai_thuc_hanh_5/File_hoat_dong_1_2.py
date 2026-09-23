tuoi = 20

if tuoi >= 18:
    print("Đã đủ tuổi trưởng thành")

if tuoi >= 18:
    print("Được phép đăng ký xe máy")
else:
    print("Chưa đủ tuổi")

diem = 7.2

if diem >= 8.0:
    print("Xếp loại: Giỏi")
elif diem >= 6.5:
    print("Xếp loại: Khá")
elif diem >= 5.0:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")

tuoi = 17
co_giay_phep = False

if tuoi >= 18:
    if co_giay_phep:
        print("Được phép lái xe")
    else:
        print("Chưa có giấy phép")
else:
    print("Chưa đủ tuổi lái xe")


diem = 4.5

ket_qua = "Đạt" if diem >= 5.0 else "Không đạt"

so = -7
tri_tuyet_doi = so if so >= 0 else -so

print(ket_qua)
print(tri_tuyet_doi)


ho_ten = "Nguyen Van An"

diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = round((diem_toan + diem_ly + diem_hoa) / 3, 2)

if dtb >= 8.0:
    xep_loai = "Giỏi"
elif dtb >= 6.5:
    xep_loai = "Khá"
elif dtb >= 5.0:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"

print("Họ tên:", ho_ten)
print("DTB:", dtb)
print("Xếp loại:", xep_loai)


a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))

if a >= b and a >= c:
    lon_nhat = a
elif b >= a and b >= c:
    lon_nhat = b
else:
    lon_nhat = c

print("Số lớn nhất là:", lon_nhat)