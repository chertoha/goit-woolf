class WrongArgumentsNumberException(Exception):
    def __init__(self, message="Wrong number of arguments in command!") -> None:
        super().__init__(message)
