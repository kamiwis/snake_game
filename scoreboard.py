"""Scoreboard Class

This script creates a class called Scoreboard for the Snake Game that inhertis from Turtle class.
This script requires `turtle` module to be imported.

This script can be imported as a module containing the Snake class.
"""
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    """
    A class used to represent a scoreboard in the Snake Game.
    ...
    Attributes
    __________
    score: keeps track of score in Snake Game
    Methods
    _______
    update_score()
        Adds scoreboard to game screen
    increase_score()
        Increases the score when snake collides with food
    game_over()
        Ends game when snake collides with wall or self.
    """
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        """Adds scoreboard to game screen."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        """Increases the score when snake collides with food."""
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        """Ends game when snake collides with wall or self."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
