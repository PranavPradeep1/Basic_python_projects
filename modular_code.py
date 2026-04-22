import random

# --- Logic Layer ---
def get_computer_choice():
    """Handles the AI logic."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, cpu):
    """Pure logic: determines the result based on inputs."""
    if user == cpu:
        return "tie"
    
    win_conditions = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if win_conditions[user] == cpu:
        return "user"
    return "cpu"

# --- UI / Interaction Layer ---
def get_user_input(valid_options):
    """Handles input and validation."""
    while True:
        choice = input(f"\nEnter {', '.join(valid_options).title()} (or 'q' to quit): ").lower()
        if choice == 'q' or choice in valid_options:
            return choice
        print("Invalid choice. Please try again.")

def display_score(user_pts, cpu_pts):
    """Handles visual output."""
    print(f"       SCORE: You {user_pts} | CPU {cpu_pts}")
    print("-" * 30)

# --- Main Controller ---
def main():
    options = ["rock", "paper", "scissors"]
    user_score = 0
    cpu_score = 0

    print("--- 🎲 Modular Rock Paper Scissors 🎲 ---")

    while user_score < 3 and cpu_score < 3:
        user_move = get_user_input(options)
        
        if user_move == 'q':
            print("Exiting game...")
            break

        cpu_move = get_computer_choice()
        print(f"Computer chose: {cpu_move}")

        result = determine_winner(user_move, cpu_move)

        if result == "tie":
            print("It's a draw!")
        elif result == "user":
            print("Point for you!")
            user_score += 1
        else:
            print("Point for the computer!")
            cpu_score += 1

        display_score(user_score, cpu_score)

    if user_score == 3:
        print("MATCH OVER: You won!")

if __name__ == "__main__":
    main()