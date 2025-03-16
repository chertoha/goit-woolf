from pprint import pprint
from contacts import *
from models.address_book import AddressBook
from models.record import Record


def main():

    address_book = AddressBook()

    record_1 = Record("Anton")
    record_1.add_phone("0667262367")
    record_1.add_phone("0667262369")

    record_2 = Record("Eva")
    record_2.add_phone("3874626605")

    record_3 = Record("Ivan")
    record_3.add_phone("0671643024")

    address_book.add_record(record_1)
    address_book.add_record(record_2)
    address_book.add_record(record_3)

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

            else:
                raise ValueError("Invalid command.")

        except Exception as err:
            display_error("Error: ", err)


if __name__ == "__main__":
    main()
