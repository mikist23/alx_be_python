class Book:
    def __init__(self, title, author) :
        self.title = title
        self.author = author
        # self._is_checked_out = _is_checked_out
        self._is_checked_out  = False

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library():
    def __init__(self):
        self._books = []
    

    def add_book(self,book):
        self._books.append(book)
        

    # def check_out_book(self, title):
    #     """Check out a book by title, if available."""
    #     for book in self._books:
    #         if book.title == title:
    #             if not book._is_checked_out:
    #                 book._is_checked_out = True
    #                 print(f"'{book.title}' has been checked out.")
    #             else:
    #                 print(f"'{book.title}' is already checked out.")
    #             return
    #     print(f"Book titled '{title}' is not available.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
    

    # def return_book(self):
    #     for book in self._books:
    #             if book._is_checked_out:
    #                 book._is_checked_out = False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    book._is_checked_out = False
                    print(f"'{book.title}' has been returned.")
                else:
                    print(f"'{book.title}' was not checked out.")
                return  # Exit the loop after finding the book
        print(f"Book titled '{title}' was not found.")

    def list_available_books(self):
        availbale_books = [book for book in self._books if not book._is_checked_out]
        if availbale_books:
            for book in availbale_books:
                print(book)
        else:
            print("Book title not found")

