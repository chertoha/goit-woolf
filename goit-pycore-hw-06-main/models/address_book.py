from collections import UserDict
from typing import List
from models.record import Record


class AddressBook(UserDict[str, Record]):

    def add_record(self, record: Record):

        self.data[record.name.value] = record

    def find(self, name: str):
        if name in self.data:
            return self.data[name]

    def delete(self, name):
        if self.data[name]:
            del self.data[name]

    def show(self) -> List:
        res = []
        for _, record in self.data.items():
            row = dict()
            row[record.name.value] = [phone.value for phone in record.phones]
            res.append(row)

        return res
