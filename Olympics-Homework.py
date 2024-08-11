# I admit, I used chatgpt

import turtle

def draw_ring(t, color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.circle(50)

def draw_olympic_rings():
    screen = turtle.Screen()
    screen.title("Olympic Rings")

    t = turtle.Turtle()
    t.width(5)

    # Coordinates and colors for the rings
    colors = ["blue", "black", "red", "yellow", "green"]
    positions = [(-120, 0), (0, 0), (120, 0), (-60, -60), (60, -60)]

    for color, (x, y) in zip(colors, positions):
        draw_ring(t, color, x, y)

    t.hideturtle()
    screen.mainloop()

# Run the function to draw the rings
draw_olympic_rings()
