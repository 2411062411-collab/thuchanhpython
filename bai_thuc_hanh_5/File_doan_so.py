import random

so_can_doan = random.randint(1, 10)

so_luot_toi_da = 7

luot_hien_tai = 1

print("===================================")
print("       TRÒ CHƠI ĐOÁN SỐ")
print("===================================")
print("Máy đã chọn một số từ 1 đến 10.")
print("Bạn có tối đa 7 lượt để đoán.")
print()

while luot_hien_tai <= so_luot_toi_da:

    so_doan = int(
        input(
            f"Lượt {luot_hien_tai}/{so_luot_toi_da} "
            f"- Nhập số bạn đoán: "
        )
    )

    if so_doan == so_can_doan:

        print()
        print(
            f"Chính xác! Bạn đã đoán đúng "
            f"sau {luot_hien_tai} lượt."
        )

        break

    elif so_doan < so_can_doan:

        print(
            "Gợi ý: Số cần đoán LỚN HƠN "
            "số bạn vừa nhập."
        )

    else:

        print(
            "Gợi ý: Số cần đoán NHỎ HƠN "
            "số bạn vừa nhập."
        )

    luot_hien_tai += 1

else:

    print()
    print(
        "Bạn đã hết 7 lượt đoán."
    )

    print(
        f"Số cần tìm là: {so_can_doan}"
    )