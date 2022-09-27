"""This app allows the user to play Snake using the `turtle` library."""
import turtle as t
import time
#from helpers import turn_left

# Create a black screen using Screen class.
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create a snake body using Turtle class.
# stretch = 3
# segment = t.Turtle(shape="square")
# segment.color("white")
# segment.turtlesize(stretch_len=stretch)

# starting_position = [(0, 0), (-20, 0), (-40, 0)]

# segments = []

for pos in starting_position:
    new_segment = t.Turtle("square")
    new_segment.color("white")
    new_segment.pu()
    new_segment.goto(pos)
    segments.append(new_segment)

# Move the snake.
game_is_on = True
while game_is_on:
    screen.update()
    # segment.fd(20)
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

# TODO Control the snake.
screen.listen()
screen.onkey()

# TODO Detect collision with food.

# TODO Create a scoreboard.

# TODO Detect collision with wall.

# TODO Detect collision with tail.

screen.exitonclick()
