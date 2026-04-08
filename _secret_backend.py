"""
LICENSE & OWNERSHIP NOTICE
==========================
© 2026 Siyabonga Mkhize. All Rights Reserved.
This file is part of the synent-task2-guessing-game-assistant-Siyamkhize project.
This module is confidential and proprietary. Unauthorized copying, modification, 
distribution, or use is strictly prohibited.
"""

import random
import base64

# Obfuscated core logic for the guessing game
def _get_secret_number(low=1, high=100):
    """Generates the secret number using the random module."""
    return random.randint(low, high)

def _evaluate_guess(guess, secret):
    """
    Evaluates the guess against the secret number.
    Returns:
    -1 if guess < secret (Too low)
     1 if guess > secret (Too high)
     0 if guess == secret (Correct)
    """
    if guess < secret:
        return -1
    elif guess > secret:
        return 1
    return 0

# Base64 encoded 'Welcome message' to simulate dynamic logic loading
_ENCODED_WELCOME = "V2VsY29tZSwgU2l5YWJvbmdhIE1raGl6ZSE="

def _get_welcome_message():
    """Decodes and returns the welcome message."""
    return base64.b64decode(_ENCODED_WELCOME).decode('utf-8')
