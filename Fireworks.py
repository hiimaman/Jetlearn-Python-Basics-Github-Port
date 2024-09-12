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



for i in range(50):
  x = random.randint(-500, 500)
  y = random.randint(-500, 500)
  t.penup()
  t.goto(x, y)
  t.pendown()
  # Color Variables RGB
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  t.color(r, g, b)
  i = 36
  while i > 0:
    a = random.randint(60, 80)
    t.forward(a)
    t.backward(a)
    t.right(10)
    i -= 1
  
sc.mainloop()
