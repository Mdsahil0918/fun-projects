from turtle import Turtle,Screen
import random

screen=Screen()
screen.title("Turtle Race")
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="make your bet",prompt="which tutrl will win th race , choose your color :") 
colors=["red","green","blue","orange","yellow","purple"]
alls=[]
screen.title("Turtle Race")
# Draw the start line
start_line = Turtle()
start_line.penup()
start_line.goto(-200, 100)
start_line.setheading(270)
start_line.pendown()
start_line.forward(200)
start_line.penup()
start_line.hideturtle()

# Draw the finish line
finish_line = Turtle()
finish_line.penup()
finish_line.goto(230, 100)
finish_line.setheading(270)
finish_line.pendown()
finish_line.forward(200)
finish_line.penup()
finish_line.hideturtle()

y_pos=[-70,-40,-5,25,60,89]
for i in range(6):
    tim=Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230,y=y_pos[i])
    alls.append(tim)

race=False
if user_bet:
    race=True
while race:
    for tim in alls:
        tim.forward(random.randint(5,10))
    if tim.xcor()>230:
        race=False
        winner=tim.pencolor()
        if winner==user_bet:
            print(f"you won the Bet :{user_bet}")
        else:
            print(f"you loosee the color is : {winner}")


screen.exitonclick()