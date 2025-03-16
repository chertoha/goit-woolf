from typing import List
from src.helpers.logger import Logger
from src.decorators.catch import catch
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.organizer import note_book
from src.decorators.confirm import confirm


@catch
@confirm("Are you sure you want to delete these tags?")
def remove_tags(args: List[str]):
    if len(args) < 2:
        raise WrongArgumentsNumberException(2)

    title, *tags = args

    note = note_book.find_note(title)

    if note:
        tags_set = set(tags)
        common_tags = tags_set.intersection(note.tags)
        if not common_tags:
            Logger.error(f"Not tags for delete in your tag list")
            return

        note.remove_tags(tags)
        Logger.success(f"Tag - {tags} successfully deleted.")
        print(note)

    else:
        raise KeyError(f"Note with title - {title} doesn't exist")
