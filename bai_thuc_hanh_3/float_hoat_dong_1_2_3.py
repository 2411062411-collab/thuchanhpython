diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]

print("Phần tử đầu tiên:", diem_so[0])
print("Phần tử cuối cùng:", diem_so[-1])
print("Các phần tử từ vị trí 1 đến trước 4:", diem_so[1:4])
print("Lấy cách 1 phần tử:", diem_so[::2])
print("Đảo ngược danh sách:", diem_so[::-1])


print("\n--- Bài tập 1.2 ---")
ten_sv = ["An", "Binh", "Chi"]
ten_sv.append("Dung")
ten_sv.insert(1, "Em")
ten_sv.remove("Chi")
pop_ra = ten_sv.pop()
print("Danh sách sau khi pop:", ten_sv)
print("Phần tử vừa lấy ra:", pop_ra)
ten_sv.sort()
print("Sau sort:", ten_sv)
ten_sv.reverse()
print("Sau reverse:", ten_sv)
ten_sv.extend(["Giang", "Hoa"])
print("Sau extend:", ten_sv)
print("\n--- Phân biệt remove() và pop() ---")
ds1 = ["An", "Binh", "Chi"]
ds1.remove("Binh")
print("Sau remove('Binh'):", ds1)
ds2 = ["An", "Binh", "Chi"]
x = ds2.pop(1)
print("Sau pop(1):", ds2)
print("Giá trị vừa lấy ra:", x)



print("\n--- Bài tập 2.1 ---")
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
tong = 0
for diem in diem_so:
    print(diem)
    tong = tong + diem
print("Tổng điểm:", tong)
print("Điểm trung bình:", round(tong / len(diem_so), 2))
ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("In từng hàng:")
for hang in ma_tran:
    print(hang)
print("\nIn từng phần tử:")
for hang in ma_tran:
    for phan_tu in hang:
        print(phan_tu, end=" ")
    print()
# Tính tổng tất cả phần tử trong ma trận
tong_ma_tran = sum(
    phan_tu
    for hang in ma_tran
    for phan_tu in hang
)
print("Tổng tất cả phần tử trong ma trận:", tong_ma_tran)


day_so = list(range(1, 21))
so_chan = [x for x in day_so if x % 2 == 0]
so_le = [x for x in day_so if x % 2 != 0]
print("Số chẵn:", so_chan)
print("Số lẻ:", so_le)


diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_cong = [
    round(diem + 0.5, 1)
    for diem in diem_so
]
print("Điểm ban đầu:", diem_so)
print("Điểm sau khi cộng 0.5:", diem_cong)
