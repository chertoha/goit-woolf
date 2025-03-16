from src.helpers.logger import Logger
from src.exceptions.wrong_command_exception import WrongCommandException
from functools import wraps


def catch(func):

    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except WrongCommandException as err:
            Logger.error(err)

        except ValueError as err:
            Logger.error(err)

        except Exception as err:
            Logger.error(err)

    return inner
