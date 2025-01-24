import time
giay = time.time() #trả về số giây (epoch)
print(giay)

present = time.ctime() #chuyển số giây epoch sang thành chuỗi
print(present)

result = int(input("đáp án của bạn: "))
time.sleep(5)    #delay chương trình theo số giây
print("overtime")


timeLocal = time.localtime()
print(timeLocal)
print(f"năm hiện tại là: {timeLocal.tm_year}")


#string time
timeLocal = time.strftime("%m /%d/ %y, %H : %M : %S", timeLocal)
print(timeLocal)


#tính năm mình được 100 tuổi
name = input("nhập tên: ")
birthday = int(input("nhập tuổi: "))
thoiGian = time.localtime()
namHienTai = thoiGian.tm_year
print(f"{name} hiện tại {birthday} tuổi và năm {(100 - birthday) + namHienTai} sẽ đủ 100 tuổi")