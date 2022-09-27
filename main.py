"""This app allows the user to play Snake using the `turtle` library."""
import turtle as t
import time
from snake import Snake

# Create a black screen using Screen class.
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create a three segment Snake.
snake = Snake()

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

# TODO Control the snake.


# TODO Detect collision with food.

# TODO Create a scoreboard.

# TODO Detect collision with wall.

# TODO Detect collision with tail.

screen.exitonclick()
