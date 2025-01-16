import time
from turtle import Screen
from snakes import Snake
from food import Food
from score import Score
from collections import deque

# Constants
MOVE_DELAY = 0.1
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class SmartSnakeGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        
        self.snake = Snake()
        self.food = Food()
        self.score = Score()
        
    def find_path_to_food(self):
        """Use BFS to find a safe path to the food"""
        start = (int(self.snake.head.xcor()), int(self.snake.head.ycor()))
        end = (int(self.food.xcor()), int(self.food.ycor()))
        
        # Create a grid for pathfinding
        grid_size = 20  # Size of each grid cell
        visited = set()
        queue = deque([(start, [])])
        
        while queue:
            pos, path = queue.popleft()
            if self.manhattan_distance(pos, end) < 20:  # Close enough to food
                return path
                
            # Try all possible moves
            for dx, dy, direction in [(20, 0, "right"), (-20, 0, "left"), 
                                    (0, 20, "up"), (0, -20, "down")]:
                new_x = pos[0] + dx
                new_y = pos[1] + dy
                new_pos = (new_x, new_y)
                
                # Check if move is safe
                if (self.is_valid_move(new_x, new_y) and 
                    new_pos not in visited and 
                    not self.will_collide_with_body(new_x, new_y)):
                    visited.add(new_pos)
                    new_path = path + [direction]
                    queue.append((new_pos, new_path))
        
        # If no path found, try to move in the safest direction
        return self.get_safe_direction()
    
    def manhattan_distance(self, pos1, pos2):
        """Calculate Manhattan distance between two points"""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    def is_valid_move(self, x, y):
        """Check if the move is within bounds"""
        return abs(x) < 290 and abs(y) < 290
    
    def will_collide_with_body(self, x, y):
        """Check if moving to (x,y) will result in collision with snake body"""
        for segment in self.snake.segments[1:]:
            if abs(segment.xcor() - x) < 10 and abs(segment.ycor() - y) < 10:
                return True
        return False
    
    def get_safe_direction(self):
        """Find a safe direction when no clear path to food exists"""
        head_x, head_y = self.snake.head.xcor(), self.snake.head.ycor()
        directions = []
        
        # Check each direction for safety
        for dx, dy, direction in [(20, 0, "right"), (-20, 0, "left"), 
                                (0, 20, "up"), (0, -20, "down")]:
            new_x = head_x + dx
            new_y = head_y + dy
            if (self.is_valid_move(new_x, new_y) and 
                not self.will_collide_with_body(new_x, new_y)):
                directions.append(direction)
        
        return directions[:1] if directions else ["right"]  # Default to right if no safe moves
    
    def auto_move(self):
        """Execute the next move based on pathfinding"""
        path = self.find_path_to_food()
        if path:
            next_move = path[0]
            if next_move == "right":
                self.snake.right()
            elif next_move == "left":
                self.snake.left()
            elif next_move == "up":
                self.snake.up()
            elif next_move == "down":
                self.snake.down()
    
    def run_game(self):
        """Main game loop"""
        while True:
            self.screen.update()
            self.auto_move()
            self.snake.move()
            
            # Check for food collision
            if self.snake.head.distance(self.food) < 15:
                self.food.refresh()
                self.snake.extend()
                self.score.inc_score()
            
            # Check for wall collision
            if abs(self.snake.head.xcor()) > 290 or abs(self.snake.head.ycor()) > 290:
                self.score.game_over()
                break
            
            # Check for self collision
            for segment in self.snake.segments[1:]:
                if self.snake.head.distance(segment) < 10:
                    self.score.game_over()
                    return
            
            time.sleep(MOVE_DELAY)
        
        self.screen.bye()

# Create and run the game
if __name__ == "__main__":
    game = SmartSnakeGame()
    game.run_game()