import turtle as t
import random
from colors import COLORS
tim = t.Turtle()
tim.shape("turtle")
tim.color("blue")
tim.pensize(10)

def ran_orient(turtle):
    return random.choice([turtle.right(45), turtle.left(45)])

def ran_move(turtle):
    f = turtle.forward(30)
    b = turtle.back(30)
    return random.choice([b, f])

a = [0, 90, 180, 270]
while True:
    b = random.choice(a)
    tim.setheading(b)
    tim.forward(30)
    r = random.choice(COLORS)
    tim.pencolor(r)


# s=3
# for _ in range(8):
#     for _ in range(s):
#         tim.forward(30)
#
#     s += 1
#     r = random.choice(COLORS)
#     tim.pencolor(r)





screen = t.Screen()
screen.exitonclick()