# Snowman

import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(1.0,1.0)
screen.bgcolor("blue")
t.pencolor("red")
t.shape("turtle")

x = 0
z =
for i in range(36):
  t.forward(15)
  t.right(10)

for i in range(36):
  t.forward(12)
  t.left(10)


t.penup()
t.goto(-25,95)
t.pendown()
t.dot(15,"white")

t.penup()
t.goto(25,95)
t.pendown()
t.dot(15,"white")

t.penup()
t.goto(-25,50)
t.pendown()
t.right(90)
t.circle(30,180)

screen.mainloop()
