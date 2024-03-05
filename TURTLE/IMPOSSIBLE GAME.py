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
ball.direction = "right"

playerOne = turtle.Turtle()
playerOne.penup()
playerOne.goto(270,0)
playerOne.shape("square")
playerOne.shapesize(stretch_wid=5, stretch_len=1)
playerOne.direction = "Stop"
playerOne.color("blue")

playerTwo = turtle.Turtle()
playerTwo.penup()
playerTwo.goto(-270,0)
playerTwo.shape("square")
playerTwo.shapesize(stretch_wid=5, stretch_len=1)
playerTwo.direction = "Stop"
playerTwo.color("red")

def goUp(player):
    player.direction = "up"

def goDown(player):
    player.direction = "down"
 

def moveBar(player):
    if player.direction == "up":
        player.sety(player.ycor() + 20)
    if player.direction == "down":
        player.sety(player.ycor() - 20)


def moveBall():
    if ball.direction == "right":
        ball.setx(ball.xcor()+30)
    if ball.direction == "left":
        ball.setx(ball.xcor()-30)    


screen.listen()
screen.onkeypress(lambda: goUp(playerOne), "Up")
screen.onkeypress(lambda: goDown(playerOne), "Down")
screen.onkeypress(lambda: goUp(playerTwo), "w")
screen.onkeypress(lambda: goDown(playerTwo), "z")


playerOneScore = 0
playerTwoScore = 0

while True:
    screen.update()
    if ball.distance(playerOne) < 30:
        ball.direction = "left"
    if ball.distance(playerTwo) < 30:
        ball.direction = "right"    
    moveBall()
    moveBar(playerOne)
    moveBar(playerTwo)
    time.sleep(0.1)

screen.mainloop()       
