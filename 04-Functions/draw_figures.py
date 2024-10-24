import turtle
from figures import draw_square, draw_rectangle, draw_triangle

pen = turtle.Turtle()
pen.speed(5)

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

pen.penup()
pen.goto(-100, 100)
pen.down()
draw_square(100, pen)
pen.penup()
pen.goto(-100, -5)
pen.pendown()
draw_rectangle(200, 100, pen)
pen.penup()
pen.goto(-100, -110)
pen.pendown()
draw_triangle(100, pen)


pen.penup()
pen.goto(100, 105)
pen.down()
draw_square(100, pen)
pen.penup()
pen.goto(105, -5)
pen.pendown()
draw_rectangle(200, 100, pen)
pen.penup()
pen.goto(105, -110)
pen.pendown()
draw_triangle(100, pen)

pen.hideturtle
window.mainloop

