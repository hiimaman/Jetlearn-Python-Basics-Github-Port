# I just went to the fire work show file and changed the code to make it squares

# Setting up libraries
import turtle
import random

# Creating Pen And Background
t = turtle.Turtle()
t.pensize(3)
t.pencolor('white')
t.speed(100)
sc = turtle.Screen()
sc.bgcolor('black')
sc.screensize(1.0, 1.0)
sc.colormode(255)

# Square function
def square(a):
  t.forward(a)
  t.right(90)

# Loop
for i in range(50):
  # Defining X And Y
  x = random.randint(-500, 500)
  y = random.randint(-500, 500)
  # Making The Cursor Move Around The Screen
  t.penup()
  t.goto(x, y)
  t.pendown()
  # Color Variables RGB
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  t.color(r, g, b)
  # I Have NO Idea...
  x = random.randint(60, 80)
  y = random.randint(60, 80)
  # For Loop For Squares
  for _ in range(4):
    a = random.randint(80, 100)
    square(a)

# Make Sure The Screen Works
sc.mainloop()
