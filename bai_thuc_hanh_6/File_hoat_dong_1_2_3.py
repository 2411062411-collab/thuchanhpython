def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def bscnn(a, b):
    return a * b // uscln(a, b)


def kiem_tra_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0

    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i

    return tong_uoc == n


print("USCLN(24, 36) =", uscln(24, 36))
print("BSCNN(4, 6) =", bscnn(4, 6))
print("29 là số nguyên tố:", kiem_tra_nguyen_to(29))
print("28 là số hoàn thiện:", kiem_tra_so_hoan_thien(28))



def loi_chao(ten):
    print("Xin chào,", ten)
    return


def chia_lay_thuong_du(a, b):
    return a // b, a % b


loi_chao("An")

thuong, du = chia_lay_thuong_du(17, 5)

print("Thương:", thuong)
print("Dư:", du)




def gioi_thieu(ten, tuoi=18, hoc_van="Sinh viên"):
    print(f"Tên: {ten}, Tuổi: {tuoi}, Học vấn: {hoc_van}")


gioi_thieu("An")
gioi_thieu("Bình", 20)
gioi_thieu("Lan", hoc_van="CNTT")
gioi_thieu("Dung", tuoi=19)

def tinh_tong(*args):
    tong = 0

    for so in args:
        tong += so

    return tong


print("Tổng:", tinh_tong(1, 2, 3))
print("Tổng:", tinh_tong(5, 10, 15, 20, 25))
print("Tổng rỗng:", tinh_tong())


def in_thong_tin(ten, tuoi, **kwargs):
    print("Họ tên:", ten)
    print("Tuổi:", tuoi)

    for khoa, gia_tri in kwargs.items():
        print(f"{khoa}: {gia_tri}")


in_thong_tin(
    "Nguyen Van A",
    20,
    lop="CNTT1",
    que_quan="Ha Noi"
)

in_thong_tin(
    "Tran Thi B",
    21,
    email="example.com"
)