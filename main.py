from turtle import Turtle, Screen
from mob import Mob


mob = Mob()

screen = Screen()
screen.screensize(600, 600)
screen.tracer(0)

screen.listen()
screen.onkey(key='w', fun=mob.move_up)


game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()