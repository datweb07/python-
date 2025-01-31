# import turtle
# import time
#
# turtle.setup(800, 600)
#
#
# def text():
#     t.color("white")
#     t.penup()
#     t.hideturtle()
#     writeText = "buồn ngủ quá ^_^"
#     width = len(writeText) * 25
#     t.goto(width / -1.5, 0)
#
#
#     for char in writeText:
#         t.write(char, font=("Times New Roman", 40, "normal"))
#         time.sleep(0.3)
#         t.forward(30)
#
#
# t = turtle.Turtle()
# t.speed(4)
# s = turtle.Screen().bgcolor("black")
# text()
# turtle.done()


# import turtle
#
# def draw_star(size):
#     t = turtle.Turtle()
#     t.speed(4)
#     t.color("yellow")
#     t.begin_fill()
#     for _ in range(5):
#         t.forward(size)
#         t.right(144)
#     t.end_fill()
#     t.hideturtle()
#
# turtle.setup(800, 600)
# screen = turtle.Screen()
# screen.bgcolor("black")
# draw_star(200)
# turtle.done()

#draw smile ^_^
import turtle
import time
turtle.setup(800, 600)
screen = turtle.Screen().bgcolor("black")
def smile():
    t = turtle.Turtle()
    t.hideturtle() #ẩn mũi tên khi vẽ
    t.speed(3)
    t.pensize(3)



    #face
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.color("yellow")
    t.begin_fill()  #fill bg
    t.circle(100, 360)   #bán kính và góc đường tròn
    t.end_fill()

    #left eye
    t.penup()
    t.goto(-40, 70)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(10, 360)
    t.end_fill()

    #right eye
    t.penup()
    t.goto(40, 70)
    t.pendown()
    t.begin_fill()
    t.circle(10, 360)
    t.end_fill()

    #mouth
    t.penup()
    t.goto(-35, 30)
    t.setheading(60)
    t.pendown()
    t.setheading(-60)
    t.circle(40, 120)


def text():
    x = turtle.Turtle()
    x.hideturtle()
    x.color("white")
    writeText="gúc nai"
    x.penup()
    x.goto(-170, -150)

    for char in writeText:
         x.write(char, font=("Times New Roman", 40, "normal"))
         time.sleep(0.3)
         x.forward(30)


def heart():
    h = turtle.Turtle()
    h.hideturtle()
    h.pensize(2)
    h.speed(1)
    h.color("red")
    h.penup()
    h.goto(150, -159)
    h.pendown()
    h.begin_fill()
    h.fillcolor("red")
    h.left(150)
    h.forward(60)   #vẽ tiến lên n đơn vị pixel
    h.circle(-30, 180)
    h.setheading(60)   #điều chỉnh góc
    h.circle(-30, 180)
    h.forward(60)
    h.end_fill()


smile()
text()
heart()
turtle.done()