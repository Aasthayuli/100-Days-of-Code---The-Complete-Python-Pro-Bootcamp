from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Pong")
screen.tracer(0)  # turns off the animation

paddle_l = Paddle((-350,0))
paddle_r = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect Right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

        # Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()