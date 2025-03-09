from turtle import Turtle

#INIT_COORDS = (100,300)
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed =0.1
        #self.setheading(self.towards(INIT_COORDS))

    def move(self):
        #self.forward(10)
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)

    def bounce_y(self):
        #self.setheading((self.heading() - 90)%360)
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()

