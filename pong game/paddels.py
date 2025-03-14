from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)
        self.move_distance = 20
        
    def go_up(self):
        if self.ycor() < 240:  # Add boundary checking
            new_y = self.ycor() + self.move_distance
            self.goto(self.xcor(), new_y)
        
    def go_down(self):
        if self.ycor() > -240:  # Add boundary checking
            new_y = self.ycor() - self.move_distance
            self.goto(self.xcor(), new_y)

