# from turtle import Turtle, Screen
# from paddels import Paddel
# from ball import Ball
# import time
# from score import Score


# screen = Screen()


# screen.bgcolor("black")
# screen.setup(800, 600) 
# screen.title("Pong")
# screen.tracer(0)

# r_paddel=Paddel((350,0))
# l_paddel=Paddel((-350,0))
# ball=Ball()
# score=Score()

# screen.listen()
# screen.onkey(r_paddel.go_up, "Up")
# screen.onkey(r_paddel.go_down, "Down")
# screen.onkey(l_paddel.go_up, "w")
# screen.onkey(l_paddel.go_down, "s")
# game_on=True

# while game_on:
#     time.sleep(ball.move_speed)
#     screen.update()
#     ball.move()
# # detect collision with the wall\
#     if ball.ycor()>280 or ball.ycor()<-280:
#         # bsll needs to bounce
#         ball.bounce_y()
# #detect collision with paddel
#     if ball.distance(r_paddel) <55 and ball.xcor()>320 or ball.distance(l_paddel)<55 and ball.xcor()<-320:
#         ball.bounce_x()
#         time.sleep()
#         # detect if paddel misses the ball 
#     if ball.xcor()>380:
#         ball.reset()
#         ball.bounce_x()
#         score.l_point()

#     if ball.xcor() < -380:
#         ball.reset()
#         ball.bounce_x()
#         score.r_point()

# screen.exitonclick()
 #main.py
from turtle import Turtle, Screen
from paddels import Paddle
from ball import Ball
from score import Score
import time

class PongGame:
    def __init__(self):
        self.screen = Screen()
        self.setup_screen()
        self.create_objects()
        self.setup_controls()
        self.game_speed = 0.1
        self.max_score = 5  # New feature: game ends when a player reaches this score
    
    
    def setup_screen(self):
        self.screen.bgcolor("black")
        self.screen.setup(800, 600)
        self.screen.title("Pong")
        self.screen.tracer(0)
        
        # Draw center line
        self.draw_center_line()
        
    def draw_center_line(self):
        center_line = Turtle()
        center_line.color("white")
        center_line.hideturtle()
        center_line.penup()
        center_line.goto(0, 300)
        center_line.setheading(270)
        
        for _ in range(30):
            center_line.pendown()
            center_line.forward(10)
            center_line.penup()
            center_line.forward(10)
            
    def create_objects(self):
        self.r_paddle = Paddle((350, 0))
        self.l_paddle = Paddle((-350, 0))
        self.ball = Ball()
        self.score = Score()
        
    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(self.r_paddle.go_up, "Up")
        self.screen.onkey(self.r_paddle.go_down, "Down")
        self.screen.onkey(self.l_paddle.go_up, "w")
        self.screen.onkey(self.l_paddle.go_down, "s")
        # New feature: pause game
        self.screen.onkey(self.toggle_pause, "space")
        
    def toggle_pause(self):
        if hasattr(self, 'paused'):
            self.paused = not self.paused
        else:
            self.paused = True
            
    def check_winner(self):
        if self.score.l_score >= self.max_score:
            return "Left"
        elif self.score.r_score >= self.max_score:
            return "Right"
        return None
        
    def run_game(self):
        self.paused = False
        game_on = True
        
        while game_on:
            if not self.paused:
                time.sleep(self.ball.move_speed)
                self.screen.update()
                self.ball.move()
                
                # Detect collision with walls
                if self.ball.ycor() > 280 or self.ball.ycor() < -280:
                    self.ball.bounce_y()
                    
                # Detect collision with paddles
                if ((self.ball.distance(self.r_paddle) < 55 and self.ball.xcor() > 320) or 
                    (self.ball.distance(self.l_paddle) < 55 and self.ball.xcor() < -320)):
                    self.ball.bounce_x()
                    
                # Detect if paddle misses the ball
                if self.ball.xcor() > 380:
                    self.ball.reset()
                    self.score.l_point()
                    
                if self.ball.xcor() < -380:
                    self.ball.reset()
                    self.score.r_point()
                    
                # Check for winner
                winner = self.check_winner()
                if winner:
                    self.score.game_over(winner)
                    game_on = False
            
            self.screen.update()
            
        self.screen.exitonclick()

if __name__ == "__main__":
    game = PongGame()
    game.run_game()
