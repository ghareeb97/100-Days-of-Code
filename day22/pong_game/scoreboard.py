from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 240)
        self.r_score = 0
        self.l_score = 0

    def refresh(self):
        self.clear()
        self.write(f"{self.r_score}  {self.l_score} ", False, align= ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= ALIGNMENT, font=FONT)
