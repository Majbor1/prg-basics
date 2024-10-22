import turtle
def draw_square(lenght):
    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Draw a square
    for i in range(4):
        pen.forward(lenght)
        pen.right(90)

    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()

def draw_triangle(lenght):
    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Draw a square
    for i in range(3):
        pen.forward(lenght)
        pen.right(120)

    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()

def draw_rectangle(lenght_a, lenght_b):
    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Draw a square
    for i in range(4):
        if i % 2 == 0:
            pen.forward(lenght_a)
            pen.right(90)
        else:
            pen.forward(lenght_b)
            pen.right(90)

    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()