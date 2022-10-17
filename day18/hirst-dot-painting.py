import turtle as t
import random
colors = [(181, 102, 22), (45, 104, 145), (128, 200, 187), (211, 161, 12), (14, 35, 60), (242, 83, 37), (210, 146, 117), (153, 185, 212), (238, 75, 91), (181, 46, 135), (97, 180, 47), (21, 91, 67), (253, 218, 0), (244, 217, 40), (62, 98, 85), (207, 136, 153)]

t.setup (width=600, height=600, startx=500, starty=0)
tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)
t.hideturtle()
# TODO 10*10 table
y = -250
for _ in range(10):
    tim.penup()
    tim.setpos(-250, y)
    y += 50
    for _ in range(10):
        r = random.choice(colors)
        tim.dot(20, r)
        tim.forward(50)

screen = t.Screen()
screen.exitonclick()