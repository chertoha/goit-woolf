from models.address_book import AddressBook
import pickle


class Database:

    def __init__(self, filename: str = "addressbook.pkl") -> None:
        self.__filename = filename

    def save_data(self, book: AddressBook) -> None:
        with open(self.__filename, "wb") as file:
            pickle.dump(book, file)

    def load_data(self):
        try:
            with open(self.__filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return AddressBook()
