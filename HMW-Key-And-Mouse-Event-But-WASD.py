# Same, but with WASD

 # Import Libraries
import turtle
import random

# Setting Up Turtle
sc = turtle.Screen()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

# Creating Shapes
t1.shape('turtle')
t2.shape('turtle')
t3.shape('turtle')

# Creating Turtle Colours
t1.color('red')

# Creating Text
t2.write('start',font=('courier',30,'bold'),align='center' )


# Creating Functions: Preperation
x = input('how many steps would you like your turtle to move?\n')

# Creating Functions: The Actual Stuff

# Go Forward
def go_forward():
  t1.forward(x)
  
# Go Right
def go_right():
  t1.setheading(0)
  
# Go Up
def go_up():
  t1.setheading(90)
  
# Go Down
def go_down():
  t1.setheading(270)
  
# Go Left
def go_left():
  t1.setheading(180)

sc.listen()
sc.onkey(go_forward, 'space')
sc.onkey(go_right, 'D')
sc.onkey(go_left, 'A')
sc.onkey(go_down, 'S')
sc.onkey(go_up, 'W')

# Mouse Part
# On Drag
def on_click(x, y):
  # Turn Off Tracer
  sc.tracer(0)      
  # Makes t1 Face Where You Clicked      
  t1.setheading(t1.towards(x, y))
  t1.goto(x, y)
  # Now It Will Draw A Line
  sc.tracer(1)
  # Print the position of t1
  print(t1.pos())
  if t1.pos()>(100, 30):
    t1.write('You Won', font = ('arial', 36, 'bold'), align = ('right'))
  
# On Drag
def on_drag(x, y):
  # Refer To Previous Comments (On_Click)
  sc.tracer(0)
  t1.goto(x, y)
  sc.tracer(1)
  
# Call The Functions
sc.onclick(on_click)
t1.ondrag(on_drag)
t2.goto(100, 30)

for i in range(100):
  t3.forward(100)
  t3.right(36)
  t3.backward(100)
  t3.forward(100)
  t3.forward(50)
  t3.right(90)
  t3.backward(20)
