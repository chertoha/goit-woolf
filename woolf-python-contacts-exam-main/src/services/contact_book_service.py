from typing import List
from decorators.catch import catch
from entities.record import Record
from exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from services.organizer import contact_book
from pprint import pprint


class ContacBookService:

    @staticmethod
    @catch
    def add(args: List[str]):

        if (len(args) < 2):
            raise WrongArgumentsNumberException(
                f"Wrong number of arguments in command!, should be at least 2")

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

        print("Phone addition success.")

    @staticmethod
    @catch
    def find(args: List[str]):
        search = ""
        if len(args) != 0:
            search = args[0]
        pprint(contact_book.retrieve_contacts(search))

    @staticmethod
    @catch
    def update(args: List[str]):
        print("update")

    @staticmethod
    @catch
    def birthday(args: List[str]):
        print("birthday")
