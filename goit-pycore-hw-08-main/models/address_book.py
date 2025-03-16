from collections import UserDict
from typing import List
from models.record import Record
from datetime import datetime, timedelta


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
            phones = [phone.value for phone in record.phones]
            birthday = datetime.strftime(
                record.birthday.value, "%d.%m.%Y") if record.birthday is not None else None

            row = dict()
            row[record.name.value] = {"phones": phones,
                                      "birthday": birthday}
            res.append(row)

        return res

    def get_upcoming_birthdays(self):
        current_date = datetime.today().date()

        res = []

        for _, record in self.data.items():

            birthday = record.birthday

            if birthday == None:
                continue

            date = birthday.value

            comparing_year = current_date.year
            if (date.month, date.day) < (current_date.month, current_date.day):
                comparing_year += 1

            comparing_date = datetime(
                comparing_year, date.month, date.day).date()

            if comparing_date < current_date or comparing_date >= current_date + timedelta(days=7):
                continue

            congrats_date = comparing_date

            if comparing_date.weekday() == 5:
                congrats_date = comparing_date + timedelta(days=2)
            elif comparing_date.weekday() == 6:
                congrats_date = comparing_date + timedelta(days=1)

            res.append(
                {"name": record.name.value, "birthday_date": date, 'congratulation_date': congrats_date.strftime("%d.%m.%Y")})

        return sorted(res, key=lambda elem: elem["congratulation_date"])

    def __getstate__(self) -> object:
        state = []

        for _, record in self.data.items():
            name = record.name.value
            birthday = record.birthday.value if record.birthday is not None else None
            phones = [phone.value for phone in record.phones]
            state.append(
                {"name": name, "phones": phones, "birthday": birthday})
        return state

    def __setstate__(self, state):
        super().__init__()

        for contact in state:
            record = Record(contact["name"])

            if record.birthday != None:
                record.add_birthday(contact["birthday"])

            for phone in contact["phones"]:
                record.add_phone(phone)

            self.add_record(record)
