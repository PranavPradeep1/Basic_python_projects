# program for deposit, withdraw, check balance

balance = 0

def deposit():
    global balance
    amount = float(input("Enter the amount to be deposited: "))
    balance += amount
    print("Amount deposited successfully!")

def withdraw():
    global balance
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Not enough balance")
    else:
        balance -= amount
        print("Amount withdrawn successfully!")

def check_balance():
    print("Current balance:", balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        deposit()
    elif choice == 2:
        withdraw()
    elif choice == 3:
        check_balance()
    elif choice == 4:
        print("Good bye!")
        break
    else:
        print("Invalid choice. Try again.")
