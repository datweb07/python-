import turtle
import time

turtle.setup(800, 600)


def text():
    t.color("white")
    t.penup()
    t.hideturtle()
    writeText = "buồn ngủ quá ^_^"
    width = len(writeText) * 25
    t.goto(width / -1.5, 0)


    for char in writeText:
        t.write(char, font=("Times New Roman", 40, "normal"))
        time.sleep(0.3)
        t.forward(30)


t = turtle.Turtle()
t.speed(4)
s = turtle.Screen().bgcolor("black")
text()
turtle.done()
