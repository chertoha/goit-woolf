from src.helpers.fill_mock_data import fill_mock_data
from src.helpers.logger import Logger
from src.handlers.show_help import show_help
from src.cli.autocomplete_config import CommandCompleter, autocmplete_style
from src.cli.config import Commands
from src.cli.commands import execute_command
from src.cli.parser import parse_input
from prompt_toolkit import PromptSession
from src.models.organizer import db
from src.models.organizer import organizer_instance


def app() -> None:

    fill_mock_data()

    COMMANDS = [cmd.value for cmd in Commands]

    autocomplete_session = PromptSession(
        completer=CommandCompleter(COMMANDS), style=autocmplete_style)

    while True:
        try:
            user_input = autocomplete_session.prompt(
                "Enter a command: ").strip()
            command, *args = parse_input(user_input)

            if command in ["exit", "quit", "end"]:
                print("Bye!")
                break

            if command.lower() == "help":
                show_help()

            execute_command(command, args)
            db.save_data(organizer_instance)

        except Exception as err:
            Logger.error(err)
