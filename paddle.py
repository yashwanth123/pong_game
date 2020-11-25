from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()

        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

        self.goto(pos)

    def forward(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)

    def backward(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)
