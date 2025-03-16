from datetime import datetime
from models.address_book import AddressBook
from models.record import Record
from .decorators import input_error


@input_error
def add_contact(args, address_book: AddressBook):
    name, phone = args

    contact = address_book.find(name)

    if contact and contact.find_phone(phone):
        raise ValueError(f"Contact {name} already has phone {phone}")

    if contact == None:
        record = Record(name)
        record.add_phone(phone)
        address_book.add_record(record)
    else:
        contact.add_phone(phone)

    return "Contact added."


@input_error
def change_contact(args, address_book: AddressBook):
    name, old_phone, new_phone = args

    contact = address_book.find(name)

    if contact == None:
        raise KeyError(f"There is no contact with name {name}")

    if not contact.find_phone(old_phone):
        raise ValueError(f"Contact {name} has no phone {old_phone}")

    contact.edit_phone(old_phone, new_phone)

    return "Contact updated."


@input_error
def show_phone(args,  address_book: AddressBook):
    name, = args
    contact = address_book.find(name)

    if contact == None:
        raise KeyError(f"There is no contact with name {name}")

    return contact


def show_all(address_book: AddressBook):
    return address_book.show()


@input_error
def delete_contact(args, address_book: AddressBook):
    name = args

    contact = address_book.find(name)

    if contact == None:
        raise KeyError(f"There is no contact with name {name}")

    address_book.delete(name)

    return "Contact deleted"


@input_error
def add_birthday(args, address_book: AddressBook):
    name, birthday = args
    contact = address_book.find(name)

    if contact == None:
        raise KeyError(f"There is no contact with name {name}")

    contact.add_birthday(birthday)
    return "Birthday added."


@input_error
def show_birthday(args, address_book: AddressBook):
    name, = args
    contact = address_book.find(name)

    if contact == None:
        raise KeyError(f"There is no contact with name {name}")

    if contact.birthday == None:
        raise ValueError("Contact doesn't have birthday info yet")

    return datetime.strftime(contact.birthday.value, "%d.%m.%Y")


@input_error
def birthdays(address_book: AddressBook):
    return address_book.get_upcoming_birthdays()
