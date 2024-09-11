# favorite_books.py

# Create a list of favorite books
books = ["To Kill a Mockingbird", "The Great Gatsby", "Pride and Prejudice"]

# Add two more books to the list
books.append("The Catcher in the Rye")
books.append("1984")

# Remove the second book from the list
del books[1]

# Sort the list in alphabetical order
books.sort()

# Create a tuple from the list
book_tuple = tuple(books)

print("Favorite books:", book_tuple)