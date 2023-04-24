from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# Creating Screen
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title("Ping-Pong")
screen.listen()
screen.tracer(0)

# Creating Paddle
right_paddle=Paddle((350,0))
left_paddle=Paddle((-350,0))

#Creating Ball
ball=Ball()

# Creating Scoreboard
scoreboard=Scoreboard()

# Movement
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")

screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")

#Game Running
game_is_on=True
while(game_is_on):
    ball.move()
    screen.update() 
    # Detect Collision with the wall
    if (ball.ycor()> 280 or ball.ycor()<-280):
            ball.bounce_y()

    # Detect collision with right paddle
    if (ball.distance(right_paddle)<50 and ball.xcor()>320):
            ball.bounce_x()


    # Detect collision with right paddle 
    if (ball.distance(left_paddle)<50 and ball.xcor()<-320):
            ball.bounce_x()  
    
    # Right Overflow
    if (ball.xcor()>375):
        scoreboard.left_pt()
        ball.reset()

    # Left Overflow 
    if (ball.xcor()<-375):
        scoreboard.right_pt()
        ball.reset() 

    time.sleep(ball.move_speed)
screen.exitonclick()