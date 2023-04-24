from turtle import Turtle

class Ball(Turtle):
    def __init__ (self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.color('red')
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1


    def move(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)

    def bounce_y(self):
        self.y_move*=-1

    def bounce_x(self):
        self.x_move*=-1
        self.move_speed*=.9

    def reset(self):
        self.goto(0,0)
        self.move_speed=.1
        self.bounce_x()

    def increase_speed(self):
        self.speed+=.1
