
from typing import List
from entities.address import Address
from entities.birthday import Birthday
from entities.email import Email
from entities.name import Name
from entities.phone import Phone


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

    @name.setter
    def name(self, new_name: Name):
        self.__name = new_name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address: Address):
        self.__address = new_address

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email: Email):
        self.__email = new_email

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, new_birthday: Birthday):
        self.__birthday = new_birthday

    @property
    def phones(self):
        return self.__phones

    def update_address(self, address: str):
        self.address = Address(address)

    def update_email(self, email: str):
        self.email = Email(email)

    def update_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)

    def add_phone(self, new_phone: str):
        self.__phones.append(Phone(new_phone))

    def remove_phone(self, searched_phone: str):
        self.__phones = list(filter(lambda phone: str(
            phone) != searched_phone, self.__phones))

    def edit_phone(self, old_phone: str, new_phone: str):
        index = next(index for index, phone in enumerate(
            self.__phones) if str(phone) == old_phone)

        self.__phones[index] = Phone(new_phone)

    def find_phone(self, searched_phone: str) -> Phone | None:
        return next((phone for phone in self.__phones if str(phone) == searched_phone), None)
