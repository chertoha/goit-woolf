from pprint import pprint
from colorama import Fore, Style
from contacts import *


def main():
    contacts = {
        "Anton": "380667262367",
        "Eva": "353874626605",
        "Ivan": "380671643024",
    }

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
                print(add_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "all":
                pprint(show_all(contacts), indent=4)
            elif command == "change":
                print(change_contact(args, contacts))
            else:
                raise ValueError("Invalid command.")

        except Exception as err:
            display_error("Error: ", err)


if __name__ == "__main__":
    main()
