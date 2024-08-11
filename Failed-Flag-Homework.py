# ChatGPT didn't come in touch this time

import turtle

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_crescent(x, y, radius):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(90)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(radius, -180)
    turtle.circle(radius // 2, 180)
    turtle.end_fill()

def draw_star(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(-72)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

def draw_pakistan_flag():
    turtle.speed(10)
    turtle.bgcolor("white")

    # Draw the green rectangle
    draw_rectangle("green", -150, 100, 300, 200)

    # Draw the white vertical stripe
    draw_rectangle("white", -150, 100, 60, 200)

    # Draw the crescent moon
    draw_crescent(-50, 30, 50)

    # Draw the star
    draw_star(10, 70, 40)

    turtle.hideturtle()
    turtle.done()

draw_pakistan_flag()
