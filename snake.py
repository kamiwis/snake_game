"""Snake Class

This script creates a Snake class for the Snake Game.
This script requires `turtle` module to be imported.

This script can be imported as a module containing the Snake class.
"""
import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake():
    """
    A class used to represent a Snake in the Snake Game
    ...
    Attributes
    __________
    segments: list of Turtle class squares
    
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
            new_segment = t.Turtle("square")
            new_segment.color("white")
            new_segment.pu()
            new_segment.goto(pos)
            self.segments.append(new_segment)
    
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
        self.head.setheading(90)
    
    def down(self):
        """Turns the snake down - 270 degrees"""
        self.head.setheading(270)
    
    def left(self):
        """Turns the snake left - 180 degrees"""
        self.head.setheading(180)
    
    def right(self):
        """Turns the snake right - 0 degrees"""
        self.head.setheading(0)
