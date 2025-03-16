def add_contact(args, contacts):
    name, phone = args

    if name in contacts.keys():
        raise ValueError(f"Contact {name} is already existed")

    if phone in contacts.values():
        raise ValueError(f"Phone {phone} has another contact")

    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args

    if not name in contacts.keys():
        raise ValueError(f"There is no contact with name {name}")

    if phone in contacts.values():
        raise ValueError(f"Phone {phone} has another contact")    

    contacts[name] = phone
    return "Contact updated."




def show_phone(args, contacts):
    if len(args)== 0:
        raise ValueError("No arguments")

    name, = args
    
    if not name in contacts.keys():
        raise ValueError(f"There is no contact with name {name}")

    return contacts[name]


def show_all(contacts):
    return contacts