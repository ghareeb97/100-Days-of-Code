import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("MG Turtle Crossy Road")
screen.tracer(0)
player = Player()

screen.listen()
screen.onkey(player.move, "Up")
game_is_on = True
cars = CarManager()
scoreboard = Scoreboard()
scoreboard.refresh()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.add_car()
    cars.move()
    for car in cars.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.finish_line_reached():
        scoreboard.level += 1
        scoreboard.refresh()
        cars.level_up()

screen.exitonclick()