from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counter_clockwise():
    tim.right(10)

def move_clockwise():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_counter_clockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear, "c")

screen.exitonclick()