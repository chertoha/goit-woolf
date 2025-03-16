from typing import List
from src.helpers.logger import Logger
from src.models.contact_book.record import Record
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.decorators.catch import catch
from src.models.organizer import contact_book


@catch
def add_contact(args: List[str]):

    if len(args) < 2:
        raise WrongArgumentsNumberException(2)

    name, phone = args

    record = contact_book.find_record(name)

    if record and record.find_phone(phone):
        raise ValueError(f"Contact {name} already has phone {phone}")

    if record == None:
        record = Record(name)
        record.add_phone(phone)
        contact_book.add_record(record)
    else:
        record.add_phone(phone)

    Logger.success("Phone addition success.")
