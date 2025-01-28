import turtle
import time

turtle.setup(800, 600)


def draw_text():
    t.color("yellow")  # Màu chữ
    t.penup()
    # Tính toán chiều dài chuỗi và điều chỉnh vị trí để căn giữa
    text = "HAPPY NEW YEAR 2025"
    width = len(text) * 30  # 40 là độ rộng của mỗi ký tự (khoảng cách giữa các ký tự)
    t.goto(-width / 2.5, 0)  # Căn giữa theo chiều ngang
    t.pendown()

    for char in text.upper():  # Chuyển thành chữ hoa
        t.write(char, font=("Arial", 30, "bold"))  # Thay đổi font chữ và kích thước
        time.sleep(0.3)  # Hiệu ứng chạy chậm lại
        t.forward(40)  # Dịch chuyển con trỏ để viết chữ tiếp theo


t = turtle.Turtle()
t.speed(3)
s = turtle.Screen()
s.bgcolor('black')

draw_text()
turtle.done()
