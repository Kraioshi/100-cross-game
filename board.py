from turtle import Turtle


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(2)
        self.penup()

    def draw(self):
        self.goto(0, -300)
        self.pendown()
        self.goto(-300, -300)
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(0, -300)