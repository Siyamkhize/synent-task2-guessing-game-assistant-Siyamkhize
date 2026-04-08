# Task 2: Number Guessing Game (CLI)

---
© 2026 Siyabonga Mkhize. All Rights Reserved.
---

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

### 🔐 Security Features
- **Secret Key Access**: The application is locked behind a secret key pattern (`Siyamkhize_2026_GUESS`). Only authorized users with the key can execute the game.
- **Obfuscated Backend**: Core arithmetic and game logic functions are stored in a hidden, obfuscated module ([_secret_backend.py](file:///c:/projects/synent-task2-guessing-game-assistant/_secret_backend.py)) to prevent unauthorized reverse-engineering.
- **Ownership Protection**: All source files contain strict ownership and license headers.
- **Dynamic Logic Loading**: Backend functions are decoded and loaded into memory at runtime from a secure source.

### ⚙️ CI/CD Pipeline
- **GitHub Actions**: Automated workflow for linting, security scanning (Bandit), and basic logic verification on every push and pull request to the `master` branch.

### 🕹️ How to Play
1. Navigate to the game folder in your terminal.
2. Launch the game:
   ```bash
   python guessing_game.py
   ```
3. Enter your guesses when prompted and follow the hints.
