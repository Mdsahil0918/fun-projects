from turtle import Turtle
aligment="center"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(0,270)
        self.update()
        self.hideturtle()
    def inc_score(self):
        self.score+=1
        self.clear()
        self.update()
    def update(self):
        self.write(f"Score : {self.score}",align=aligment,font=("Arial",24,"normal"))
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align=aligment,font=("Arial",24,"normal"))