# The Full Thing, And My Second-To-Last Prohect On Python Basics

# Importing Libraries
import turtle
import random

# Screen
sc = turtle.Screen()
sc.bgcolor('blue')

# User Turtle
user = turtle.Turtle()
user.shape('turtle')
user.color('red')
user.penup()
user.goto(-180, 80)

# Move Right Function
def move_right():
  user.forward(10)

# Input
sc.listen()
sc.onkey(move_right, 'Right')

# Creating Lists For The Turtle
colors = ['black', 'orange', 'white', 'purple']
players = []

# For Loop
y_pos = -100
for i in colors:
  p1 = turtle.Turtle()
  p1.shape('turtle')
  # I Represents Colours Variables
  p1.color(i)
  p1.penup()
  p1.goto(-180, y_pos)
  players.append(p1)
  y_pos += 50

# Move Non-User-Controlled Players
def move_players():
  for i in players:
    steps = random.randint(1, 10)
    i.forward(steps)

# Game Loop Code
game_over = False
while not game_over:
  move_players()
  for i in players:
    if i.xcor()>=200:
      game_over = True
      if user.xcor()>i.xcor():
        winner = 'red'
      else:
        winner = i.color()[0] # Only Works On Replit Not Trinket
      break
  
# Display Win Text
if winner:
  turtle.write('The {} turtle wins'.format(winner), font = ('Arial', 36, 'bold'), align = 'center')
