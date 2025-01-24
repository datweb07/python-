import math
print("Giải phương trinh bậc 2")
heSoA = float(input("Nhập vào hệ số a: "))
heSoB = float(input("Nhập vào hệ số b: "))
heSoC = float(input("Nhập vào hệ số c: "))
if heSoA == 0:
    if heSoB == 0:
        if heSoC == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print(f"Phương trình có đúng 1 nghiệm là: {-heSoC / heSoB}")
else:
    denTa = float((heSoB ** 2) - (4 * heSoA * heSoC))
    if denTa > 0:
        print(f"Phương trình có 2 nghiệm: x1 = {(-heSoB + math.sqrt(denTa)) / (2 * heSoA)}, x2 = {(-heSoB - math.sqrt(denTa)) / (2 * heSoA)}")
    elif denTa == 0:
        print(f"Phương trình có đúng 1 nghiệm là: {-heSoB / (2 * heSoA)}")
    else:
        print("Phương trình vô nghiệm")


