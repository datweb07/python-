thang = int(input("nhập vào một tháng: "))
if 1 <= thang <= 12:
    if thang in [1, 2, 3]:
        print(f"Tháng {thang} thuộc quý 1")
    elif thang in [4, 5, 6]:
        print(f"tháng {thang} thuộc quý 2")
    elif thang in [7, 8, 9]:
        print(f"tháng {thang} thuộc quý 3")
    else:
        print(f"tháng {thang} thuộc quý 4")
else:
    print("Nhập lại tháng!")