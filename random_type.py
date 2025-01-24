from math import trunc
from random import randrange
n = int(input("nhập vào số bất kỳ từ 0 - 10: "))
print(f"số bạn đoán là {n}")
while(n > 10 or n < 0):
    n = int(input("nhập lại số từ 0 - 10: "))
    print(f"số bạn đoán là {n}")

a = randrange(0, 11)
print(f"số máy chọn là {a}")
nguoiLuonThang = True
while(nguoiLuonThang):
    if n == a:
        print("hai bên hòa")
    elif n != a:
        print("bạn đã thua")
    nguoiLuonThang = False

