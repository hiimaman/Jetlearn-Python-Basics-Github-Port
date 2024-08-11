# I worked my ass off (hope dad didn't hear that)
# This was practice for the while loop in guessing game

import turtle

# Print numbers from 1 to 10 using while loop
print("Numbers from 1 to 10 (while loop):")
i = 1
while i <= 10:
    print(i)
    i += 1

# Print numbers from 1 to 10 using for loop
print("\nNumbers from 1 to 10 (for loop):")
for i in range(1, 11):
    print(i)

# Print even numbers from 1 to 50 using while loop
print("\nEven numbers from 1 to 50 (while loop):")
i = 2
while i <= 50:
    print(i)
    i += 2

# Print even numbers from 1 to 50 using for loop
print("\nEven numbers from 1 to 50 (for loop):")
for i in range(2, 51, 2):
    print(i)

# Setup the screen for turtle graphics
screen = turtle.Screen()
turtle.screensize(1.0, 1.0)
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.speed(5)  # Set the speed of the turtle


# Function to draw a circle
def draw_circle():
    t.color("blue")
    t.circle(100)


# Function to draw a square
def draw_square():
    t.color("green")
    for _ in range(4):
        t.forward(100)
        t.right(90)


# Function to draw a triangle
def draw_triangle():
    t.color("red")
    for _ in range(3):
        t.forward(100)
        t.right(120)


# Main function to draw all shapes
def draw_shapes():
    draw_circle()
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    draw_square()
    t.penup()
    t.goto(150, 0)
    t.pendown()
    draw_triangle()


# Call the main function
draw_shapes()

# Finish turtle graphics
turtle.done()
