from turtle import Turtle
import random
import scoreboard
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.carspeed = STARTING_MOVE_DISTANCE
    def add_car(self):
        random_generator = random.randint(1, 6)
        if random_generator == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            ran_y = random.randint(-250, 250)
            new_car.goto(320, ran_y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            new_x = car.xcor() - self.carspeed
            car.goto(new_x, car.ycor())

    def level_up(self):
        self.carspeed += MOVE_INCREMENT