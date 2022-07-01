from turtle import Turtle, Screen
import random

my_turtle = Turtle()

def choose_way():
    directions = [0, 90, 180, 270]
    my_turtle.setheading(random.choice(directions))

def choose_color():
    R = random.random()
    G = random.random()
    B = random.random()
    my_turtle.color(R, G, B)

my_turtle.width(10)
my_turtle.speed(10)

for i in range(200):
    choose_color()
    my_turtle.forward(30)
    choose_way()

screen = Screen()
screen.exitonclick()