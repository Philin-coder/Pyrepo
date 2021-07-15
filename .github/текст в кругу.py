from turtle import Turtle, Screen
 
RADIUS = 50
 
FONT_SIZE = 18
 
FONT = ("Arial", FONT_SIZE, "normal")
 
def draw_node(turtle, text, x, y):
    turtle.up()
    turtle.goto(x, y - RADIUS)
    turtle.down()
    turtle.circle(RADIUS)
    turtle.up()
    turtle.goto(x, y - FONT_SIZE // 2)
    turtle.write(text, align="center", font=FONT)
 
def draw_design(turtle):
 
    turtle.color("white")
    turtle.pensize(4)
 
    draw_node(turtle, "S0", -100, 100)
 
    draw_node(turtle, "S1", 100, 100)
 
screen = Screen()
screen.bgcolor("blue")
 
yertle = Turtle(shape="turtle")
 
draw_design(yertle)