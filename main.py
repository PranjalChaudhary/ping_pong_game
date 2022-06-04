from turtle import Screen
from paddle import Paddle

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
player1 = Paddle(.98)
player2 = Paddle(-1)

screen.onkeypress(player1.move_up, "Up")
screen.onkeypress(player1.move_down, "Down")

screen.onkeypress(player2.move_up, "w")
screen.onkeypress(player2.move_down, "s ")


screen.exitonclick()
