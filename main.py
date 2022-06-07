from turtle import Screen
from paddle import Paddle
from balls import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
player1 = Paddle(350, 0)
player2 = Paddle(-350, 0)
ball = Ball()
score = ScoreBoard()

screen.onkeypress(player1.move_up, "Up")
screen.onkeypress(player1.move_down, "Down")

screen.onkeypress(player2.move_up, "w")
screen.onkeypress(player2.move_down, "s ")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce()
    if ball.distance(player1) <= 50 and ball.xcor()>335:
        ball.paddle_bounce()

    if ball.distance(player2) <= 50 and ball.xcor() < -335:
        ball.paddle_bounce()

    if ball.xcor() > 370:
        score.l_point()
        ball.reset_position()
    if ball.xcor() < -370:
        score.r_point()
        ball.reset_position()
    screen.update()

screen.exitonclick()
