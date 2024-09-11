# calculate_numbers.py

def calculate(x, y):
    # Calculate the sum, difference, product, and quotient
    sum = x + y
    difference = x - y
    product = x * y
    quotient = x / y
    
    # Return the results as a tuple
    return sum, difference, product, quotient

# Test the function
result = calculate(5, 3)
print("The result is:", result)
