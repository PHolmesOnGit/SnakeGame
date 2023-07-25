# Welcome to the Snake Game! Run the code to start the snake game and use WASD to move your snake. Enjoy! #

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game V1.0")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
# Key controls
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

game_is_on = True
# sets the game state to "True" will continually move the snake forward by 20 pixels till False
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        # detects collision with food object and creates a new food object and increases score
        food.refresh()
        snake.extend()
        scoreboard.point()

    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        # detects collision with walls
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:-1]:
        # detects collision with the snake body
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
