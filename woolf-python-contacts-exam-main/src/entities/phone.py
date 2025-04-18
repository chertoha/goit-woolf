from entities.field import Field


class Phone(Field):

    def __init__(self, value: str) -> None:
        super().__init__(value)

    def __str__(self) -> str:
        return str(self._value)
