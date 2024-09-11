# factorial.py

def factorial(n):
    # Base case: 0! = 1
    if n == 0:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)

# Test the function
print("The factorial of 5 is:", factorial(5))