from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,positon):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(positon)

    def up(self):
        self.goto(self.xcor(),self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(),self.ycor() - 20)


