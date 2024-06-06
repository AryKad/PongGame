import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

ball = Ball()
sb = ScoreBoard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

game_on = True
while game_on:
    time.sleep(ball.spd)
    screen.update()
    ball.move()

    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    # paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()
        sb.l_inc()

    if ball.xcor() < -380:
        ball.reset_pos()
        sb.r_inc()
screen.exitonclick()