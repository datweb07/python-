print("BÀI TẬP WHILE TRUE")
while True:
    ten = input("họ và tên: ")
    mon = input("môn dự thi: ")
    diem = float(input("diem: "))
    print(f"bạn {ten} dự thi môn {mon} với số điểm là {diem}")
    if diem >= 7:
        print("đã đủ điều kiện đạt giải")
    else:
        print("chưa đủ điều kiện đoạt giải")
    dung = input("nhập vào chữ 'N' để dừng chương trình: ")
    if dung == "N":
        break