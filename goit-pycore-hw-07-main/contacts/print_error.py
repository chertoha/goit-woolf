from colorama import Fore, Style


def display_error(message, err):
    print(Fore.RED, message, err, Style.RESET_ALL)
