from typing import List
from src.helpers.logger import Logger
from src.decorators.catch import catch
from src.models.organizer import contact_book
from pprint import pprint


@catch
def find_contacts(args: List[str]):

    query = args[0] if len(args) >= 1 else ""

    records = contact_book.retrieve_contacts(query)

    if len(records) != 0:
        contact_book.show_records(records)
    elif query == "":
        Logger.warning(f"We found zero contacts. Don't be lazy, add some ;)")
    else:
        Logger.warning(f"Nothing found for query '{query}'")
