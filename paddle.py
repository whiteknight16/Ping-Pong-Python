from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape('square')
        self.pu()
        self.color('white')
        self.goto(pos)
        self.resizemode('user')
        self.shapesize(5, 1)
        self.color('blue')

    def up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)
