from src.models.field import Field


class Address(Field):

    def __init__(self, value: str) -> None:
        super().__init__(value)

    def __str__(self) -> str:
        return str(self._value)
