import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

STARTING_POSITIONS_P2  = (350,0)
STARTING_POSITIONS_P1  = (-350,0)
SCORE_POSITION_L = (-100,200)
SCORE_POSITION_R = (100,200)
SPEED = ["slowest","slow","normal","fast","fastest"]


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle_P1 = Paddle(STARTING_POSITIONS_P1)
r_paddle_P2 = Paddle(STARTING_POSITIONS_P2)
ball = Ball()
score_l = Scoreboard(SCORE_POSITION_L)
score_r = Scoreboard(SCORE_POSITION_R)

screen.listen()
screen.onkey(l_paddle_P1.up, "w")
screen.onkey(l_paddle_P1.down, "s")
screen.onkey(r_paddle_P2.up,"Up")
screen.onkey(r_paddle_P2.down,"Down")


speed = 0
ball.speed(SPEED[speed])

game_over = False
while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle_P2) < 50 and ball.xcor() > 320 or ball.distance(l_paddle_P1) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_ball()
        score_l.update_score()

    if ball.xcor() < -380:
        ball.reset_ball()
        score_r.update_score()



screen.exitonclick()