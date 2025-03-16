from typing import List
from src.decorators.catch import catch
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.organizer import note_book
from src.decorators.confirm import confirm
from src.helpers.logger import Logger


@catch
@confirm()
def remove_note(args: List[str]):
    if len(args) != 1:
        raise WrongArgumentsNumberException(1)
    title = args[0]
    resp = note_book.remove_note(title)
    if resp:
        Logger.success(f"Note with this title - {title} successfully deleted.")
    else:
        raise KeyError(f"Note with title - {title} does not exist.")
