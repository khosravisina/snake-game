from turtle import Turtle
import random

class Food(Turtle):
    """A class to represent the food."""
    def __init__(self):
        """Initializes the food."""
        Turtle.__init__(self)
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        x_new = random.randint(-270, 270)
        y_new = random.randint(-270, 270)
        self.goto(x_new, y_new)

    def reset_pos(self):
        """Resets the position of the food."""
        x_new = random.randint(-270, 270)
        y_new = random.randint(-270, 270)
        self.goto(x_new, y_new)


