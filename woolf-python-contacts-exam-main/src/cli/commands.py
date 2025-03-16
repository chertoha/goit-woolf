from typing import List
from cli.config import Commands
from decorators.catch import catch
from exceptions.wrong_command_exception import WrongCommandException
from services.contact_book_service import ContacBookService


commands = {
    Commands.ADD: ContacBookService.add,
    Commands.FIND: ContacBookService.find,
    Commands.UPDATE: ContacBookService.update,
    Commands.BIRTHDAY: ContacBookService.birthday,

}


@catch
def execute_command(command: str, args: List[str]):
    if any(cmd.value == command for cmd in Commands):
        handler = commands[Commands(command)]
        handler(args)
    else:
        raise WrongCommandException()
