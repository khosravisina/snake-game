from turtle import Turtle

# Constants
FONT = ("Arial", 16, "normal")
END_FONT = ("Arial", 30, "normal")

class Score(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.score_num = 0.0
        self.goto(0, 270)
        self.color('white')
        self.write(arg=f'SCORE: {self.score_num}',align='center', font=FONT)

        self.hideturtle()

    def reset_score(self):
        self.clear()
        self.score_num += 1
        self.write(arg=f'SCORE: {self.score_num}',align='center', font=("Arial", 16, "normal"))

    def over(self):
        self.clear()
        self.goto(0, 0)
        self.write('Game is over', font=END_FONT, align='center')