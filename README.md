# Task 2: Number Guessing Game (CLI)

## Developer: Siyabonga Mkhize
## Repository: synent-task2-guessing-game-assistant-Siyamkhize

### 🎮 Project Description
This is an interactive command-line guessing game developed in Python. The application generates a secret random number between 1 and 100, and the player is tasked with guessing it in as few attempts as possible.

### 🧠 Logic & Flow
The game logic follows a structured loop that guides the player towards the correct answer:
- **Random Generation**: Utilizes Python's `random` module to pick a secret number between 1 and 100 inclusive.
- **Attempt Tracking**: Increments a counter for each valid guess made by the player.
- **Feedback System**:
  - **Too Low**: Informs the user if their guess is less than the secret number.
  - **Too High**: Informs the user if their guess is greater than the secret number.
  - **Correct Guess**: Congratulates the user and displays the total number of attempts.
- **Input Sanitization**: Handles non-numeric inputs and provides an option to quit ('q') at any point.
- **Replayability**: After a successful guess, the player can choose to start a new game or exit.

### ✨ Features
- [x] Random secret number generation (1-100)
- [x] Dynamic feedback (Hints: Too High / Too Low)
- [x] Attempt tracking and counting
- [x] Input validation for numerical entries
- [x] Quitting and Replaying functionality

### 🕹️ How to Play
1. Navigate to the game folder in your terminal.
2. Launch the game:
   ```bash
   python guessing_game.py
   ```
3. Enter your guesses when prompted and follow the hints.
