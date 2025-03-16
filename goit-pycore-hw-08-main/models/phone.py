from .field import Field


class Phone(Field):

    def __init__(self, value):
        self.__validate(value)
        super().__init__(value)

    def get_value(self):
        return self.value

    def __validate(self, value):
        if len(value) != 10:
            raise ValueError("Phone number must have 10 digits")
