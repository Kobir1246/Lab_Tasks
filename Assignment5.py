# Initial data
books = (
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("1984", "George Orwell", 1949),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925)
)

tags = {"classic", "dystopian", "novel", "literature"}

# a. Access the second book's author and print it
second_book_author = books[1][1]
print("Second book's author:", second_book_author)

# b. Add a new record for the book "Brave New World" by Aldous Huxley, published in 1932
# Since tuples are immutable, we need to create a new tuple by combining the existing one
new_book = ("Brave New World", "Aldous Huxley", 1932)
books = books + (new_book,)
print("\nUpdated books tuple:", books)

# c. Unpack the details of the third book into separate variables and print them
title, author, year = books[2]
print(f"\nDetails of the third book: Title: {title}, Author: {author}, Year: {year}")

# d. Loop through the books tuple and print each book's title
print("\nBook Titles:")
for book in books:
    print(book[0])

# e. Add a new tag "sci-fi" to the tags set and print the updated set
tags.add("sci-fi")
print("\nUpdated tags set:", tags)

# f. Remove the tag "novel" from the tags set and print the updated set
tags.discard("novel")  # Using discard to avoid error if the tag doesn't exist
print("\nUpdated tags set after removing 'novel':", tags)
