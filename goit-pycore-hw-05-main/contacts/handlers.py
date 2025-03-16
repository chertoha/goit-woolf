from .decorators import input_error


@input_error
def add_contact(args, contacts):
    name, phone = args

    if name in contacts.keys():
        raise KeyError(f"Contact {name} is already existed")

    if phone in contacts.values():
        raise ValueError(f"Phone {phone} has another contact")

    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args

    if not name in contacts.keys():
        raise KeyError(f"There is no contact with name {name}")

    if phone in contacts.values():
        raise ValueError(f"Phone {phone} has another contact")

    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    if len(args) == 0:
        raise IndexError("No arguments")

    name, = args

    if not name in contacts.keys():
        raise KeyError(f"There is no contact with name {name}")

    return contacts[name]


def show_all(contacts):
    return contacts
