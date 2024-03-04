import turtle
import time
import random
screen = turtle.Screen()
screen.title("Impossible Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

ball = turtle.Turtle()
ball.speed(10)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0,0)
ball.direction = random.choice(["up", "left", "right", "down"])

bar = turtle.Turtle()
bar.penup()
bar.goto(0,0)
bar.shape("turtle")
bar.direction = "Stop"

def goUp():
    bar.direction = "up"

def goDown():
    bar.direction = "down"

def goRight():
    bar.direction = "right"

def goLeft():
    bar.direction = "left"    

def moveBar():
    if bar.direction == "up":
        bar.sety(bar.ycor() + 10)
    if bar.direction == "down":
        bar.sety(bar.ycor() - 20)
    if bar.direction == "right":
        bar.setx(bar.xcor() + 20)
    if bar.direction == "left":
        bar.setx(bar.xcor() - 20)           

def moveBall():
    if ball.direction == "up":
        ball.sety(bar.ycor() + 10)
    if ball.direction == "down":
        ball.sety(bar.ycor() - 20)
    if ball.direction == "right":
        ball.setx(bar.xcor() + 20)
    if ball.direction == "left":
        ball.setx(bar.xcor() - 20)  
    if ball.xcor() > 295 or ball.xcor() < -295 or ball.ycor() > 295 or ball.ycor() < -295:
        ball.direction = random.choice(["up", "left", "right", "down"])    


screen.listen()
screen.onkeypress(goUp, "Up")
screen.onkeypress(goDown, "Down")
screen.onkeypress(goLeft, "Left")
screen.onkeypress(goRight, "Right")


while True:
    screen.update()
    moveBall()
    
    if ball.xcor() > 295 or ball.xcor() < -295 or ball.ycor() > 295 or ball.ycor() < -295:
        ball.direction = random.choice(["up", "left", "right", "down"])


screen.mainloop()       
