"""sum = 0
for i in range(1, 8, 2):
    if i == 3:
        continue
    sum+=i
print(sum)"""
from math import trunc

"""print("BÀI TẬP: Tìm những số chia hết cho 3 trong đoạn từ 1-100")
for i in range(1, 101):
    if i % 3 != 0:
        continue
    print(i, end=" ")"""



"""print("BÀI TẬP: Tính tổng S = 1! + 2! + 3! + ... + 10!")
b = 1
sumB = 0
for i in range(1, 11):
    b*=i
    sumB+=b
print(f"tổng là: {sumB}")"""


"""print("BÀI TẬP: Tìm số hoàn hảo")
for a in range(1, 9999):
    sum = 0
    for i in range(1, a):
        if a % i == 0:
            sum += i
    if sum == a:
        print(a, end=" ")"""


"""print("BÀI TẬP: Tính tổng S(x,n) = x + (x^2/2!) + ... + (x^n/n!)")
x = int(input("nhập vào giá trị x: "))
n = int(input("nhập vào giá trị n: "))
a = 1
sum = 0
for i in range(1, n + 1):
    a*=i
    b = (x ** i) / a
    sum+=b
print(f"Tổng là: {sum}")"""


print("BÀI TẬP: Kiểm tra số nguyên tố")
# cách 1
"""soNguyenTo = int(input("nhập vào một số bất kỳ: "))
while soNguyenTo < 0:
    soNguyenTo = int(input("nhập lại số lớn hơn 0: "))
if soNguyenTo % 1 == 0 and soNguyenTo % soNguyenTo == 0:
    print(f"{soNguyenTo} là một số nguyên tố")
else:
    print(f"{soNguyenTo} không là một số nguyên tố")

while True:
    print("bạn có muốn thoát khỏi chương trình không?")
    co = input("nhập số 1 để thoát chương trình: ")
    if co == "1":
        break"""



#cách 2
"""soNguyenTo = int(input("nhập vào một số bất kỳ: "))
while soNguyenTo < 0:
    soNguyenTo = int(input("nhập lại số lớn hơn 0: "))
if soNguyenTo < 2:
    print(f"{soNguyenTo} không là số nguyên tố")
else:
    laSoNguyenTo = True
    for i in range(2, int(soNguyenTo ** 0.5) + 1):
        if soNguyenTo % i == 0:
            laSoNguyenTo = False
    if (laSoNguyenTo):
        print(f"{soNguyenTo} là số nguyên tố")
    else:
        print(f"{soNguyenTo} không là số nguyên tố")
while True:
    print("bạn có muốn thoát khỏi chương trình không?")
    co = input("nhập số 1 để thoát chương trình: ")
    if co == "1":
        break"""


a = [4,7,2,8]
a.extend([2,4])
print(a)
