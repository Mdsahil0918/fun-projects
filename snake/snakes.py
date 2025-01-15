import turtle
import time
# Constants
starting_pos = [(0, 0), (-20, 0), (-40, 0)]
move = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in starting_pos:
            self.add_segment(pos)

    def move(self):
        # Move the segments in reverse order
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(move)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def extend(self):
        self.add_segment(self.segments[-1].position())


    def add_segment(self,pos):
            new_segment = turtle.Turtle("square")
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)