def add(x, y):
    """Perform addition of two numbers."""
    return x + y


def subtract(x, y):
    """Perform subtraction of two numbers."""
    return x - y


def multiply(x, y):
    """Perform multiplication of two numbers."""
    return x * y


def divide(x, y):
    """Perform division of two numbers."""
    if y == 0:
        return "Error: Division by zero"
    return x / y


def calculator():
    """Main calculator function with user interface."""
    print("Welcome to the Python Calculator!")

    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        # Get user choice
        choice = input("Enter choice (1/2/3/4/5): ")

        # Exit condition
        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        # Input validation
        if choice not in ['1', '2', '3', '4']:
            print("Invalid input. Please try again.")
            continue

        # Get numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Perform calculation based on user's choice
        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")


# Run the calculator
if __name__ == "__main__":
    calculator()
