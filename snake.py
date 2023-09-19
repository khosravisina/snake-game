from turtle import Turtle

# Constants
DOWN = 270
RIGHT = 0
UP = 90
LEFT = 180
MOVE_DISTANCE = 20

class Snake():
    """A class to represent the snake."""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the snake."""
        for i in range(3):
            new_turtle = Turtle('square')
            new_turtle.penup()
            new_turtle.color('white')
            new_turtle.goto((-1*20), 0)
            self.segments.append(new_turtle)
    def move(self):
        """Moves the snake."""
        for seg in range(len(self.segments) - 1, 0, -1):
            pos = self.segments[seg - 1].pos()
            self.segments[seg].goto(pos)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """Moves the snake up."""
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        """Moves the snake down."""
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        """Moves the snake right."""
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        """Moves the snake left."""
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def check(self):
        """Checks if the snake has collided with itself or the wall."""
        if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > +290 or self.head.ycor() < -290 or snake.detect_hit() == False:
            return False
        else:
            True

    def rise_snake(self):
        """Adds a new segment to the snake."""
        new_turtle = Turtle('square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(new_turtle)

    def detect_hit(self):
        """Checks if the snake has collided with itself."""
        for seg in self.segments[1:]:
            if self.head.distance(seg) < 10:
                return False




