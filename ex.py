# import pyfiglet
# import time
# text = pyfiglet.figlet_format('Happy New Year', width = 200)
# for i in text.splitlines():
#     print(i)
#     time.sleep(0.5)




import turtle
import time
import random

# Cài đặt màn hình
turtle.setup(800, 600)
s = turtle.Screen()
s.bgcolor("black")

# Con trỏ rùa chính
t = turtle.Turtle()
t.speed(3)
t.hideturtle()

# Hàm viết chữ
def text():
    t.color("yellow")  # Màu chữ
    t.penup()
    t.hideturtle()  # Ẩn con trỏ rùa
    # Tính toán chiều dài chuỗi và điều chỉnh vị trí để căn giữa
    writeText = "HAPPY NEW YEAR"
    width = len(writeText) * 30  # 40 là độ rộng của mỗi ký tự
    t.goto(width / -1.5, 0)  # Căn giữa theo chiều ngang

    for char in writeText.upper():  # Chuyển thành chữ hoa
        t.write(char, font=("Arial", 30, "bold"))  # Thay đổi font chữ và kích thước
        time.sleep(0.3)  # Hiệu ứng chạy chậm lại
        t.penup()  # Không vẽ khi di chuyển
        t.forward(40)  # Dịch chuyển con trỏ để viết chữ tiếp theo

# Hàm hiệu ứng pháo hoa
def fireworks():
    firework_turtle = turtle.Turtle()
    firework_turtle.hideturtle()
    firework_turtle.speed(0)

    # Tạo nhiều lần pháo hoa
    for _ in range(10):  # Tùy chỉnh số lượng pháo hoa
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        firework_turtle.penup()
        firework_turtle.goto(x, y)
        firework_turtle.pendown()

        colors = ["red", "yellow", "blue", "green", "orange", "purple", "white"]
        firework_turtle.color(random.choice(colors))

        # Vẽ pháo hoa (lan tỏa từ trung tâm)
        for _ in range(36):  # 36 tia pháo hoa
            firework_turtle.forward(50)
            firework_turtle.backward(50)
            firework_turtle.right(10)

        time.sleep(0.5)  # Tạm dừng giữa các lần pháo hoa

# Hiển thị chữ
text()

# Hiệu ứng pháo hoa
fireworks()

# Kết thúc chương trình
turtle.done()
