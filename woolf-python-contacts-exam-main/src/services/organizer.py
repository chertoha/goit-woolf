from services.contact_book import ContactBook
from services.note_book import NoteBook


class Organizer:

    def __init__(self) -> None:
        self.note_book = NoteBook()
        self.contact_book = ContactBook()


organizer_instance = Organizer()
contact_book = organizer_instance.contact_book
note_book = organizer_instance.note_book
