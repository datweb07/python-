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

def smile():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(3)
    t.pensize(3)



    #face
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(100, 360)
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
    writeText="buồn ngủ quá ^_^"
    width = len(writeText) * 25
    x.penup()
    x.goto(width / -2, -150)

    for char in writeText:
         x.write(char, font=("Times New Roman", 40, "normal"))
         time.sleep(0.3)
         x.forward(30)


screen = turtle.Screen().bgcolor("black")
smile()
text()
turtle.done()