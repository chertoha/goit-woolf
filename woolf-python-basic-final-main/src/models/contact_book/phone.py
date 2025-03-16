"""
Phone Class
===========

The `Phone` class is a subclass of the `Field` class, designed to represent and validate phone numbers. 
It ensures that the phone number provided matches a specific pattern (usually for a 10-digit number, 
but this can be adjusted based on the `phone_pattern`).

The class provides an encapsulated way to represent phone numbers with built-in validation 
to ensure that only valid phone numbers can be stored in an instance of this class.
"""

from src.models.field import Field
from src.utils.patterns import phone_pattern
import re


class Phone(Field):

    def __init__(self, value: str) -> None:
        self.__validate(value)
        super().__init__(value)

    def __str__(self) -> str:
        return str(self._value)

    def __validate(self, value):
        if not bool(re.match(phone_pattern, value)):
            raise ValueError("Not valid phone! Must be 10 digits")
