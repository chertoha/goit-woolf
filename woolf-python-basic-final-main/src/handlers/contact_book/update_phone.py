from typing import List
from src.models.contact_book.record import Record
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.decorators.catch import catch
from src.models.organizer import contact_book
from src.helpers.logger import Logger


@catch
def update_phone(args: List[str]):
    if len(args) < 3:
        raise WrongArgumentsNumberException(3)

    name, old_phone, new_phone, *_ = args

    record = contact_book.find_record(name)

    if record is None:
        raise KeyError(f"Contact with name '{name}' not found.")

    if not record.find_phone(old_phone):
        raise ValueError(f"Phone number '{
                         old_phone}' not found in contact '{name}'.")

    if record.find_phone(new_phone):
        raise ValueError(f"Phone number '{
                         new_phone}' already exists in contact '{name}'.")

    record.update_phone(old_phone, new_phone)

    Logger.success(f"Phone number '{old_phone}' updated to '{
        new_phone}' for contact '{name}'.")
