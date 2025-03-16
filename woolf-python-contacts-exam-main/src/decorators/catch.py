from exceptions.wrong_command_exception import WrongCommandException
from functools import wraps


def catch(func):

    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except WrongCommandException as err:
            print(err)

        except ValueError as err:
            print(err)

        except Exception as err:
            print(err)

    return inner
