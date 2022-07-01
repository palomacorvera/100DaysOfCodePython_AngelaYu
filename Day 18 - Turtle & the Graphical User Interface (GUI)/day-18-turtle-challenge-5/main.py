from turtle import Turtle, Screen
import random

my_turtle = Turtle()

def choose_color():
    R = random.random()
    G = random.random()
    B = random.random()
    my_turtle.color(R, G, B)

my_turtle.speed("fastest")
size_of_gap = 5

for i in range(int(360 / size_of_gap)):
    choose_color()
    my_turtle.circle(50)
    my_turtle.left(size_of_gap)

screen = Screen()
screen.exitonclick()