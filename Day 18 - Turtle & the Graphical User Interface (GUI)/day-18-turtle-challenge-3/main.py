from turtle import Turtle, Screen
import random

my_turtle = Turtle()

num_lados = 3
num_figuras = 7

def def_color():
    R = random.random()
    G = random.random()
    B = random.random()
    my_turtle.color(R, G, B)

for i in range(num_figuras):
    def_color()
    
    for i in range(num_lados):
        my_turtle.forward(100)
        my_turtle.right(360 / num_lados)
    
    num_lados += 1

screen = Screen()
screen.exitonclick()