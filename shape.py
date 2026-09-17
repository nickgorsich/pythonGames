import turtle as t
import time

def shapeGenerator():
    print()
    print("Welcome to shape generator!")
    sides = input("How many sides: ")
    length = input("Insert side length(10-200): ")
    angle = input("Insert angle: ")
    color = input("Pick a color: ")
    b_color = input("Pick a background color: ")
    t.up()
    t.goto(-250, -250)
    t.left(90)
    t.down()
    t.fillcolor(b_color)
    t.begin_fill()
    for i in range(4):
        t.forward(500)
        t.right(90)
    t.end_fill()
    t.up()
    t.goto(-100,0)
    t.down()
    for i in range(int(sides)):
        t.color(color)
        t.forward(int(length))
        t.right(int(angle))
    time.sleep(5)

shapeGenerator()