from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn):
        self._title = title
        self.author = author
        self.__isbn = isbn
        self.is_borrowed = False
        self.borrower = None
        self.due_date = None

    def get_ISBN(self):
        return "****" + self.__isbn[-4:]

    def display_info(self):
        status = "Available" if not self.is_borrowed else f"Borrowed by {self.borrower} (Due: {self.due_date})"
        print(f"Title: {self._title}, Author: {self.author}, ISBN: {self.get_ISBN()}, Status: {status}")

    def borrow(self, user_name, duration=14):
        if self.is_borrowed:
            raise BookNotAvailableError(f"The book '{self._title}' is currently borrowed.")
        else:
            self.is_borrowed = True
            self.borrower = user_name
            self.due_date = datetime.now() + timedelta(days=duration)
            print(f"'{self._title}' has been borrowed by {user_name}.")

    def return_book(self):
        if not self.is_borrowed:
            raise BookAlreadyReturnedError(f"The book '{self._title}' is not currently borrowed.")
        else:
            self.is_borrowed = False
            self.borrower = None
            self.due_date = None
            print(f"The book '{self._title}' has been returned.")


class Library:
    def __init__(self):
        self.books = []
        self.users = {}

    def add_book(self, book, admin):
        if admin.is_admin:
            self.books.append(book)
            print(f"Admin '{admin.name}' added the book '{book._title}' to the library.")
        else:
            print("Only admins can add books.")

    def remove_book(self, title, admin):
        if admin.is_admin:
            book = self.find_book_by_title(title)
            if book:
                self.books.remove(book)
                print(f"Admin '{admin.name}' removed the book '{title}' from the library.")
            else:
                print(f"No book found with the title '{title}' to remove.")
        else:
            print("Only admins can remove books.")

    def register_user(self, user, admin):
        if admin.is_admin:
            if user.name in self.users:
                print(f"User '{user.name}' is already a registered member.")
            else:
                self.users[user.name] = user
                user.is_member = True
                print(f"Admin '{admin.name}' registered '{user.name}' as a member.")
        else:
            print("Only admins can register new members.")

    def remove_user(self, user_name, admin):
        if admin.is_admin:
            if user_name in self.users:
                del self.users[user_name]
                print(f"Admin '{admin.name}' removed '{user_name}' from the library members.")
            else:
                print(f"User '{user_name}' is not a member.")
        else:
            print("Only admins can remove members.")

    def display_available_books(self):
        print("\nAvailable Books:")
        available_books = [book for book in self.books if not book.is_borrowed]
        if not available_books:
            print("No books are currently available.")
        else:
            for idx, book in enumerate(available_books, start=1):
                print(f"{idx}. {book._title} by {book.author}")
        return available_books

    def find_book_by_title(self, title):
        for book in self.books:
            if book._title.lower() == title.lower():
                return book
        return None

    def is_member(self, user_name):
        return user_name in self.users and self.users[user_name].is_member


class User:
    MAX_BORROW_LIMIT = 3

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.borrowed_books = []
        self.is_member = False

    def borrow_book(self, library, duration=14):
        if not self.is_member:
            raise NotAMemberError(f"{self.name} is not a registered member. Please register to borrow books.")
        if len(self.borrowed_books) >= User.MAX_BORROW_LIMIT:
            raise ExceedBorrowLimitError("Borrow limit reached. Return a book to borrow a new one.")

        available_books = library.display_available_books()
        if not available_books:
            print("No books available to borrow.")
            return

        choice = int(input("Enter the number of the book you want to borrow: ")) - 1
        if 0 <= choice < len(available_books):
            book = available_books[choice]
            book.borrow(self.name, duration)
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book._title}'.")
        else:
            print("Invalid choice.")

    def return_book(self, library):
        if not self.borrowed_books:
            print("You have no books to return.")
            return

        print("\nYour Borrowed Books:")
        for idx, book in enumerate(self.borrowed_books, start=1):
            print(f"{idx}. {book._title} (Due: {book.due_date})")

        choice = int(input("Enter the number of the book you want to return: ")) - 1
        if 0 <= choice < len(self.borrowed_books):
            book = self.borrowed_books[choice]
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book._title}'.")
        else:
            print("Invalid choice.")

    def view_profile(self):
        print(f"\nProfile of {self.name}")
        print(f"Membership Status: {'Active' if self.is_member else 'Inactive'}")
        print("Borrowed Books:")
        if not self.borrowed_books:
            print("No books borrowed.")
        else:
            for book in self.borrowed_books:
                print(f"- {book._title} (Due: {book.due_date})")


class Admin(User):
    def __init__(self, name, password):
        super().__init__(name, password)
        self.is_admin = True


# Custom Exceptions
class BookNotAvailableError(Exception):
    def __init__(self, message="This book is currently unavailable for borrowing."):
        super().__init__(message)

class BookAlreadyReturnedError(Exception):
    def __init__(self, message="This book is already returned to the library."):
        super().__init__(message)

class ExceedBorrowLimitError(Exception):
    def __init__(self, message="You have exceeded the borrow limit."):
        super().__init__(message)

class NotAMemberError(Exception):
    def __init__(self, message="User is not a registered member. Please register first."):
        super().__init__(message)


def main():
    library = Library()
    admin = Admin("Admin", "admin123")  # Default admin user

    library.add_book(Book("Python Programming", "John Doe", "1234567890123"), admin)
    library.add_book(Book("Data Science Basics", "Jane Smith", "9876543210987"), admin)
    library.add_book(Book("Machine Learning Guide", "Alice Brown", "5678901234567"), admin)
    library.add_book(Book("Deep Learning Insights", "Tom Wilson", "8901234567890"), admin)
    library.add_book(Book("Artificial Intelligence", "Emma Davis", "2345678901234"), admin)
    library.add_book(Book("Big Data Concepts", "Chris Taylor", "3456789012345"), admin)

    print("\nInitial set of books added to the library.")
    library.display_available_books()


    while True:
        print("\n--- Library Management System ---")
        print("1. Admin: Add Book")
        print("2. Admin: Remove Book")
        print("3. Admin: Register User")
        print("4. Admin: Remove User")
        print("5. User: Borrow Book")
        print("6. User: Return Book")
        print("7. User: View Profile")
        print("8. Display Available Books")
        print("9. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":  # Add Book
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                library.add_book(Book(title, author, isbn), admin)

            elif choice == "2":  # Remove Book
                title = input("Enter book title to remove: ")
                library.remove_book(title, admin)

            elif choice == "3":  # Register User
                name = input("Enter new user name: ")
                password = input("Enter password for the user: ")
                library.register_user(User(name, password), admin)

            elif choice == "4":  # Remove User
                name = input("Enter user name to remove: ")
                library.remove_user(name, admin)

            elif choice == "5":  # Borrow Book
                name = input("Enter your name: ")
                password = input("Enter your password: ")
                if name in library.users and library.users[name].password == password:
                    user = library.users[name]
                    user.borrow_book(library)
                else:
                    print("Invalid credentials. Please try again.")

            elif choice == "6":  # Return Book
                name = input("Enter your name: ")
                password = input("Enter your password: ")
                if name in library.users and library.users[name].password == password:
                    user = library.users[name]
                    user.return_book(library)
                else:
                    print("Invalid credentials. Please try again.")

            elif choice == "7":  # View Profile
                name = input("Enter your name: ")
                password = input("Enter your password: ")
                if name in library.users and library.users[name].password == password:
                    user = library.users[name]
                    user.view_profile()
                else:
                    print("Invalid credentials. Please try again.")

            elif choice == "8":  # Display Available Books
                library.display_available_books()

            elif choice == "9":  # Exit
                print("Exiting the Library Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()