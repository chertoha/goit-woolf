from typing import List
from src.helpers.logger import Logger
from src.models.contact_book.email import Email
from src.exceptions.non_existed_record_exception import NonExistedException
from src.models.organizer import contact_book
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.decorators.catch import catch


@catch
def add_email(args: List[str]):
    if len(args) < 2:
        raise WrongArgumentsNumberException(2)

    name, email = args

    record = contact_book.find_record(name)

    if record == None:
        raise NonExistedException(name)

    record.email = Email(email)

    Logger.success("Email addition was successful.")
