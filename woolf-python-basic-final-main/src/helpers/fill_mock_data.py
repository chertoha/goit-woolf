import json
import os
from src.models.contact_book.address import Address
from src.models.contact_book.birthday import Birthday
from src.models.contact_book.email import Email
from src.models.contact_book.record import Record
from src.models.note_book.note import Note
from src.models.organizer import contact_book
from src.models.organizer import note_book


def fill_mock_data():

    if os.path.exists("data/organizer.pkl"):
        return

    with open('data/mock_contacts.json', 'r') as fc:
        mock_contacts = json.load(fc)

    for contact in mock_contacts:
        record = Record(contact["name"])
        for tel in contact["phones"]:
            record.add_phone(tel)

        if "email" in contact:
            record.email = Email(contact["email"])

        if "address" in contact:
            record.address = Address(contact["address"])

        if "birthday" in contact:
            record.birthday = Birthday(contact["birthday"])

        contact_book.add_record(record)

    with open('data/mock_notes.json', 'r') as fn:
        mock_notes = json.load(fn)

    for item in mock_notes:
        note = Note(item["title"], item["text"])

        if "tags" in item:
            note.add_tags(item["tags"])

        note_book.add_note(note)
