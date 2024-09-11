# address_book.py

# Define a dictionary representing a simple address book
address_book = {}

def add_entry(name, phone_number):
    """
    Add a new entry to the address book.

    Args:
        name (str): The name of the person.
        phone_number (str): The phone number of the person.
    """
    address_book[name] = phone_number

def delete_entry(name):
    """
    Delete an entry from the address book.

    Args:
        name (str): The name of the person to delete.
    """
    if name in address_book:
        del address_book[name]

def modify_entry(name, new_phone_number):
    """
    Modify an existing entry in the address book.

    Args:
        name (str): The name of the person to modify.
        new_phone_number (str): The new phone number.
    """
    if name in address_book:
        address_book[name] = new_phone_number

def write_address_book_to_file():
    """
    Write the address book to a file named 'address_book.txt'.
    """
    try:
        with open('address_book.txt', 'w') as f:
            for name, phone_number in address_book.items():
                f.write(f"{name}:{phone_number}\n")
    except IOError as e:
        print(f"Error writing to file: {e}")

def read_address_book_from_file():
    """
    Read the address book from the file and print its contents.
    """
    try:
        with open('address_book.txt', 'r') as f:
            for line in f:
                name, phone_number = line.strip().split(":")
                print(f"Name: {name}, Phone Number: {phone_number}")
    except IOError as e:
        print(f"Error reading from file: {e}")

# Test the address book functions
add_entry("John", "1234567890")
add_entry("Jane", "0987654321")
modify_entry("John", "1111111111")
delete_entry("Jane")
write_address_book_to_file()
read_address_book_from_file()

# Define a function to count the occurrence of each word in a text file
def count_words_in_file(file_name):
    """
    Read a text file, count the occurrence of each word, and return a dictionary with words as keys and their counts as values.

    Args:
        file_name (str): The name of the text file.

    Returns:
        dict: A dictionary with words as keys and their counts as values.
    """
    try:
        with open(file_name, 'r') as f:
            text = f.read()
            words = text.split()
            word_counts = {}
            for word in words:
                word = word.lower()
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
            return word_counts
    except IOError as e:
        print(f"Error reading from file: {e}")
        return {}

# Test the word counting function
word_counts = count_words_in_file('sample_text.txt')
print("Word Counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")

# Implement a basic unit test for the word counting function
import unittest

class TestWordCountingFunction(unittest.TestCase):
    def test_normal_operation(self):
        word_counts = count_words_in_file('sample_text.txt')
        self.assertIsInstance(word_counts, dict)
        self.assertGreater(len(word_counts), 0)

    def test_empty_file(self):
        word_counts = count_words_in_file('empty_file.txt')
        self.assertIsInstance(word_counts, dict)
        self.assertEqual(len(word_counts), 0)

    def test_non_existent_file(self):
        word_counts = count_words_in_file('non_existent_file.txt')
        self.assertIsInstance(word_counts, dict)
        self.assertEqual(len(word_counts), 0)

if __name__ == '__main__':
    unittest.main()

# Use list comprehension to create a list of squares of even numbers from 1 to 20
squares_of_even_numbers = [i ** 2 for i in range(2, 21, 2)]
print("Squares of Even Numbers:", squares_of_even_numbers)

# Use dictionary comprehension to create a dictionary where the keys are numbers from 1 to 10, and the values are their cubes
cubes = {i: i ** 3 for i in range(1, 11)}
print("Cubes:", cubes)