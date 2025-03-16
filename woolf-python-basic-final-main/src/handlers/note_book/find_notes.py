from typing import List
from src.helpers.logger import Logger
from src.decorators.catch import catch
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.organizer import note_book


@catch
def find_notes(args: List[str]):

    query = args[0] if len(args) >= 1 else ""
    notes = note_book.find_notes_by_partial_title(query)
    if len(notes) != 0:
        note_book.show_notes(notes)
    elif query == "":
        Logger.warning(f"No notes yet! You can create few ;)")
    else:
        Logger.warning(f"Nothing found for query '{query}'")
