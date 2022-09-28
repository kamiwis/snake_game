"""Snake Class

This script creates a Snake class for the Snake Game.
This script requires `turtle` module to be imported.

This script can be imported as a module containing the Snake class.
"""
import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    """
    A class used to represent a Snake in the Snake Game
    ...
    Attributes
    __________
    segments: list of Turtle class squares
    head: first segment of snake body
    Methods
    _______
    create_snake()
        Creates a snake made of 3 square segments from Turtle class
    move()
        Starts moving the snake toward the right at a constant distance
    up()
        Turns the snake up - 90 degrees
    down()
        Turns the snake down - 270 degrees
    left()
        Turns the snake left - 180 degrees
    right()
        Turns the snake right - 0 degrees
    add_segement()
        Adds segnent to snake.
    extend()
        Extends snake by adding segment.
    """
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates a snake with 3 white square segments from Turtle class.
        Uses the STARTING_POSITION constant in order to space segments.
        Places segments in the correct position.
        """
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def move(self):
        """Moves the snake at a constant MOVE_DISTANCE.
        Takes into consideration that the individual segments need to trail behind eachother.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Turns the snake up - 90 degrees"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turns the snake down - 270 degrees"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turns the snake left - 180 degrees"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turns the snake right - 0 degrees"""
        if self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)

    def add_segment(self, pos):
        """Adds segnent to snake."""
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.goto(pos)
        self.segments.append(new_segment)
        
    def extend(self):
        """Extends snake by adding segment."""
        self.add_segment(self.segments[-1].position())
