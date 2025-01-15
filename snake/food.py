from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        x_rand=random.randint(-288,288)
        y_rand=random.randint(-288,265)
        self.goto(x_rand,y_rand)
        self.refresh()


    def refresh(self):
        x_rand=random.randint(-288,288)
        y_rand=random.randint(-288,260)
        self.goto(x_rand,y_rand)        
