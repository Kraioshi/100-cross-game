from turtle import Turtle, Screen

from mob import Mob
from car import Car
from score import Score

mob = Mob()
game_over = Score()
score = Score()

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor('black')
screen.tracer(0)

game_is_on = True


def end_game():
    global game_is_on
    game_is_on = False


screen.listen()
screen.onkey(key='q', fun=end_game)
screen.onkey(key='w', fun=mob.move_up)

car_park = []
for _ in range(1, 75, 1):
    car = Car()
    car.create_car()
    car_park.append(car)


difficulty = 1
while game_is_on:

    # Setting cars in motion
    for cars in car_park:
        cars.move_car()

    # Scoreboard
    score.update_score(difficulty)

    # level up
    if mob.ycor() >= 280:
        for car in car_park:
            car.level_up()
        mob.goto(0, -290)
        difficulty += 1
        score.update_score(difficulty)
        print('dif_update', difficulty)

    # Respawning cars
    for car in car_park:
        if car.xcor() < -400:
            car.hideturtle()
            current_level = car.level
            car_park.remove(car)

            car = Car()
            car.create_secondary()
            car.level = current_level
            car_park.append(car)

    # collision with cars:
    for cars in car_park:
        if mob.distance(cars) < 25:
            game_over.game_over()
            game_is_on = False

    screen.update()
screen.exitonclick()