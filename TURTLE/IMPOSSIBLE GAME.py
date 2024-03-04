import turtle
import time
screen = turtle.Screen()
screen.title("Impossible Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0,0)
ball.direction = "Stop"

screen.listen()
while True:
    screen.update()
