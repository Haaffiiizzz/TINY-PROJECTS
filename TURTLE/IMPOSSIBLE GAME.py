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
playerOne.goto(-270,0)
playerOne.shape("square")
playerOne.direction = "Stop"
playerOne.color("blue")

playerTwo = turtle.Turtle()
playerTwo.penup()
playerTwo.goto(270,0)
playerTwo.shape("square")
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
    


screen.listen()
screen.onkeypress(goUp(playerOne), "Up")
screen.onkeypress(goDown(playerOne), "Down")
screen.onkeypress(goUp(playerTwo), "w")
screen.onkeypress(goDown(playerTwo), "z")




while True:
    screen.update()
    

    moveBar(playerOne)
    moveBar(playerTwo)
    time.sleep(0.2)


screen.mainloop()       
