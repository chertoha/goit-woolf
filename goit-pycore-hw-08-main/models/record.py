from typing import List
from models.birthday import Birthday
from models.name import Name
from models.phone import Phone


class Record:
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones: List[Phone] = []
        self.birthday = None

    def __str__(self):
        birthday = f", birthday: {
            self.birthday.value}" if self.birthday is not None else ""
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}" + birthday

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        self.phones = list(
            filter(lambda tel: tel.value != phone,  self.phones))

    def edit_phone(self, old_phone: str, new_phone: str):
        index = next(i for i, phone in enumerate(
            self.phones) if phone.value == old_phone)
        self.phones[index] = Phone(new_phone)

    def find_phone(self, phone):
        res = next((p for p in self.phones if p.value == phone), None)
        return res

    def add_birthday(self, value):
        self.birthday = Birthday(value)
