# My Final One, It's Been A Long Journey, Hasn't It?
# See You Next Course!

# Importing Libraries
import turtle
import random
import time

# Time Variables
delay = 0.1
segment = []
score = 0
high_score = 0

# Creating A Turtle And Background
sc = turtle.Screen()
sc.bgcolor('blue')
snake = turtle.Turtle()
snake.color('green')
snake.shape('square')
snake.direction = 'stop'
snake.penup()
snake.goto(0, 180)

# Move Function
def move():
  # Move Up
  if snake.direction == 'up':
    y = snake.ycor()
    snake.sety(y + 20)
  
  # Move Down
  if snake.direction == 'down':
    y = snake.ycor()
    snake.sety(y - 20)
    
  # Move Right
  if snake.direction == 'right':
    x = snake.xcor()
    snake.setx(x + 20)
    
  # Move Left
  if snake.direction == 'left':
    x = snake.xcor()
    snake.setx(x - 20)

# Creating Input
# Go Up Function
def go_up():
  snake.direction = 'up'

# Go Down Function
def go_down():
  snake.direction = 'down'
  
# Go Right Function
def go_right():
  snake.direction = 'right'

# Go Left Function
def go_left():
  snake.direction = 'left'

sc.listen()
sc.onkey(go_up, 'w')
sc.onkey(go_down, 's')
sc.onkey(go_right, 'd')
sc.onkey(go_left, 'a')

# Apple Turtle
apple = turtle.Turtle()
apple.color('red')
apple.shape('circle')

# Pen Turtle
pen = turtle.Turtle()
pen.penup()
pen.goto(0, 100)
pen.hideturtle()
pen.write('score:0', align = 'center', font = ('Arial', 30, 'bold'))

# Apple And Snake Movement
while True:
  sc.update()
  move()
  time.sleep(delay)
  if snake.distance(apple)<20:
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    apple.penup()
    apple.goto(x, y)
  
   # Increasing The Snake Length
    ns = turtle.Turtle()
    ns.shape('square')
    ns.color('dark green')
    ns.penup()
    segment.append(ns)
    score = score + 1
    
    if score > high_score:
      high_score = score
    pen.clear()
    pen.write('score:{}'.format(score), align = 'center', font = ('Arial', 30, 'bold'))
      
# I Have No Idea
  for i in range(len(segment)-1, 0, -1):
    x = segment[i - 1].xcor()
    y = segment[i - 1].ycor()
    segment[i].goto(x, y)
  
  if len(segment)>0:
    x = snake.xcor()
    y = snake.ycor()
    segment[0].goto(x, y)
