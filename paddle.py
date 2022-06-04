from turtle import Turtle


class Paddle:
    def __init__(self, sign):
        self.paddle = Turtle()
        self.paddle.shape('square')
        self.paddle.color('white')
        self.paddle.shapesize(stretch_len=1, stretch_wid=5)
        self.paddle.penup()
        self.new_y = 0
        self.sign = sign
        self.paddle.speed("fastest")
        self.paddle.goto(self.sign * 390, 100)

    def move_up(self):
        self.new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), self.new_y)

    def move_down(self):
        self.new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), self.new_y)
