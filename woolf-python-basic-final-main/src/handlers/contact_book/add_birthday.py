from typing import List
from src.models.contact_book.birthday import Birthday
from src.decorators.catch import catch
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.organizer import contact_book
from src.exceptions.non_existed_record_exception import NonExistedException
from src.helpers.logger import Logger


@catch
def add_birthday(args: List[str]):

    if len(args) < 2:
        raise WrongArgumentsNumberException(2)

    name, birthday = args

    record = contact_book.find_record(name)

    if record == None:
        raise NonExistedException(name)

    record.birthday = Birthday(birthday)

    Logger.success(f"Birthday successfully changed for {birthday}")
