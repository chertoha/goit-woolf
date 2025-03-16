from colorama import Fore, Style


class Logger:

    @staticmethod
    def success(message):
        print(Fore.LIGHTGREEN_EX, message, Style.RESET_ALL)

    @staticmethod
    def error(message):
        print(Fore.RED, message, Style.RESET_ALL)

    @staticmethod
    def warning(message):
        print(Fore.YELLOW, message, Style.RESET_ALL)
