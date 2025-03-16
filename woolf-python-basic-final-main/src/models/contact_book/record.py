"""
Record Class
============

The `Record` class is designed to represent an individual contact within a contact 
management system. It stores personal information such as the contact's name, 
address, email, birthday, and phone numbers. This class allows managing and organizing 
a contact's details, providing the ability to add, update, and remove various attributes 
associated with a person.


"""

import os
from typing import List

from src.helpers.wrap_text import wrap_text
from .address import Address
from .birthday import Birthday
from .email import Email
from .name import Name
from .phone import Phone
from colorama import Fore


class Record:

    def __init__(self, name: str) -> None:

        self.__name: Name | None = None
        self.__address: Address | None = None
        self.__email: Email | None = None
        self.__birthday: Birthday | None = None
        self.__phones: List[Phone] = []

        self.name = Name(name)

    @property
    def name(self):
        return self.__name

    def update_name(self, new_name: str):
        self.__name = Name(new_name)

    @name.setter
    def name(self, new_name: Name):
        self.__name = new_name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address: Address | None):
        self.__address = new_address

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email: Email | None):
        self.__email = new_email

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, new_birthday: Birthday | None):
        self.__birthday = new_birthday

    @property
    def phones(self):
        return self.__phones

    def add_phone(self, new_phone: str):
        self.__phones.append(Phone(new_phone))

    def update_phone(self, old_phone: str, new_phone: str):
        for i, phone in enumerate(self.__phones):
            if str(phone) == old_phone:
                self.__phones[i] = Phone(new_phone)
                return

    def remove_phone(self, searched_phone: str):
        self.__phones = list(filter(lambda phone: str(
            phone) != searched_phone, self.__phones))

    def find_phone(self, searched_phone: str) -> Phone | None:
        return next((phone for phone in self.__phones if str(phone) == searched_phone), None)

    def __str__(self):
        terminal_width = os.get_terminal_size().columns
        if terminal_width < 50:
            raise Exception(f"The width of terminal is {
                            terminal_width}. Please set width not less than 50")

        name = str(self.name)
        email = str(self.email) if self.email is not None else "-"
        birthday = str(self.birthday) if self.birthday is not None else "-"
        address = str(self.address) if self.address is not None else "-"

        wrapped_address = wrap_text(address, 40)

        TAB_COLOR = Fore.CYAN
        TEXT_COLOR = Fore.LIGHTBLACK_EX

        res = f"{TAB_COLOR}"

        res += "┌" + "─" * 10 + "┬" + "─" * 31 + "┐\n"

        res += "│{:<23}│ {:<40}│\n".format(
            f"\033[1mName\033[0m{TAB_COLOR}", f"{TEXT_COLOR}{name}{TAB_COLOR}")

        res += "├" + "─" * 10 + "┼" + "─" * 31 + "┤\n"

        res += "│{:<23}│ {:<40}│\n".format(
            f"\033[1mEmail\033[0m{TAB_COLOR}", f"{TEXT_COLOR}{email}{TAB_COLOR}")

        res += "├" + "─" * 10 + "┼" + "─" * 31 + "┤\n"

        res += "│{:<23}│ {:<40}│\n".format(
            f"\033[1mBirthday\033[0m{TAB_COLOR}", f"{TEXT_COLOR}{birthday}{TAB_COLOR}")

        res += "├" + "─" * 10 + "┴" + "─" * 31 + "┤\n"

        res += "│{:<55}│\n".format(f"\033[1mAddress\033[0m{TAB_COLOR}")
        res += "│" + " " * 42 + "│\n"
        for row in wrapped_address:
            res += "│{:<52}│\n".format(f"{TEXT_COLOR}{str(row)}{TAB_COLOR}")

        res += "├" + "─" * 10 + "─" + "─" * 31 + "┤\n"

        res += "│{:<55}│\n".format(f"\033[1mPhones\033[0m{TAB_COLOR}")
        res += "│" + " " * 42 + "│\n"
        for phone in self.phones:
            res += "│{:<52}│\n".format(f"{TEXT_COLOR}{str(phone)}{TAB_COLOR}")

        res += "└" + "─" * 42 + "┘\n"

        return res
