from turtle import Turtle, Screen
from mob import Mob
from car import Car
from board import Board
import time

mob = Mob()

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor('black')
screen.tracer(0)

screen.listen()
screen.onkey(key='w', fun=mob.move_up)

car_park = []
for _ in range(1, 75, 1):
    car = Car()
    car.create_car()
    car_park.append(car)

game_is_on = True
while game_is_on:
    for cars in car_park:
        cars.move_car()
    for car in car_park:
        if car.xcor() < -290:
            car.hideturtle()
            car_park.remove(car)
            car = Car()
            car.create_secondary()
            car_park.append(car)
    screen.update()


screen.exitonclick()