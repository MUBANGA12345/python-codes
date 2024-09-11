# favorite_books.py

# a) Create a list of favorite books
favorite_books = ["1984", "Alice in Wonderland", "Harry Potter", "Pride and Prejudice", "To Kill a Mockingbird"]
# Print the original list of favorite books
print("Original list of favorite books:")
print(favorite_books)

# c) Add two more books to the end of the list
favorite_books.append("The Catcher in the Rye")
favorite_books.append("The Great Gatsby")
# Print the list after adding two more books
print("\nList after adding two more books:")
print(favorite_books)

# d) Remove the second book from the list
del favorite_books[1]
# Print the list after removing the second book
print("\nList after removing the second book:")
print(favorite_books)

# e) Sort the list alphabetically
favorite_books.sort()
# Print the sorted list of favorite books
print("\nSorted list of favorite books:")
print(favorite_books)

# f) Print the sorted list
print(favorite_books)

# g) Create a tuple from the sorted list
favorite_books_tuple = tuple(favorite_books)
# Print the tuple of favorite books
print("\nTuple of favorite books:")
print(favorite_books_tuple)

# h) Try to add a new book to the tuple and handle the resulting error
try:
    # Attempt to add a new book to the tuple (this will raise an AttributeError)
    favorite_books_tuple.append("The Lord of the Rings")
except AttributeError as e:
    # Catch the AttributeError and print an error message
    print("\nError: Tuples are immutable, cannot add new book to the tuple.")
    print(e)