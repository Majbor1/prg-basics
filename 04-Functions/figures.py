import turtle

def draw_square(lenght, pen):
    for _ in range(4):
        pen.forward(lenght)
        pen.right(90)
    

def draw_triangle(lenght, pen):
    for _ in range(3):
        pen.forward(lenght)
        pen.right(120)
    

def draw_rectangle(lenght_a, lenght_b, pen):
    for _ in range(2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)
    