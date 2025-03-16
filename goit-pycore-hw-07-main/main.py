from pprint import pprint
from contacts import *
from contacts.handlers import add_birthday, birthdays, show_birthday
from data.mock_contacts import get_mock_contacts
from models.address_book import AddressBook
from models.record import Record


def fill_address_book(address_book: AddressBook):
    for contact in get_mock_contacts():
        record = Record(contact["name"])

        if "birthday" in contact:
            record.add_birthday(contact["birthday"])

        for phone in contact["phones"]:
            record.add_phone(phone)

        address_book.add_record(record)


def main():

    address_book = AddressBook()
    fill_address_book(address_book)

    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ").strip()
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")

            elif command == "add":
                print(add_contact(args, address_book))

            elif command == "phone":
                print(show_phone(args, address_book))

            elif command == "all":
                pprint(show_all(address_book), indent=4)

            elif command == "change":
                print(change_contact(args, address_book))

            elif command == "delete":
                print(delete_contact(args, address_book))

            elif command == "add-birthday":
                print(add_birthday(args, address_book))

            elif command == "show-birthday":
                print(show_birthday(args, address_book))

            elif command == "birthdays":
                pprint(birthdays(address_book), indent=4)

            else:
                raise ValueError("Invalid command.")

        except Exception as err:
            display_error("Error: ", err)


if __name__ == "__main__":
    main()
