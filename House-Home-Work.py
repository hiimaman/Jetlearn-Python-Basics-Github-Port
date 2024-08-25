# ChatGPT for parts I was to busy for (the X and Y)
# Im proud of myself

import turtle

t = turtle.Turtle()
sc = turtle.Screen()
sc.setup(1.0, 1.0)

# Function for a Square
def square(l, c):
    t.color(c)
    t.begin_fill()
    for i in range(4):
        t.forward(l)
        t.left(90)
    t.end_fill()

# Function for a Rectangle
def rectangle(l, c,):
    t.color(c)
    t.begin_fill()
    for i in range(2):
        t.forward(l)
        t.left(90)
        t.forward(l)
        t.left(90)
    t.end_fill()

# Function for a Triangle
def triangle(l, c):
    t.color(c)
    t.begin_fill()
    for i in range(3):
        t.forward(l)
        t.left(120)
    t.end_fill()

# Function to position the turtle
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Drawing shapes
move_to(-100, -100)
square(300, 'blue')
move_to(50, -100)
rectangle(80, 'yellow')
move_to(80, 70)
square(100, 'light blue')
move_to(-100, 200)
triangle(300, 'yellow')

sc.mainloop()
