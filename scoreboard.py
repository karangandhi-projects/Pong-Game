from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(position)
        self.points = -1
        self.update_score()

    def update_score(self):
        self.points += 1
        self.clear()
        self.write(arg=f"{self.points}", move=False, align=ALIGNMENT, font=FONT)