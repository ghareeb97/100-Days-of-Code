import turtle as t
import random
from colors import COLORS
tim = t.Turtle()
tim.shape("turtle")
tim.color("blue")
# tim.pensize(10)

# a = [0, 90, 180, 270]
# while True:
#     b = random.choice(a)
#     tim.setheading(b)
#     tim.forward(30)
#     r = random.choice(COLORS)
#     tim.pencolor(r)
tim.speed("fastest")
def draw_sprirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        r = random.choice(COLORS)
        tim.pencolor(r)
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_sprirograph(10)

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