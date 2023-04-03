from turtle import Turtle


class Mob(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.goto(x=0, y=-290)

    def move_up(self):
        self.forward(30)
