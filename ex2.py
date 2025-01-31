import turtle


def heart():
    h = turtle.Turtle()
    h.pensize(2)
    h.speed(1)
    h.color("red")

    h.penup()
    h.goto(-100, 50)  # Điều chỉnh vị trí ban đầu nếu cần
    h.pendown()

    h.begin_fill()
    h.fillcolor("red")

    h.right(150)  # Đổi hướng quay từ left(150) sang right(150)
    h.forward(180)
    h.circle(60, 180)  # Đổi từ -60 thành 60 để đúng hướng
    h.setheading(240)  # Điều chỉnh góc cho phần còn lại
    h.circle(60, 180)
    h.forward(180)

    h.end_fill()
    h.hideturtle()


# Gọi hàm để vẽ trái tim
heart()
turtle.done()
