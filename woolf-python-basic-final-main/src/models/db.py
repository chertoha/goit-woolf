"""
Database Class
==============

The `Database` class is responsible for saving and loading data related to the `Organizer` class 
using the `pickle` module. It provides functionality to persist an `Organizer` object to a file 
and retrieve it back, allowing for data to be stored between program executions.

This class uses binary file format (with `.pkl` extension by default) for serialization, 
making it possible to save complex objects and restore them efficiently. The filename for the 
data storage is customizable, and if no filename is provided, it defaults to `"data/organizer.pkl"`.

The class ensures that an `Organizer` object can be saved to disk with the `save_data` method, 
and retrieved with the `load_data` method. If the file containing the data doesn't exist, 
it returns a new instance of the `Organizer` class.

This class simplifies data persistence for the organizer application, offering a straightforward 
mechanism for managing saved states without the need for manual data entry after every session.
"""

import pickle

from src.models.organizer_class import Organizer


class Database:

    def __init__(self, filename: str = "data/organizer.pkl") -> None:
        self.__filename = filename

    def save_data(self, organizer: Organizer) -> None:
        with open(self.__filename, "wb") as file:
            pickle.dump(organizer, file)

    def load_data(self):
        try:
            with open(self.__filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return Organizer()
