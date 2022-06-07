from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
player1 = Paddle(384,0)
player2 = Paddle(-390,0)

screen.onkeypress(player1.move_up, "Up")
screen.onkeypress(player1.move_down, "Down")

screen.onkeypress(player2.move_up, "w")
screen.onkeypress(player2.move_down, "s ")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()
