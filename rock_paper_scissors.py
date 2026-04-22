import random

def play_game():
    options = ["rock", "paper", "scissors"]
    user_score = 0
    cpu_score = 0

    print("--- 🪨  📄 ✂️  Rock, Paper, Scissors ---")
    print("First to 3 wins! Type 'quit' to exit.")

    while user_score < 3 and cpu_score < 3:
        user_choice = input("\nChoose Rock, Paper, or Scissors: ").lower()

        if user_choice == "quit":
            break
        
        if user_choice not in options:
            print("Invalid choice. Please try again.")
            continue

        cpu_choice = random.choice(options)
        print(f"Computer chose: {cpu_choice}")

        # Game Logic
        if user_choice == cpu_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and cpu_choice == "scissors") or \
             (user_choice == "paper" and cpu_choice == "rock") or \
             (user_choice == "scissors" and cpu_choice == "paper"):
            print("You win this round! 🎉")
            user_score += 1
        else:
            print("Computer wins this round! 🤖")
            cpu_score += 1

        print(f"Score -> You: {user_score} | CPU: {cpu_score}")

    # Final result
    if user_score == 3:
        print("\nCongratulations! You beat the computer!")
    elif cpu_score == 3:
        print("\nGame Over! The computer won the match.")

if __name__ == "__main__":
    play_game()