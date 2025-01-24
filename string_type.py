import math

chuoi_1 = "Nguyễn Văn A"
chuoi_2 = "chúc mừng năm mới"
print(f"Chuỗi sau khi được nối là: {chuoi_1 + " " + chuoi_2}") #sử dụng dấu cộng để nối 2 chuỗi bất kỳ
chuoi_3 = "*" * 40 # sử dụng dấu * để nhân số ký tự của chuỗi lên n lần
print(f"{chuoi_3}")



a = 10
b = 4
print("Phần dư của phép chia là:", a % b)
print(f"Phần dư của phép tính là: {a % b}")
print(f"Phần nguyên của phép tính là: {10 // 4}")
print(f"Kết quả 10 lũy thừa 4: {10 ** 4}")
print(f"{chuoi_3}")

a = 2
b = 4
print(int(a/b))
print(f"{chuoi_3}")
print("BÀI TẬP 1")
import math
nhapVao = float(input("Nhập vào bán kính hình tròn: "))
print(f"Chu vi hình tròn là: {round((2 * math.pi * nhapVao), 3)}")
print(f"Diện tích hình tròn là: {round(math.pi * (nhapVao ** 2), 3)}")
print(f"{chuoi_3}")


print("BÀI TẬP 2")
time1 = float(input("Nhập thời gian của người 1: "))
time2 = float(input("Nhập thời gian của người 2: "))
time3 = float(input("Nhập thời gian của người 3: "))
timeTrungBinh = float((time1 + time2 + time3) / 3)
print(f"Thời gian trung bình của 3 người là: {round(timeTrungBinh, 3)}")
