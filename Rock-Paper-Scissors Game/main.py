import random

print("🎮 Welcome to Rock Paper Scissors! 🎮")

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

while True:
    user_choice = input("\nEnter rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice! Try again.")
        continue

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(f"Result: {result}")
    print(f"\nScore -> You: {user_score} | Computer: {computer_score}")

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != "y":
        print("\nThanks for playing!")
        break
