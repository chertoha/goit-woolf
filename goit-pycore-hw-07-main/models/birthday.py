from models.field import Field
from datetime import datetime


class Birthday(Field):
    def __init__(self, value):
        try:
            if type(value) != str:
                raise TypeError()

            date = datetime.strptime(value, "%d.%m.%Y")

            super().__init__(date)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        except TypeError:
            raise TypeError("Invalid date type. Must be a string")
