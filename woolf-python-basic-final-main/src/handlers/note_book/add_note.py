from typing import List
from src.decorators.catch import catch
from src.models.organizer import note_book
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.note_book.note import Note
from src.helpers.logger import Logger

@catch
def add_note(args: List[str]):
    if len(args) < 2:
        raise WrongArgumentsNumberException(2)
    
    title, *rest = args
    text = " ".join(rest)

    note = note_book.find_note(title)
    if note:
        raise KeyError(f"Note with title - {title} already exist")

    note_book.add_note(Note(title, text))
    Logger.success(f"Note with title '{title}' successfully added.")
