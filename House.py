import turtle

t = turtle.Turtle()
sc = turtle.Screen()
sc.setup(1.0, 1.0)
t.speed(9)

# Function for a Square
def square(l, c):
    t.color(c)
    t.begin_fill()
    for i in range(4):
        t.forward(l)
        t.left(90)
    t.end_fill()

# Function for a Rectangle
def rectangle(w, c, l):
    t.color(c)
    t.begin_fill()
    for i in range(2):
        t.forward(l)
        t.left(90)
        t.forward(w)
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

# Grass Function
def gra(c):
    t.setheading(90)
    t.color(c)
    t.begin_fill()
    for i in range(23):
        t.forward(50)
        t.right(165)
        t.forward(52)
        t.left(165)
    t.end_fill()
        
    

# Function to position the turtle
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Drawing shapes
move_to(-100, -100)
square(300, 'blue')
move_to(-40, -100)
rectangle(150, 'yellow', 100)
move_to(80, 70)
square(100, 'light blue')
move_to(-100, 200)
triangle(300, 'yellow')
move_to(-100, -100)
gra('green')

sc.mainloop()
