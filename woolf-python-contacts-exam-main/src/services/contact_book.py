
from collections import UserList
from typing import List
from entities.record import Record


class ContactBook(UserList[Record]):

    def add_record(self, record: Record) -> None:
        self.data.append(record)

    def retrieve_contacts(self, searched_value: str = "") -> List:
        res = []

        for record in self.data:
            name = str(record.name)
            email = str(record.email)
            address = str(record.address)
            birthday = str(record.birthday)
            phones = [str(phone) for phone in record.phones]

            searchable = name + email + address + birthday + " ".join(phones)

            # if (searched_value in name or
            #         searched_value in email or
            #         searched_value in address or
            #         searched_value in birthday or
            #         searched_value in phones):

            if searched_value.lower() in searchable.lower():
                row = dict(name=name, email=email, address=address,
                           birthday=birthday, phones=phones)
                res.append(row)

        return res

    def remove_record(self, searched_name: str) -> None:
        self.data = [record for record in self.data if str(
            record.name) != searched_name]

    def find_record(self, searched_name: str) -> Record | None:
        return next((record for record in self.data if str(record.name) == searched_name), None)
