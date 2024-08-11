# Star

import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(1.0, 1.0)
pc = input("Enter in a pen colour. ")
bc = input("Enter in a background colour. ")
t.pencolor(pc)
screen.bgcolor(bc)

t.speed(999)
t.pensize(3)

x = 0
while(x < 20):
  t.forward(260)
  t.left(190)
  x += 1
  

screen.mainloop()
