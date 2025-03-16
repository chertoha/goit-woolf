from abc import ABC, abstractmethod
from typing import List
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.__books: List[Book] = []

    def add_book(self, book: Book):
        self.__books.append(book)

    def remove_book(self, title: str):
        self.__books = [book for book in self.__books if book.title != title]

    def show_books(self):
        for book in self.__books:
            logging.info(book)


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: str):
        book = Book(title, author, year)
        self.library.add_book(book)
        logging.info(f'Book "{title}" added.')

    def remove_book(self, title: str):
        self.library.remove_book(title)
        logging.info(f'Book "{title}" removed.')

    def show_books(self):
        self.library.show_books()


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter book year: ").strip()
            manager.add_book(title, author, year)
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            manager.remove_book(title)
        elif command == "show":
            manager.show_books()
        elif command == "exit":
            break
        else:
            logging.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
