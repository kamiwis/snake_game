"""Food Class

This script creates a class called Food for the Snake Game that inhertis from Turtle class.
This script requires `turtle` module to be imported.

This script can be imported as a module containing the Snake class.
"""
from turtle import Turtle
import random

class Food(Turtle):
    """
    A class used to represent snake Food in Snake Game.
    This class inherits from the Turtle class.
    ...
    Attributes
    __________
    
    Methods
    _______
    
    """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
