
from .print_error import display_error


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as err:
            display_error("Key error:", err)
        except ValueError as err:
            display_error("Value error:", err)
        except IndexError as err:
            display_error("Index error:", err)

    return inner
