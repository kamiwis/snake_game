"""This app allows the user to play Snake using the `turtle` library."""
from turtle import Screen
import time
from snake import Snake
from food import Food

# Create a black screen using Screen class.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create a three segment Snake.
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move the snake.
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()

# TODO Create a scoreboard.

# TODO Detect collision with wall.

# TODO Detect collision with tail.

screen.exitonclick()
