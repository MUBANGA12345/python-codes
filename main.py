# Part 1: Basic Calculations and String Operations

# Demonstrate basic calculations and string operations using the Python interactive shell
print("Part 1: Basic Calculations and String Operations")
print("Using the Python interactive shell:")
print(">>> 2 + 2")
print("4")
print(">>> 'hello' + ' world'")
print("'hello world'")
print(">>> 'hello'.upper()")
print("'HELLO'")

# Part 2: Functions and Modules

# 2.2. Write a Python function that takes two numbers as arguments and returns their sum, difference, product, and quotient as a tuple
def calculate(num1, num2):
    return (num1 + num2, num1 - num2, num1 * num2, num1 / num2 if num2 != 0 else "Error: Division by zero")

print("\nPart 2: Functions and Modules")
print("2.2. Calculate function:")
print(calculate(10, 2))

# 2.3. Create a Python module named 'math_operations' that contains functions for basic arithmetic operations
import math_operations

print("\n2.3. Math Operations Module:")
print(math_operations.add(10, 2))
print(math_operations.subtract(10, 2))
print(math_operations.multiply(10, 2))
print(math_operations.divide(10, 2))

# 2.4. Write a Python script that prompts the user to enter their age and categorizes them into "Child", "Teenager", "Adult", or "Senior"
age = int(input("\nEnter your age: "))
if age <= 12:
    print("You are a Child.")
elif age <= 19:
    print("You are a Teenager.")
elif age <= 59:
    print("You are an Adult.")
else:
    print("You are a Senior.")

# 2.5. Implement a recursive function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("\n2.5. Factorial function:")
print(factorial(5))

# Part 3: Sequences and Control Flow

# 3.1. Write a Python script that creates a list of favorite books, adds two more books, removes the second book, sorts the list, and creates a tuple
favorite_books = ["Book1", "Book2", "Book3", "Book4", "Book5"]
print("\nPart 3: Sequences and Control Flow")
print("3.1. Favorite Books:")
print(favorite_books)
favorite_books.extend(["Book6", "Book7"])
print("After adding two more books:")
print(favorite_books)
del favorite_books[1]
print("After removing the second book:")
print(favorite_books)
favorite_books.sort()
print("After sorting the list:")
print(favorite_books)
favorite_books_tuple = tuple(favorite_books)
print("Tuple of favorite books:")
print(favorite_books_tuple)
try:
    favorite_books_tuple.append("Book8")
except AttributeError:
    print("Error: Cannot add to a tuple.")

# 3.2. Create a program that generates a multiplication table for numbers 1 to 10
print("\n3.2. Multiplication Table:")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")

# 3.3. Write a function that takes a string as input and returns a new string with all vowels removed
def remove_vowels(s):
    return "".join([c for c in s if c.lower() not in "aeiou"])

print("\n3.3. Remove Vowels function:")
print(remove_vowels("Hello World"))

# Part 4: Dictionaries, File Handling, and Comprehensions

# 4.1. Create a Python script that defines a dictionary representing a simple address book, implements functions to add, delete, and modify entries, and writes the address book to a file
address_book = {"John": "123-4567", "Jane": "987-6543"}
def add_entry(name, phone_number):
    address_book[name] = phone_number
def delete_entry(name):
    del address_book[name]
def modify_entry(name, phone_number):
    address_book[name] = phone_number

print("\nPart 4: Dictionaries, File Handling, and Comprehensions")
print("4.1. Address Book:")
print(address_book)
add_entry("Bob", "555-1234")
print("After adding an entry:")
print(address_book)
delete_entry("Jane")
print("After deleting an entry:")
print(address_book)
modify_entry("John", "111-2222")
print("After modifying an entry:")
print(address_book)

try:
    with open("address_book.txt", "w") as f:
        for name, phone_number in address_book.items():
            f.write(f"{name}: {phone_number}\n")
    print("Address book written to file.")
except IOError as e:
    print(f"Error writing to file: {e}")

try:
    with open("address_book.txt", "r") as f:
        print("Address book read from file:")
        for line in f:
            print(line.strip())
except IOError as e:
    print(f"Error reading from file: {e}")

# 4.2. Write a function that reads a text file, counts the occurrence of each word, and returns a dictionary with words as keys and their counts as values
def count_words(filename):
    word_counts = {}
    with open(filename, "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
    return word_counts

print("\n4.2. Word Count function:")
print(count_words("example.txt"))

# 4.3. Implement a basic unit test for the word counting function using Python's unittest module
import unittest

class TestWordCount(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(count_words("example.txt"), {"word1": 2, "word2": 1, "word3": 1})

if __name__ == "__main__":
    unittest.main()

# 4.4. Use list comprehension to create a list of squares of even numbers from 1 to 20, and dictionary comprehension to create a dictionary where the keys are numbers from 1 to 10, and the values are their cubes
even_squares = [i**2 for i in range(2, 21, 2)]
print("\n4.4. Even Squares:")
print(even_squares)

cube_dict = {i: i**3 for i in range(1, 11)}
print("Cube Dictionary:")
print(cube_dict)

# Part 5: Advanced Concepts

# 5.1. Write a function that can accept any number of positional and keyword arguments
def print_args(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print("\nPart 5: Advanced Concepts")
print("5.1. Print Args function:")
print_args(1, 2, 3, a=4, b=5)

# 5.2. Create a list of lambda functions that perform basic arithmetic operations
arithmetic_operations = [
    lambda x, y: x + y,  # addition
    lambda x, y: x - y,  # subtraction
    lambda x, y: x * y,  # multiplication
    lambda x, y: x / y if y != 0 else "Error: Division by zero"  # division
]

print("\n5.2. Arithmetic Operations:")
for i, operation in enumerate(arithmetic_operations):
    result = operation(10, 2)
    operation_name = ["addition", "subtraction", "multiplication", "division"][i]
    print(f"10 {operation_name} 2 = {result}")

# 5.3. Implement a decorator function that measures and prints the execution time of any function it decorates
import time
import functools

def timer_decorator(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer_decorator
def sort_large_list():
    large_list = [i for i in range(10000)]
    sorted_list = sorted(large_list)
    return sorted_list

print("\n5.3. Timer Decorator:")
sort_large_list()