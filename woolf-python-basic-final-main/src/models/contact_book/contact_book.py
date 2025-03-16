"""
The `ContactBook` class extends Python's `UserList` to manage contact records. It supports adding, searching, removing, exporting, and importing contacts, along with handling upcoming birthdays.
"""

from collections import UserList
from typing import List
from datetime import datetime, timedelta
from src.models.contact_book.address import Address
from src.models.contact_book.birthday import Birthday
from src.models.contact_book.email import Email
from .record import Record
import os
from colorama import Fore


class ContactBook(UserList[Record]):

    def add_record(self, record: Record) -> None:
        self.data.append(record)

    def retrieve_contacts(self, searched_value: str = "") -> List:

        if searched_value == "":
            return self.data

        res = []

        for record in self.data:

            name = str(record.name).lower()
            email = str(record.email).lower(
            ) if record.email is not None else ""
            address = str(record.address).lower(
            ) if record.address is not None else ""
            birthday = str(
                record.birthday).lower() if record.birthday is not None else ""
            phones = [str(phone).lower() for phone in record.phones]
            stringyfied_phones = " ".join(phones)

            if (searched_value.lower() in name or
                    searched_value in email or
                    searched_value in address or
                    searched_value in birthday or
                    searched_value in stringyfied_phones):

                res.append(record)

        return res

    def remove_record(self, searched_name: str) -> None:
        record = self.find_record(searched_name)
        if record:
            self.data.remove(record)
        else:
            raise ValueError(f"Contact with name '{searched_name}' not found.")

    def find_record(self, searched_name: str) -> Record | None:
        return next((record for record in self.data if str(record.name) == searched_name), None)

    def get_dump_state(self):
        state = []

        for record in self.data:
            name = str(record.name)
            address = str(
                record.address) if record.address is not None else None
            email = str(record.email) if record.email is not None else None
            birthday = str(
                record.birthday) if record.birthday is not None else None
            phones = [str(phone) for phone in record.phones]

            state.append(
                {"name": name, "phones": phones, "birthday": birthday, "address": address, "email": email})

        return state

    def set_dump_state(self, state):

        for contact in state:
            record = Record(contact["name"])

            if contact["birthday"] is not None:
                record.birthday = Birthday(contact["birthday"])

            if contact["email"] is not None:
                record.email = Email(contact["email"])

            if contact["address"] is not None:
                record.address = Address(contact["address"])

            for phone in contact["phones"]:
                record.add_phone(phone)

            self.add_record(record)

    def show_records(self, records: List[Record]):

        for record in records:
            print(record)

    def get_upcoming_birthdays(self, days):
        current_date = datetime.today().date()

        res = []

        for record in self.data:

            birthday = record.birthday

            if birthday == None:
                continue

            date = birthday.to_datetime()

            comparing_year = current_date.year
            if (date.month, date.day) < (current_date.month, current_date.day):
                comparing_year += 1

            comparing_date = datetime(
                comparing_year, date.month, date.day).date()

            if comparing_date < current_date or comparing_date >= current_date + timedelta(days=days):
                continue

            congrats_date = comparing_date

            if comparing_date.weekday() == 5:
                congrats_date = comparing_date + timedelta(days=2)
            elif comparing_date.weekday() == 6:
                congrats_date = comparing_date + timedelta(days=1)

            res.append(
                {"name": str(record.name), "birthday_date": date.strftime("%d.%m.%Y"), 'congratulation_date': congrats_date.strftime("%d.%m.%Y")})

        return sorted(res, key=lambda elem: elem["congratulation_date"])

    def show_birthdays(self, birthdays):

        terminal_width = os.get_terminal_size().columns
        print(terminal_width)
        if terminal_width < 50:
            raise Exception(f"The width of terminal is {
                            terminal_width}. Please set width not less than 50")

        TAB_COLOR = Fore.YELLOW
        TEXT_COLOR = Fore.LIGHTBLACK_EX

        for birthday in birthdays:

            name = birthday["name"]
            birthday_date = birthday["birthday_date"]
            congratulation_date = birthday["congratulation_date"]

            res = f"{TAB_COLOR}"
            res += "┌" + "─" * 17 + "┬" + "─" * 25 + "┐\n"

            res += "│{:<30}│ {:<34}│\n".format(
                f"\033[1mName\033[0m{TAB_COLOR}", f"{TEXT_COLOR}{name}{TAB_COLOR}")

            res += "├" + "─" * 17 + "┼" + "─" * 25 + "┤\n"

            res += "│{:<30}│ {:<34}│\n".format(
                f"\033[1mBirthday\033[0m{TAB_COLOR}", f"{TEXT_COLOR}{birthday_date}{TAB_COLOR}")

            res += "├" + "─" * 17 + "┼" + "─" * 25 + "┤\n"

            res += "│{:<30}│ {:<34}│\n".format(
                f"\033[1mCongratulation\033[0m{TAB_COLOR}", f"{TEXT_COLOR}{congratulation_date}{TAB_COLOR}")
            res += "│{:<30}│{:25}│\n".format(
                f"\033[1mdate\033[0m{TAB_COLOR}", " ")

            res += "└" + "─" * 17 + "┴" + "─" * 25 + "┘\n"

            print(res)
