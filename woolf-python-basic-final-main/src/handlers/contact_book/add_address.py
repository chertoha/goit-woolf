from typing import List
from src.exceptions.non_existed_record_exception import NonExistedException
from src.models.contact_book.address import Address
from src.decorators.catch import catch
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.organizer import contact_book
from src.helpers.logger import Logger


@catch
def add_address(args: List[str]):
    if len(args) < 2:
        raise WrongArgumentsNumberException(2)

    name, *rest = args
    address = " ".join(rest)

    record = contact_book.find_record(name)

    if record == None:
        raise NonExistedException(name)

    record.address = Address(address)

    Logger.success(f"Address successfully changed for {address}")
