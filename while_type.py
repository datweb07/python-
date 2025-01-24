nhapVao = int(input("nhập vào một số bất kỳ từ 1 - 100: "))
if 1 <= nhapVao <= 100:
    print(nhapVao)
else:
    while nhapVao < 1 or nhapVao > 100:
        nhapVao = int(input("nhập lại số: "))
        print(nhapVao)

