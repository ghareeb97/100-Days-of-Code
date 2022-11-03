from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        ran_y = random.randint(-280, 280)
        self.goto(320, ran_y)

    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())


    def __init__(self):
        self.cars = []
        self.create_car()
        self.head = self.cars[0]

    def create_car(self):
        for position in STARTING_POSITION:
            self.add_car(position)

    def add_car(self, position):
        new_car = Turtle("square")
        new_car.color("white")
        new_car.penup()
        new_car.goto(position)
        self.cars.append(new_car)