
#draw smile ^_^
import turtle
turtle.setup(800, 600)

def smile():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(5)
    t.pensize(3)



    #face
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(100, 360)
    t.end_fill()

    #left eye
    t.penup()
    t.goto(-40, 30)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.setheading(45)
    for i in range(2):
        t.circle(15, 90)
        t.circle(10, 90)
    t.end_fill()

    #right eye
    t.penup()
    t.goto(40, 30)
    t.pendown()
    t.begin_fill()
    t.setheading(45)
    for i in range(2):
        t.circle(15, 90)
        t.circle(10, 90)
    t.end_fill()

    #mouth
    t.penup()
    t.goto(-35, -20)
    t.setheading(60)
    t.pendown()
    t.setheading(-60)
    t.color("black")
    t.begin_fill()
    t.circle(40, 120)


screen = turtle.Screen().bgcolor("black")
smile()
turtle.done()