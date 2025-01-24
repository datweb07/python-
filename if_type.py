diemDauVao = float(input("Nhập vào điểm đầu vào của thí sinh: "))
if diemDauVao >= 8:
    print("Bạn đã đỗ")
elif (diemDauVao > 5 and diemDauVao) < 8:
    print("Bạn vẫn có cơ hội đậu")
else:
    print("Bạn đã trượt")

a = "*" * 40
print(a)

print("BÀI TẬP 1")
nhapSo = int(input("Nhập vào một số nguyên: "))
if nhapSo % 2 == 0:
    print(f"{nhapSo} là một số chẵn")
else:
    print(f"{nhapSo} là một số lẻ")
print(a)

print("BÀI TẬP 2")
# cách 1
nhapNam = int(input("Nhập vào một năm dương lịch: "))
if (nhapNam % 4 == 0 and nhapNam % 100 != 0) or (nhapNam % 400 == 0):
    print(f"{nhapNam} là một năm nhuận")
else:
    print(f"{nhapNam} không là năm nhuận")

# cách 2
def kiemTra (year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
year = 2025
if kiemTra(year):
    print("Đây là năm nhuận")
else:
    print("Đây không phải là năm nhuận")
print(a)

print("BÀI TẬP 3")
thang = int(input("Nhập vào một tháng bất kỳ trong năm: "))
if thang in [1, 3, 5, 7, 8, 10, 12]:
    print(f"Tháng {thang} có 31 ngày")
elif thang in [4, 6, 9, 11]:
    print(f"Tháng {thang} có 30 ngày")
elif (thang == 2):
    nam = int(input("Nhập thêm năm: "))
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print("Tháng 2 có 29 ngày")
    else:
        print("Tháng 2 có 28 ngày")
else:
    print("Nhập lại tháng hợp lệ")


