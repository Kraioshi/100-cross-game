from turtle import Turtle

GO_FONT = ('Courier', 42, 'bold')
GO_ALIGNMENT = 'center'
FONT = ('Courier', 21, 'bold')
ALIGNMENT = 'left'


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor('white')

    def game_over(self):
        self.goto(0, 270)
        self.write("GAME OVER", font=GO_FONT, align=GO_ALIGNMENT)

    def update_score(self, difficulty):
        self.clear()
        self.goto(-370, 290)
        self.write(f"LEVEL {difficulty}", font=FONT, align=ALIGNMENT)

