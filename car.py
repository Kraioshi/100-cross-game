from turtle import Turtle
import random

COLORS = ['blue', 'red', 'green', 'yellow', 'purple']
X_POSITION = [*range(-150, 3000, 50)]
Y_POSITION = [*range(-195, 270, 60)]
SECONDARY_X = [*range(300, 1500, 50)]
SPEED = 0.25


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1

    def create_car(self):
        self.penup()
        self.shape('square')
        self.speed('slowest')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.goto(random.choice(X_POSITION), random.choice(Y_POSITION))

    def move_car(self):
        speed = 1 * self.level
        self.forward(speed)

    def level_up(self):
        self.level += 1

    def level_checker(self):
        return self.level

    def create_secondary(self):
        super().__init__()

        self.penup()
        self.shape('square')
        self.speed('slowest')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.goto(random.choice(SECONDARY_X), random.choice(Y_POSITION))


if __name__ == '__main__':
    print(X_POSITION)
    print(Y_POSITION)
