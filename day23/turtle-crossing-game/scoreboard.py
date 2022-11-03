from turtle import Turtle
FONT = ("Courier", 20, "bold")
ALIGNMENT = "left"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.level = 1

    def refresh(self):
        self.clear()
        self.write(f"Level: {self.level} ", False, align= ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align= "center", font=FONT)
