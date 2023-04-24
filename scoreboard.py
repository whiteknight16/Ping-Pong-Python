from turtle import Turtle
ALIGN="center"
FONT=("Courier",85,"bold")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color('yellow')
        self.score_l=0
        self.score_r=0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.goto(-100,190)
        self.write(self.score_l,align=ALIGN,font=FONT)
        self.goto(100,190)
        self.write(self.score_r,align=ALIGN,font=FONT)

    def left_pt(self):
        self.score_l+=1
        self.clear()
        self.update_scoreboard()
    
    
    def right_pt(self):
        self.score_r+=1
        self.clear()
        self.update_scoreboard()
