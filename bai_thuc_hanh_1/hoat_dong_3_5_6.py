ten = "Phan Quang Huy"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000  

print(ten, diem_toan, diem_van, so_luong_mon_hoc, MUC_LUONG_TOI_THIEU)

import keyword
print(keyword.kwlist)
print("Số lượng từ khóa:", len(keyword.kwlist))


a = 17
b = 5
print("Bài 5.1 - Tính toán:", a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

diem = 6.5
tuoi = 20
print("Bài 5.2 - Đạt loại Khá?", diem >= 6.5 and diem < 8.0)
print("Bài 5.2 - Chưa đủ 18 hoặc trên 60?", tuoi < 18 or tuoi > 60)

print("Bài 5.4 - Độ ưu tiên 1:", 2 + 3 * 4 ** 2)
print("Bài 5.4 - Độ ưu tiên 2:", (2 + 3) * 4 ** 2)

print("--- Bài 6.1 ---")
bien = 10
print(bien, type(bien))
bien = "Xin chao"
print(bien, type(bien))

print("--- Bài 6.2: Tính điểm tổng hợp ---")
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu) 