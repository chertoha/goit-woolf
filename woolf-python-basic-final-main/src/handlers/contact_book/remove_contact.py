from typing import List
from src.models.contact_book.record import Record
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.decorators.catch import catch
from src.models.organizer import contact_book
from src.decorators.confirm import confirm
from src.helpers.logger import Logger


@catch
@confirm()
def remove_contact(args: List[str]):

    if len(args) < 1:
        raise WrongArgumentsNumberException(1)

    name = args[0]

    record = contact_book.find_record(name)

    if record is None:
        raise ValueError(f"Contact with name '{name}' not found.")

    contact_book.remove_record(name)

    Logger.success(f"Contact '{name}' has been removed successfully.")
