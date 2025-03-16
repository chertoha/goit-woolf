"""
NoteBook Class
==============

The `NoteBook` class is designed to manage a collection of notes. It allows storing, 
retrieving, updating, and removing individual notes in an organized manner. Each note 
is represented by an instance of the `Note` class, which contains a title, text content, 
and associated tags. The `NoteBook` class provides an interface to manipulate these notes, 
making it easier to search for specific notes, filter by tags, and update existing note details.


"""

from typing import List
from .note import Note


class NoteBook:

    def __init__(self) -> None:
        self.__notes: List[Note] = []

    def add_note(self, data: Note) -> None:
        self.__notes.append(data)

    def find_note(self, searched_title: str):
        return next((note for note in self.__notes if note.title == searched_title), None)

    def find_notes_by_partial_title(self, partial_title: str):
        return [note for note in self.__notes if note.title.lower().startswith(partial_title.lower())]

    def remove_note(self, searched_title: str):
        for index, note in enumerate(self.__notes):
            if note.title == searched_title:
                del self.__notes[index]
                return True
        return False

    def update_note(self, searched_title: str, new_text: str):
        for note in self.__notes:
            if note.title == searched_title:
                note.text = new_text

    def update_note_title(self, old_title: str, new_title: str):
        for note in self.__notes:
            if note.title == old_title:
                note.title = new_title

    def find_tags(self, search_tag):
        result = []
        for note in self.__notes:
            for tag in note.tags:
                if tag.lower().startswith(search_tag.lower()):
                    result.append(note)
        return result

    def get_dump_state(self):
        state = []

        for note in self.__notes:
            title = note.title
            text = note.text
            tags = note.get_tags()

            state.append({"title": title, "text": text, "tags": tags})

        return state

    def set_dump_state(self, state):
        for item in state:
            note = Note(item["title"], item["text"])
            note.add_tags(item["tags"])
            self.add_note(note)

    def show_notes(self, notes: List[Note]):
        for note in notes:
            print(note)
