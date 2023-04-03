from turtle import Turtle


class Mob(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.goto(x=0, y=-280)

    def move_up(self):
        self.forward(20)
