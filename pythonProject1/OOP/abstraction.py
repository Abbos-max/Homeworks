
from abc import ABC, abstractmethod
import datetime




class AbstractUser(ABC):
    @abstractmethod
    def borrow_book(self, book):
        pass

    @abstractmethod
    def return_book(self, book):
        pass

class AbstractBook(ABC):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def get_author(self):
        pass

    @abstractmethod
    def get_isbn(self):
        pass

    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    def set_status(self, status):
        pass


class Book(AbstractBook):
    def init(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.due_time = None

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_isbn(self):
        return self.isbn

    def get_status(self):
        return "available" if self.is_available else f"borrowed until {self.due_time}"

    def set_status(self, status):
        if status == "available":
            self.is_available = True
            self.due_time = None
        elif status.startswith("borrowed"):
            self.is_available = False
            self.due_time = datetime.datetime.now().date() + datetime.timedelta(days=14)
        else:
            raise ValueError("Invalid status")


class Patron(AbstractUser):
    def init(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            book.due_time = datetime.datetime.now().date() + datetime.timedelta(days=14)
            self.borrowed_books.append(book)
            print(f'{self.name} borrowed "{book.title}" until {book.due_time}.')
        else:
            print(f'"{book.title}" is not available. It will be available on {book.due_time + datetime.timedelta(days=1)}.')

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            book.due_time = None
            print(f'{self.name} returned "{book.title}".')
        else:
            print(f'"{book.title}" was not borrowed by {self.name}.')


class Library:
    def init(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f'"{book.title}" has been added to the library.')

    def add_patron(self, patron):
        self.patrons.append(patron)
        print(f'{patron.name} has joined the library.')

    def borrow_book(self, book, patron, days=14) -> None:
        if book.is_available:
            book.is_available = False
            book.due_time = datetime.datetime.now().date() + datetime.timedelta(days=days)
            patron.borrowed_books.append(book)
            print(f'{patron.name} borrowed "{book.title}" until {book.due_time}.')
        else:
            print(f'"{book.title}" is not available. It will be available on {book.due_time + datetime.timedelta(days=1)}.')

    def return_book(self, book: Book, patron: Patron):
        if book in patron.borrowed_books:
            patron.borrowed_books.remove(book)
            book.is_available = True
            book.due_time = None
            print(f'"{book.title}" has been returned to the library.')
        else:
            print(f'"{book.title}" was not borrowed by {patron.name}.')

    def search_books(self, query):
        return [book for book in self.books if
                query.lower() in book.title.lower() or
                query.lower() in book.author.lower() or
                query in book.isbn]


def display_borrowed_books(self, patron: Patron = None):
        if patron:
            return patron.borrowed_books
        else:
            borrowed_books = {}
            for patron in self.patrons:
                borrowed_books[patron.member_id] = patron.borrowed_books
            return borrowed_books


library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789")
book2 = Book("1984", "George Orwell", "987654321")
patron1 = Patron("Alice", "P001")

library.add_book(book1)
library.add_book(book2)
library.add_patron(patron1)

library.borrow_book(book1, patron1)
borrowed_books = library.display_borrowed_books()
print(borrowed_books)