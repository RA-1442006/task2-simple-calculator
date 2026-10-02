"""
Simple Command-Line Calculator
Task 2 — Python Internship Project

This module provides an interactive command-line calculator supporting basic
arithmetic operations: addition, subtraction, multiplication, division, and modulus.
It includes robust input validation, graceful zero-division error handling,
an interactive menu loop, and cleanly formatted results.
"""


def add(a: float, b: float) -> float:
    """
    Return the sum of two numbers.

    Parameters:
        a (float): The first addend.
        b (float): The second addend.

    Returns:
        float: Sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Return the difference of two numbers (a - b).

    Parameters:
        a (float): The minuend.
        b (float): The subtrahend.

    Returns:
        float: Difference of a and b.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Return the product of two numbers.

    Parameters:
        a (float): The first factor.
        b (float): The second factor.

    Returns:
        float: Product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Return the quotient of two numbers (a / b).

    Parameters:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: Quotient of a and b.

    Raises:
        ZeroDivisionError: If the divisor (b) is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def modulus(a: float, b: float) -> float:
    """
    Return the remainder of two numbers (a % b).

    Parameters:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: Modulus/remainder of a divided by b.

    Raises:
        ZeroDivisionError: If the divisor (b) is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot calculate modulus with a divisor of zero.")
    return a % b


def get_number(prompt: str) -> float:
    """
    Prompt the user for a numeric input and re-prompt until a valid number is entered.

    Parameters:
        prompt (str): The message prompt displayed to the user.

    Returns:
        float: The validated numeric value entered by the user.
    """
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid numeric value.")


def display_menu() -> None:
    """Display the interactive calculator menu options."""
    print("\n==============================")
    print("      SIMPLE CALCULATOR       ")
    print("==============================")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exit")
    print("==============================")


def main() -> None:
    """
    Main driver function to run the command-line calculator.
    Handles the menu loop, user choices, input delegation, and result output.
    """
    print("Welcome to the Simple Command-Line Calculator!")

    # Mapping of menu options to (function, operator_symbol, operation_name)
    operations = {
        "1": (add, "+", "Addition"),
        "2": (subtract, "-", "Subtraction"),
        "3": (multiply, "*", "Multiplication"),
        "4": (divide, "/", "Division"),
        "5": (modulus, "%", "Modulus"),
    }

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        # Exit option
        if choice == "6":
            print("\nThank you for using the Simple Calculator. Goodbye!")
            break

        # Validate menu selection
        if choice not in operations:
            print("Invalid choice! Please select an option from 1 to 6.")
            continue

        func, symbol, name = operations[choice]
        print(f"\n--- {name} ---")

        # Prompt and validate both numbers
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        # Perform calculation and handle zero division gracefully
        try:
            result = func(num1, num2)
            print(f"\nResult: {num1} {symbol} {num2} = {result}")
        except ZeroDivisionError as error:
            print(f"\nError: {error}")


if __name__ == "__main__":
    main()
