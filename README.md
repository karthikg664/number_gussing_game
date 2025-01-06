# Number Guessing Game

This is a simple number guessing game written in Python. The computer generates a random number between 1 and 100, and the player has a limited number of attempts to guess it. The game offers three difficulty levels: Easy, Medium, and Hard.

## Project Repository

Sample solution for the [number-guessing-game](https://github.com/karthikg664/number_gussing_game) challenge from [roadmap.sh](https://roadmap.sh).

## How to Play

1.  **Run the script:** Execute the Python script.
2.  **Select difficulty:** Choose a difficulty level from the menu:
    *   Easy (10 chances)
    *   Medium (5 chances)
    *   Hard (3 chances)
3.  **Make a guess:** Enter your guess as an integer.
4.  **Receive feedback:** The game will tell you if your guess is too high or too low.
5.  **Win or lose:** If you guess the number correctly within the allowed attempts, you win. Otherwise, you lose.
6.  **Play again:** You can choose to play another round or exit the game.

## Game Logic

*   The game generates a random number between 1 and 100.
*   The player selects a difficulty level, which determines the number of attempts allowed.
*   The player enters their guess.
*   The game provides feedback:
    *   If the guess is correct, the player wins.
    *   If the guess is too high, the game tells the player the number is lower.
    *   If the guess is too low, the game tells the player the number is higher.
*   If the player runs out of attempts, they lose, and the correct number is revealed.
*   The player can choose to play again or exit.
