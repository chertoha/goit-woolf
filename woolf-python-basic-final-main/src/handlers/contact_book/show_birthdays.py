from typing import List
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.decorators.catch import catch
from src.models.organizer import contact_book
from src.helpers.logger import Logger


@catch
def show_birthdays(args: List[str]):
    if len(args) < 1:
        raise WrongArgumentsNumberException(1)

    try:
        days = int(args[0])
    except ValueError:
        raise ValueError("The number of days must be an integer.")

    upcoming_birthdays = contact_book.get_upcoming_birthdays(days)

    if upcoming_birthdays:
        print("Upcoming birthdays:")

        contact_book.show_birthdays(upcoming_birthdays)

    else:
        Logger.warning("No birthdays in the specified range.")
