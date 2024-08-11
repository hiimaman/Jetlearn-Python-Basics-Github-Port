# Desert Scenery

import turtle

t = turtle.Turtle()
sc = turtle.Screen()
sc.setup(1.0, 1.0)
sc.bgcolor("sky blue")
t.speed(100)

#blazing sun
t.penup()
t.goto(100, 150)
t.pendown()
t.color("yellow")
t.begin_fill()
for i in range(4):
  t.forward(60)
  t.right(90)
t.end_fill()
t.penup()
t.goto(130, 165)
t.pendown()
t.right(45)
t.begin_fill()
for i in range(4):
  t.forward(60)
  t.right(90)
t.end_fill()

#pyramid
t.left(45)
t.penup()
t.goto(-100, -40)
t.pendown()
t.color("orange")
t.begin_fill()
for i in range(3):
  t.forward(200)
  t.left(120)
t.end_fill()

#ground
t.pensize(3)
t.backward(500)
t.color("orange")
t.pencolor("purple")
t.begin_fill()
for i in range(2):
  t.forward(1500)
  t.right(90)
  t.forward(150)
  t.right(90)
t.end_fill()

#function for straight lines
def go_to(x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()

#pen lines
t.pensize(3)

go_to(-30, 80)
t.forward(60)

go_to(-53, 40)
t.forward(110)

go_to(-75, 0)
t.forward(155)

#hump
t.color("orange")
go_to(180,-50)
t.left(90)
t.begin_fill()
for i in range(19):
  t.forward(10)
  t.right(10)
t.end_fill()

#cactus
t.color("green")
t.begin_fill()
t.left(90)
go_to(250, 0)
t.left(100)
t.begin_fill()
t.forward(50)
t.right(90)
t.circle(20, 90)
t.forward(10)
t.circle(20, 90)
t.left(90)
t.forward(20)
t.left(180)
t.forward(20)
t.circle(20, 180)
t.forward(20)
t.right(180)
t.forward(20)
t.left(90)
t.circle(20, 180)
t.right(90)
t.forward(50)
t.left(90)
t.forward(40)
t.left(90)
t.forward(10)
t.end_fill()

sc.mainloop()
