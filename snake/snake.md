# Snake Game with Auto-Play

This project is a Python implementation of the classic **Snake** game using the `turtle` graphics module. The game features automatic gameplay, where the snake moves towards the food, eats it, and grows longer until it hits a wall or itself.
![Screenshot (41)](https://github.com/user-attachments/assets/5cb3fdde-b41d-4457-844c-78c86f7f5a2c)

## Features:
- **Auto-Play**: The snake moves automatically towards the food, avoiding walls and itself.
- **Score Tracking**: The score increases as the snake eats the food.
- **Game Over**: The game ends if the snake collides with the walls or its own body.
- **Food Respawn**: After the snake eats the food, it respawns at a random position.

## Requirements:
- Python 3.x
- `turtle` module (usually comes pre-installed with Python)

## Setup:
1. Clone the repository or download the files.
2. Make sure you have Python 3.x installed on your system.
3. The `turtle` module is typically included with Python, so no extra installation is required.

## File Structure:

### Description of Files:
- **`snake.py`**: Defines the `Snake` class, responsible for creating and moving the snake, as well as handling its growth when it eats food.
- **`food.py`**: Defines the `Food` class, responsible for generating and moving food to a new random position after the snake eats it.
- **`score.py`**: Defines the `Score` class, which tracks and displays the player's score, and shows the "Game Over" message.
- **`auto_play.py`**: The main game file that controls the game loop, and handles the automatic movement of the snake towards the food.

## How to Run:
1. **Clone or download the files**.
2. Open a terminal or command prompt and navigate to the directory where the files are stored.
3. Run the `auto_play.py` file to start the game:
   ```bash
   python auto_play.py
The game will automatically play, where the snake moves towards the food, eats it, and continues growing. The game ends when the snake collides with a wall or itself.

Game Controls:
The snake moves automatically towards the food.
No manual controls are needed since the game is automated.
Example Gameplay:
The snake will automatically steer itself towards the food, and each time it eats the food, it will grow in size. The game continues until the snake collides with the walls or itself, at which point the game over message is displayed, and the score is shown.

License:
This project is open source. Feel free to fork and modify it as you wish.

vbnet
Copy

You can copy and paste this into a file named `README.md` in your project directory.

Let me know if you need further modifications!


