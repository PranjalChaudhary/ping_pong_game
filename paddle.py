from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.paddle = Turtle()
        self.xcor = x_cor
        self.ycor = y_cor
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.new_y = 0
        self.speed("fastest")
        self.goto(self.xcor, self.ycor)

    def move_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

    def move_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)
