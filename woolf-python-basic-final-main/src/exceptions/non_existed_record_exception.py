class NonExistedException(Exception):
    def __init__(self, name: str) -> None:
        message = f"Record with name '{name}' doesn't exist"
        super().__init__(message)
