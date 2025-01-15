import turtle 
import time
from snakes import Snake
from food import Food
from score import Score

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("powder blue")
screen.title("Snakes")
screen.tracer(0)

# Create a Snake instance
snake = Snake()
food=Food()
scoreb=Score()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# Game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.15)
    snake.move()
#delect collition of snake with food
    if snake.head.distance(food)<17:
        food.refresh()
        snake.extend()
        scoreb.inc_score()
#detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor()> 280 or snake.head.ycor()< -280:
        game_on=False
        scoreb.game_over()
# detect collision with tail
for segment in snake.segments[1:]:
    if snake.head.distance(segment)<10:
        game_on=False
        scoreb.game_over()
# Exit on click
screen.exitonclick()