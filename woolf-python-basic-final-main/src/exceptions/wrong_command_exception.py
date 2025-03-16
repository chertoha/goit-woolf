class WrongCommandException(Exception):
    def __init__(self, message="Wrong command!") -> None:
        super().__init__(message)
