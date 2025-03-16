from src.models.db import Database


db = Database()

organizer_instance = db.load_data()

contact_book = organizer_instance.contact_book
note_book = organizer_instance.note_book
