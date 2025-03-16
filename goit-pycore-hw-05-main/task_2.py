from typing import Callable
import re

pattern = r'(?<=\s)\d+(?:\.\d+)?(?=\s)'


def generator_numbers(text: str):
    for match in re.finditer(pattern, text):
        yield match.group()


def sum_profit(text: str, func: Callable):
    return sum([float(el) for el in generator_numbers(text)])


def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == "__main__":
    main()
