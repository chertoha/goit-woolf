from entities.field import Field
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
