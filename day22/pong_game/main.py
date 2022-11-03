from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("MG Pong Game")
game_is_on = True
screen.tracer(0)

r_paddle = Paddle(350, "red")
l_paddle = Paddle(-350, "blue")
ball = Ball()
scoreboard = Scoreboard()
scoreboard.refresh()
screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.paddle_bounce()
    if (ball.xcor() > 380):
        scoreboard.r_score += 1
        scoreboard.refresh()
        ball.home()
        ball.x_move *= -1
        ball.move_speed = 0.1
    if (ball.xcor() < -380):
        scoreboard.l_score += 1
        scoreboard.refresh()
        ball.home()
        ball.x_move *= -1
        ball.move_speed = 0.1



screen.exitonclick()