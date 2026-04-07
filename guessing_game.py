import random
import sys

def main():
    print("--- Number Guessing Game ---")
    print("Project: synent-task2-guessing-game-assistant-Siyamkhize")
    print(f"Welcome, Siyabonga Mkhize!")
    print("\nI have selected a number between 1 and 100.")
    print("Can you guess what it is?")

    secret_number = random.randint(1, 100)
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

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number {secret_number} in {attempts} attempts.")
                
                play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
                if play_again == 'y':
                    secret_number = random.randint(1, 100)
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
