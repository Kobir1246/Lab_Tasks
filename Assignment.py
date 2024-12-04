class LibraryBook:
    def __init__(self, isbn, title, author):
        self.__isbn = isbn
        self._title = title
        self.author = author

    def get_ISBN(self):
        return "****" + self.__isbn[-4:]

    def borrow_book(self, borrower_name):
        print(f"The book '{self._title}' has been borrowed by {borrower_name}")

    def _display_basic_info(self):
        print(f"Title: {self._title}, Author: {self.author}")

class DigitalLibraryBook(LibraryBook):
    def display_basic_info(self):
        super()._display_basic_info()
        print("Format: eBook")

# Test
book = LibraryBook("1234567890123", "Python Programming", "John Doe")
print("ISBN:", book.get_ISBN())
book.borrow_book("Alice")
digital_book = DigitalLibraryBook("9876543210123", "Data Science", "Jane Doe")
digital_book.display_basic_info()