from src.decorators.catch import catch
from src.cli.commands import commands
from colorama import Fore, Style


@catch
def show_help():

    print("\n\033[1mAvailable commands:\033[0m\n")
    for command, details in commands.items():

        description = details.get("description", "No description available")

        print(f"{Fore.GREEN}\033[1m{command.value}\033[0m")
        print(f"\033[3m{description}\033[0m\n")
