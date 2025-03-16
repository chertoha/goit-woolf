class WrongArgumentsNumberException(Exception):
    def __init__(self, number_of_arguments: int) -> None:
        message = f"Wrong number of arguments in command!, should be at least {
            number_of_arguments}"
        super().__init__(message)
