from typing import List
from entities.note import Note


class NoteBook:

    def __init__(self) -> None:
        self.__notes: List[Note] = []

    def add_note(self, title: str, text: str) -> None:
        self.__notes.append(Note(title, text))

    def find_note(self, searched_title: str):
        return next((note for note in self.__notes if note.title == searched_title), None)

    def remove_note(self, searched_title: str):
        self.__notes = list(filter(lambda note: note.title !=
                                   searched_title, self.__notes))

    def update_note(self, searched_title: str, new_text: str):
        note = self.find_note(searched_title)

        if note == None:
            raise ValueError(f"Cannot find note with title '{searched_title}'")

        note.text = new_text

    def update_note_title(self, old_title: str, new_title: str):
        note = self.find_note(old_title)

        if note == None:
            raise ValueError(f"Cannot find note with title '{old_title}'")

        note.title = new_title
