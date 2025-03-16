"""
Organizer Class
===============

The `Organizer` class serves as the central point for managing both the `NoteBook` and 
`ContactBook` in the organizer application. It aggregates these two components, providing 
methods for serialization and deserialization of their state, allowing for easy saving 
and restoring of the full state of the organizer.

The class contains two main attributes:
- `note_book`: An instance of the `NoteBook` class, responsible for handling notes.
- `contact_book`: An instance of the `ContactBook` class, responsible for managing contacts.

It implements two important methods for managing object persistence:
- `__getstate__`: This method is used to retrieve the current state of the `Organizer`, 
  including the states of both the `NoteBook` and `ContactBook`. It serializes the current 
  state of these components into a dictionary.
  
- `__setstate__`: This method is used to restore the state of the `Organizer` from a given 
  dictionary. It reinitializes the `NoteBook` and `ContactBook` instances and sets their 
  state based on the data provided.

This class facilitates the storage and retrieval of data related to both notes and contacts, 
allowing the entire `Organizer` to be easily serialized and deserialized. It is designed 
for use with a persistence mechanism (e.g., saving and loading from a file).
"""


from src.models.contact_book.contact_book import ContactBook
from src.models.note_book.note_book import NoteBook


class Organizer:

    def __init__(self) -> None:
        self.note_book = NoteBook()
        self.contact_book = ContactBook()

    def __getstate__(self) -> object:
        contact_book_state = self.contact_book.get_dump_state()
        note_book_state = self.note_book.get_dump_state()
        return {"contact_book": contact_book_state, "note_book": note_book_state}

    def __setstate__(self, state):
        self.note_book = NoteBook()
        self.contact_book = ContactBook()

        contact_book_state = state["contact_book"]
        note_book_state = state["note_book"]

        self.contact_book.set_dump_state(contact_book_state)
        self.note_book.set_dump_state(note_book_state)
