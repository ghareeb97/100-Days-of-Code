from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=450, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race Enter a color: ")
screen.title("Welcome To The Turtle Race!")
zohlof = Turtle()
zahlouf = Turtle()
zalahlaf = Turtle()
zahloufa = Turtle()

turtles = [zohlof, zahlouf, zalahlaf, zahloufa]
colors = ["blue", "purple", "green", "pink"]
h = 100
for i in range(4):
    turtles[i].shape("turtle")
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(-200, h)
    h -= 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The winner is {winner} turtle.")
            else:
                print(f"You've lost! The winner is {winner} turtle.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()