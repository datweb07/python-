a = int(input("nhập một số bất kỳ: "))
if a % 2 == 0:
    for i in range(1, 6):
        a+=i
    print(f"tổng giá trị của a là: {a}")
else:
    print("đây là số lẻ, kết thúc chương trình")