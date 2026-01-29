# Program of a simple calculator consisting of basic calculations

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect Operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (+, -, *, /): ")

match choice:
    case '+':
        result = num1 + num2
        print("Result =", result)

    case '-':
        result = num1 - num2
        print("Result =", result)

    case '*':
        result = num1 * num2
        print("Result =", result)

    case '/':
        if num2 == 0:
            print("Division by zero is not allowed!")
        else:
            result = num1 / num2
            print("Result =", result)

    case _:
        print("Invalid operation")
