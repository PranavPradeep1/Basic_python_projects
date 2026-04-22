import random

def roll_dice():
    print("--- 🎲 Dice Rolling Game 🎲 ---")
    
    while True:
        user_input = input("\nPress 'Enter' to roll the dice (or type 'q' to quit): ").lower()
        
        if user_input == 'q':
            print("Thanks for playing! Goodbye.")
            break
        
        # Generate a random number between 1 and 6
        result = random.randint(1, 6)
        
        print(f"You rolled a: {result}")
        
        # Optional: Add a little visual flair
        if result == 6:
            print("Critical Hit! 🌟")
        elif result == 1:
            print("Ouch, a snake eye. 🐍")

if __name__ == "__main__":
    roll_dice()