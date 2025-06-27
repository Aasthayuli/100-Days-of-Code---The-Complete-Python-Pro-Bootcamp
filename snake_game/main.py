from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


# Create Snakes
my_snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")

# Moves Snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    # Detect collision with food.
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in my_snake.segments[1:]:
    # if head collides with any segment in the tail:
        # trigger game over
        if my_snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()