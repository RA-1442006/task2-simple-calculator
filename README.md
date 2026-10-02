# Simple Command-Line Calculator

Task 2 — Python Internship Project

---

## 📌 Project Overview

The **Simple Command-Line Calculator** is a robust, modular, and interactive terminal-based application written in Python. It enables users to perform fundamental mathematical operations through a structured menu interface. Built adhering to software engineering best practices, it emphasizes clean separation of concerns, defensive programming with input validation, graceful zero-division error handling, and clean code documentation.

---

## ✨ Features

- **Modular Arithmetic Functions**: Dedicated functions for each supported operation (`add`, `subtract`, `multiply`, `divide`, `modulus`).
- **Interactive Menu Loop**: A clear numeric menu (1 to 5 for operations, 6 to exit) that runs continuously until the user decides to quit.
- **Robust Input Validation**: Validates user inputs with `try...except ValueError` inside an input loop, gracefully rejecting non-numeric values without crashing.
- **Zero-Division Protection**: Protects against zero division for both regular division (`/`) and modulus (`%`), printing descriptive error messages instead of raising uncaught exceptions.
- **Clear Formatted Results**: Displays calculations cleanly, e.g., `Result: 10.0 / 2.0 = 5.0`.
- **Pure Python Standard Library**: Relies entirely on built-in Python features with zero external third-party dependencies.
- **Clean Code Architecture**: Formatted with PEP 8 standards, comprehensive docstrings, type hints, and standard `main()` / `if __name__ == "__main__":` entry point.

---

## 🛠️ How to Run the Program

### Prerequisites
- Python 3.6 or newer installed on your machine.
- A terminal, command prompt, or code editor (VS Code, PowerShell, Terminal, etc.).

### Steps
1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd simple-calculator
   ```
3. Run the script:
   ```bash
   python calculator.py
   ```
4. Follow the on-screen menu prompts to select operations, input numbers, and view results. Enter `6` when you wish to exit.

---

## 🔢 Supported Operations

| Option | Operation | Operator | Function Signature | Description |
| :---: | :--- | :---: | :--- | :--- |
| `1` | **Addition** | `+` | `add(a, b)` | Calculates the sum of two numbers. |
| `2` | **Subtraction** | `-` | `subtract(a, b)` | Subtracts the second number from the first. |
| `3` | **Multiplication** | `*` | `multiply(a, b)` | Multiplies two numbers. |
| `4` | **Division** | `/` | `divide(a, b)` | Computes the float quotient (checks `b != 0`). |
| `5` | **Modulus** | `%` | `modulus(a, b)` | Computes the remainder of division (checks `b != 0`). |
| `6` | **Exit** | — | — | Terminates the calculator session. |

---

## 📋 Sample Output

Below is a demonstration covering all five arithmetic operations, error cases (zero-division and invalid inputs), and session termination:

```text
Welcome to the Simple Command-Line Calculator!

==============================
      SIMPLE CALCULATOR       
==============================
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulus (%)
6. Exit
==============================
Enter your choice (1-6): 1

--- Addition ---
Enter the first number: 10
Enter the second number: 5

Result: 10.0 + 5.0 = 15.0

==============================
      SIMPLE CALCULATOR       
==============================
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulus (%)
6. Exit
==============================
Enter your choice (1-6): 2

--- Subtraction ---
Enter the first number: 20
Enter the second number: 8

Result: 20.0 - 8.0 = 12.0

==============================
      SIMPLE CALCULATOR       
==============================
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulus (%)
6. Exit
==============================
Enter your choice (1-6): 3

--- Multiplication ---
Enter the first number: 7
Enter the second number: 6

Result: 7.0 * 6.0 = 42.0

==============================
      SIMPLE CALCULATOR       
==============================
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulus (%)
6. Exit
==============================
Enter your choice (1-6): 4

--- Division ---
Enter the first number: 10
Enter the second number: 2

Result: 10.0 / 2.0 = 5.0

==============================
      SIMPLE CALCULATOR       
==============================
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulus (%)
6. Exit
==============================
Enter your choice (1-6): 4

--- Division ---
Enter the first number: 10
Enter the second number: 0

Error: Cannot divide by zero.

==============================
      SIMPLE CALCULATOR       
==============================
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulus (%)
6. Exit
==============================
Enter your choice (1-6): 5

--- Modulus ---
Enter the first number: 17
Enter the second number: 5

Result: 17.0 % 5.0 = 2.0

==============================
      SIMPLE CALCULATOR       
==============================
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulus (%)
6. Exit
==============================
Enter your choice (1-6): 5

--- Modulus ---
Enter the first number: 17
Enter the second number: 0

Error: Cannot calculate modulus with a divisor of zero.

==============================
      SIMPLE CALCULATOR       
==============================
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulus (%)
6. Exit
==============================
Enter your choice (1-6): 9
Invalid choice! Please select an option from 1 to 6.

==============================
      SIMPLE CALCULATOR       
==============================
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulus (%)
6. Exit
==============================
Enter your choice (1-6): 1

--- Addition ---
Enter the first number: abc
Invalid input! Please enter a valid numeric value.
Enter the first number: 15
Enter the second number: xyz
Invalid input! Please enter a valid numeric value.
Enter the second number: 3

Result: 15.0 + 3.0 = 18.0

==============================
      SIMPLE CALCULATOR       
==============================
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulus (%)
6. Exit
==============================
Enter your choice (1-6): 6

Thank you for using the Simple Calculator. Goodbye!
```

---

## 💡 Conceptual Questions & Answers

### 1. What is the difference between `/` and `//` in Python?
- **`/` (True / Float Division)**: Performs standard mathematical division and **always returns a floating-point number (`float`)**, regardless of whether the operands are integers or floats.
  - Example: `7 / 2` evaluates to `3.5`.
  - Example: `6 / 2` evaluates to `3.0`.
- **`//` (Floor / Integer Division)**: Divides two numbers and rounds down to the nearest whole integer towards negative infinity (mathematical floor $\lfloor x \rfloor$). The return type is an `int` if both operands are integers, or a whole `float` if at least one operand is a float.
  - Example: `7 // 2` evaluates to `3`.
  - Example: `7.0 // 2` evaluates to `3.0`.
  - Example: `-7 // 2` evaluates to `-4` (rounds down towards negative infinity, unlike truncation towards zero).

---

### 2. What does the modulus operator do?
- The **modulus operator (`%`)** returns the **remainder** left over after dividing the left operand by the right operand.
- In Python, the formula for modulus is defined as:
  $$r = a - (b \times (a // b))$$
- **Examples**:
  - `17 % 5 = 2` (because $5 \times 3 = 15$, and $17 - 15 = 2$).
  - `10 % 2 = 0` (indicating that 10 is evenly divisible by 2).
- **Common Real-World Use Cases**:
  - Determining parity (checking if a number is even or odd: `num % 2 == 0`).
  - Cyclical indexing and circular buffers (e.g., wrapping hours on a 12-hour or 24-hour clock: `(current_hour + elapsed) % 24`).
  - Unit conversions (e.g., remaining seconds after converting to full minutes: `seconds % 60`).

---

### 3. How can you prevent division-by-zero errors?
Attempting to divide or calculate remainder by zero in Python raises an unhandled `ZeroDivisionError` that crashes the program if uncaught. There are two primary paradigms to prevent this:

1. **Pre-Check Validation (LBYL — Look Before You Leap)**:
   Explicitly inspect the divisor prior to executing the division or modulus calculation.
   ```python
   if divisor == 0:
       print("Error: Divisor cannot be zero.")
   else:
       result = dividend / divisor
   ```
2. **Exception Handling (EAFP — Easier to Ask for Forgiveness than Permission)**:
   Attempt the operation inside a `try...except` block, catching the `ZeroDivisionError` and presenting an informative error message to the user without interrupting program flow.
   ```python
   try:
       result = dividend / divisor
   except ZeroDivisionError:
       print("Error: Cannot divide by zero.")
   ```
In this project, both paradigms work synergistically: the mathematical functions explicitly check and raise `ZeroDivisionError("Cannot divide by zero.")`, while the caller catches the exception and displays an informative error message gracefully.

---

## 🔗 Project & Submission Links

- **GitHub Repository**: [https://github.com/RA-1442006/task2-simple-calculator](https://github.com/RA-1442006/task2-simple-calculator)
- **LinkedIn Post**: [https://lnkd.in/p/ghh9gggu](https://lnkd.in/p/ghh9gggu)

