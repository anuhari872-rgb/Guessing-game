import random

def show_welcome():
    """Show game title."""
    print("===================================")
    print("        NUMBER GUESSING GAME       ")
    print("===================================\n")


def choose_difficulty():
    """Let the user choose a difficulty level."""
    print("Choose difficulty:")
    print("1. Easy   (1–50)   Unlimited attempts")
    print("2. Medium (1–100)  10 attempts")
    print("3. Hard   (1–200)  7 attempts\n")

    while True:
        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            return 50, None   # range up to 50, unlimited attempts
        elif choice == "2":
            return 100, 10    # range up to 100, 10 tries
        elif choice == "3":
            return 200, 7     # range up to 200, 7 tries
        else:
            print("Invalid choice! Please choose 1, 2, or 3.\n")


def give_hint(secret, guess):
    """Give hints to help the player."""
    if abs(secret - guess) <= 5:
        return "🔥 You're very close!"
    elif abs(secret - guess) <= 15:
        return "🙂 You're close!"
    else:
        return "❄ You're far away."


def play_one_round():
    """Play one round of the game."""
    max_range, max_attempts = choose_difficulty()

    # Game setup
    secret_number = random.randint(1, max_range)
    attempts = 0

    print(f"\nI'm thinking of a number between 1 and {max_range}.")
    print("Try to guess it!\n")

    # Game loop
    while True:
        if max_attempts:
            print(f"Attempts left: {max_attempts - attempts}")

        guess = input("Enter your guess: ")

        # Validate input
        if not guess.isdigit():
            print("Please enter a valid number!\n")
            continue

        guess = int(guess)
        attempts += 1

        # Check the guess
        if guess < secret_number:
            print("Too low!", give_hint(secret_number, guess), "\n")

        elif guess > secret_number:
            print("Too high!", give_hint(secret_number, guess), "\n")

        else:
            print("\n🎉 Correct! You guessed the number!")
            print("The number was:", secret_number)
            print("Total attempts:", attempts)
            return attempts  # return the score

        # If attempts are limited and used up
        if max_attempts and attempts >= max_attempts:
            print("\n💀 You've run out of attempts!")
            print("The correct number was:", secret_number)
            return None  # no score


def main_game():
