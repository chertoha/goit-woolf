"""
Email Class
===========

The `Email` class is a subclass of the `Field` class, designed to represent and validate email addresses. 
It ensures that the provided email matches a specific pattern, typically a standard email format.


The class provides an encapsulated way to represent email addresses with built-in validation 
to ensure that only valid email addresses can be stored in an instance of this class.
"""

from src.models.field import Field
from src.utils.patterns import email_pattern
import re


class Email(Field):

    def __init__(self, value: str) -> None:
        self.__validate(value)
        super().__init__(value)

    def __str__(self) -> str:
        return str(self._value)

    def __validate(self, value):
        if not bool(re.match(email_pattern, value)):
            raise ValueError("Not valid email!")
