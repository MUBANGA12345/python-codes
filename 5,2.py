# Create a list of lambda functions that perform basic arithmetic operations
arithmetic_operations = [
    lambda x, y: x + y,  # addition
    lambda x, y: x - y,  # subtraction
    lambda x, y: x * y,  # multiplication
    lambda x, y: x / y if y != 0 else "Error: Division by zero"  # division
]

# Define a function to perform calculations using the lambda functions
def perform_calculations(num1, num2):
    """
    Perform basic arithmetic operations on a pair of numbers using lambda functions.

    Args:
        num1 (int or float): The first number.
        num2 (int or float): The second number.
    """
    for i, operation in enumerate(arithmetic_operations):
        result = operation(num1, num2)
        operation_name = ["addition", "subtraction", "multiplication", "division"][i]
        print(f"{num1} {operation_name} {num2} = {result}")

# Example usage:
num1 = 10
num2 = 2
perform_calculations(num1, num2)