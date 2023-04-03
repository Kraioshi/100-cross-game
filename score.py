from turtle import Turtle

FONT = ('Courier', 42, 'bold')
ALIGNMENT = 'center'


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor('white')
        self.goto(0, 260)

    def game_over(self):
        self.write("GAME OVER", font=FONT, align=ALIGNMENT)

    def score(self):
        pass