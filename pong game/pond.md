# 🏓 Pong Game with AI

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A modern implementation of the classic Pong game built with Python's Turtle graphics library. Play against an AI opponent that uses predictive algorithms to track and hit the ball!

## ✨ Features

- 🤖 Smart AI opponent that predicts ball trajectory
- 🎮 Smooth paddle controls
- 🎯 Dynamic ball speed that increases during rallies
- 📊 Real-time score tracking
- ⏸️ Pause functionality
- 🏁 Game over screen with winner announcement
- 🎲 Random ball direction after each point
- 📏 Visual center court line
- 🔄 Automatic boundary checking for paddles

## 🎮 Controls

| Action | Key |
|--------|-----|
| Move Right Paddle Up | ⬆️ Up Arrow |
| Move Right Paddle Down | ⬇️ Down Arrow |
| Pause Game | Spacebar |
| Exit Game | Click window |

## 🛠️ Requirements

- Python 3.x
- Built-in `turtle` module (no additional installations needed)

## 📥 Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/pong-game.git
cd pong-game
```

2. Run the game:
```bash
python main.py
```

## 📁 Project Structure

```
pong-game/
│
├── main.py          # Game initialization and main loop
├── ball.py          # Ball movement and physics
├── paddels.py       # Paddle controls and AI logic
└── score.py         # Score tracking and display
```

## 🎯 How to Play

1. Launch the game using `python main.py`
2. Control the right paddle using the Up and Down arrow keys
3. The left paddle is controlled by AI
4. First player to reach 5 points wins
5. The ball speeds up each time it hits a paddle
6. Press spacebar to pause/unpause the game

## 🤖 AI Behavior

The AI-controlled paddle:
- Calculates predicted ball trajectory
- Adjusts position based on ball direction and speed
- Accounts for wall bounces in predictions
- Maintains realistic movement speed
- Gets more challenging as the game progresses

## 🚀 Game Mechanics

- Ball speed increases with each paddle hit
- Random starting direction after each point
- Automatic collision detection
- Score tracking for both players
- Paddle movement boundary enforcement
- Center line for visual reference

## 🔧 Customization

You can modify game parameters in `main.py`:
- `self.max_score`: Change the winning score (default: 5)
- `self.bot_speed`: Adjust AI paddle speed
- `self.game_speed`: Modify general game speed
- `self.ball.move_speed`: Change ball speed

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by the classic Atari Pong game
- Built using Python's Turtle graphics library
- AI logic inspired by basic game theory principles

## 📧 Contact

Your Name - [@your_twitter](https://twitter.com/your_twitter)

Project Link: [https://github.com/YOUR_USERNAME/pong-game](https://github.com/YOUR_USERNAME/pong-game)