# remove_vowels.py

def remove_vowels(input_string):
    """
    Remove all vowels from the input string.

    Args:
        input_string (str): The input string from which to remove vowels.

    Returns:
        str: The input string with all vowels removed.
    """
    vowels = "aeiouAEIOU"
    output_string = ""
    for char in input_string:
        if char not in vowels:
            output_string += char
    return output_string

# Demonstrate the use of the function with example inputs
input_strings = ["Hello World", "Python is fun", "AEIOUaeiou"]
for input_string in input_strings:
    print(f"Input: {input_string}")
    print(f"Output: {remove_vowels(input_string)}")
    print()