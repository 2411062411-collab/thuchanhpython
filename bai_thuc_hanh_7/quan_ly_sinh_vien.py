# ============================================================
# DỰ ÁN: QUẢN LÝ SINH VIÊN - TỔNG HỢP CHƯƠNG 1
# Python: list, dictionary, if/elif/else, for, while,
#         function, try-except, break, continue
# ============================================================

danh_sach_sv = [
    {"ma_sv": "SV001", "ho_ten": "Nguyen Van An", "tuoi": 20, "diem": 8.0},
    {"ma_sv": "SV002", "ho_ten": "Tran Thi Binh", "tuoi": 19, "diem": 7.5},
    {"ma_sv": "SV003", "ho_ten": "Le Van Cuong", "tuoi": 21, "diem": 9.0},
]

def nhap_so_nguyen(thong_bao):
    while True:
        try:
            return int(input(thong_bao))
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap so nguyen.")

def nhap_diem(thong_bao):
    while True:
        try:
            diem = float(input(thong_bao))
            if 0 <= diem <= 10:
                return diem
            print("-> Diem phai nam trong khoang 0 den 10.")
        except ValueError:
            print("-> Vui long nhap diem bang so.")

def hien_thi_danh_sach():
    print("\n========== DANH SACH SINH VIEN ==========")
    if not danh_sach_sv:
        print("-> Chua co sinh vien.")
        return

    print(f"{'Ma SV':<10}{'Ho ten':<25}{'Tuoi':<8}{'Diem':<8}")
    print("-" * 51)
    for sv in danh_sach_sv:
        print(f"{sv['ma_sv']:<10}{sv['ho_ten']:<25}"
              f"{sv['tuoi']:<8}{sv['diem']:<8.2f}")

def tim_sinh_vien(ma_sv):
    for sv in danh_sach_sv:
        if sv["ma_sv"].upper() == ma_sv.upper():
            return sv
    return None

def them_sinh_vien():
    print("\n========== THEM SINH VIEN ==========")
    ma_sv = input("Nhap ma sinh vien: ").strip().upper()

    if tim_sinh_vien(ma_sv) is not None:
        print("-> Ma sinh vien da ton tai.")
        return

    ho_ten = input("Nhap ho ten: ").strip()
    if not ho_ten:
        print("-> Ho ten khong duoc de trong.")
        return

    tuoi = nhap_so_nguyen("Nhap tuoi: ")
    if tuoi < 16:
        print("-> Tuoi khong hop le.")
        return

    diem = nhap_diem("Nhap diem: ")

    danh_sach_sv.append({
        "ma_sv": ma_sv,
        "ho_ten": ho_ten,
        "tuoi": tuoi,
        "diem": diem
    })
    print(f"-> Them sinh vien {ma_sv} thanh cong.")

def sua_sinh_vien():
    print("\n========== SUA SINH VIEN ==========")
    ma_sv = input("Nhap ma sinh vien can sua: ").strip().upper()
    sv = tim_sinh_vien(ma_sv)

    if sv is None:
        print("-> Khong tim thay sinh vien.")
        return

    ho_ten = input(f"Nhap ho ten moi ({sv['ho_ten']}): ").strip()
    if ho_ten:
        sv["ho_ten"] = ho_ten

    sv["tuoi"] = nhap_so_nguyen("Nhap tuoi moi: ")
    sv["diem"] = nhap_diem("Nhap diem moi: ")
    print("-> Cap nhat sinh vien thanh cong.")

def xoa_sinh_vien():
    print("\n========== XOA SINH VIEN ==========")
    ma_sv = input("Nhap ma sinh vien can xoa: ").strip().upper()
    sv = tim_sinh_vien(ma_sv)

    if sv is None:
        print("-> Khong tim thay sinh vien.")
        return

    danh_sach_sv.remove(sv)
    print(f"-> Da xoa sinh vien {ma_sv}.")

def tim_kiem_sinh_vien():
    print("\n========== TIM KIEM ==========")
    tu_khoa = input("Nhap ma SV hoac ho ten can tim: ").strip().lower()
    tim_thay = False

    for sv in danh_sach_sv:
        if (tu_khoa in sv["ma_sv"].lower()
                or tu_khoa in sv["ho_ten"].lower()):
            print(f"{sv['ma_sv']} - {sv['ho_ten']} - "
                  f"Tuoi: {sv['tuoi']} - Diem: {sv['diem']:.2f}")
            tim_thay = True

    if not tim_thay:
        print("-> Khong tim thay sinh vien.")

def thong_ke():
    print("\n========== THONG KE ==========")
    if not danh_sach_sv:
        print("-> Chua co du lieu.")
        return

    tong = sum(sv["diem"] for sv in danh_sach_sv)
    diem_tb = tong / len(danh_sach_sv)
    cao_nhat = max(danh_sach_sv, key=lambda sv: sv["diem"])

    so_dat = sum(1 for sv in danh_sach_sv if sv["diem"] >= 5)

    print(f"So luong sinh vien: {len(danh_sach_sv)}")
    print(f"Diem trung binh: {diem_tb:.2f}")
    print(f"So sinh vien dat (>= 5): {so_dat}")
    print(f"Sinh vien diem cao nhat: {cao_nhat['ho_ten']} "
          f"({cao_nhat['diem']:.2f})")

def hien_thi_menu():
    print("\n" + "=" * 45)
    print("       CHUONG TRINH QUAN LY SINH VIEN")
    print("=" * 45)
    print("1. Hien thi danh sach")
    print("2. Them sinh vien")
    print("3. Sua sinh vien")
    print("4. Xoa sinh vien")
    print("5. Tim kiem sinh vien")
    print("6. Thong ke")
    print("0. Thoat")

def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach()
        elif lua_chon == "2":
            them_sinh_vien()
        elif lua_chon == "3":
            sua_sinh_vien()
        elif lua_chon == "4":
            xoa_sinh_vien()
        elif lua_chon == "5":
            tim_kiem_sinh_vien()
        elif lua_chon == "6":
            thong_ke()
        elif lua_chon == "0":
            print("Cam on ban da su dung chuong trinh. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai.")

if __name__ == "__main__":
    chay_chuong_trinh()
