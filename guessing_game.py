"""
LICENSE & OWNERSHIP NOTICE
==========================
© 2026 Siyabonga Mkhize. All Rights Reserved.
This file is part of the synent-task2-guessing-game-assistant-Siyamkhize project.
This module is confidential and proprietary. Unauthorized copying, modification, 
distribution, or use is strictly prohibited.
"""

import sys
import os

# Secure Secret Key Access (Can be moved to an environment variable in production)
SECRET_KEY = "Siyamkhize_2026_GUESS"

def authenticate():
    """Prompts the user for a secret key to unlock the application."""
    print("--- Security Protocol ---")
    try:
        key_input = input("Enter Secret Access Key: ").strip()
        if key_input == SECRET_KEY:
            print("Access Granted. Unlocking backend logic...\n")
            return True
        else:
            print("Access Denied. Incorrect key. System terminating.")
            return False
    except KeyboardInterrupt:
        print("\nExiting...")
        return False

def main():
    if not authenticate():
        sys.exit(1)

    # Dynamic Logic Loading: Import backend only after successful authentication
    try:
        import _secret_backend as backend
    except ImportError:
        print("Error: Obfuscated backend module not found.")
        sys.exit(1)

    print("--- Number Guessing Game ---")
    print("Project: synent-task2-guessing-game-assistant-Siyamkhize")
    print(backend._get_welcome_message())
    
    print("\nI have selected a number between 1 and 100.")
    print("Can you guess what it is?")

    secret_number = backend._get_secret_number(1, 100)
    attempts = 0

    while True:
        try:
            guess_input = input("\nEnter your guess (or 'q' to quit): ").strip().lower()
            
            if guess_input == 'q':
                print(f"Quitting. The number was {secret_number}. Goodbye!")
                break

            guess = int(guess_input)
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue

            result = backend._evaluate_guess(guess, secret_number)

            if result == -1:
                print("Too low! Try again.")
            elif result == 1:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number {secret_number} in {attempts} attempts.")
                
                play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
                if play_again == 'y':
                    secret_number = backend._get_secret_number(1, 100)
                    attempts = 0
                    print("\n--- New Game Started ---")
                    print("I have selected a new number between 1 and 100.")
                else:
                    print("Thanks for playing! Goodbye.")
                    break
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
