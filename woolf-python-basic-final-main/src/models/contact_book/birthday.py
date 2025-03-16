"""
Birthday Class
==============

The `Birthday` class is a subclass of the `Field` class, designed to represent and validate a person's birthday. 
It ensures that the provided date is in the correct format and stores it as a `datetime` object for easier manipulation.

The class is useful for storing and validating birthdates in a structured format, ensuring that only correctly formatted dates can be saved and manipulated.
"""

from src.models.field import Field
from datetime import datetime


class Birthday(Field):
    def __init__(self, value: str):
        try:
            date = datetime.strptime(value, "%d.%m.%Y")
            super().__init__(date)

        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self) -> str:
        return datetime.strftime(self._value, "%d.%m.%Y")

    def to_datetime(self):
        return self._value
