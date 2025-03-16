"""
Note Class
==========

The `Note` class represents a single note with a title, text content, and associated tags. 
Each note is an independent entity, and its primary function is to store and manage textual 
information along with a list of tags for categorization or search purposes. 


"""

import os
from typing import List
from colorama import Fore
from src.helpers.wrap_text import wrap_text


class Note():
    def __init__(self, title: str, text: str) -> None:
        self.__title = None
        self.__text = None

        self.__tags: set[str] = set()
        self.title = title
        self.text = text

    @property
    def tags(self):
        return self.__tags

    @property
    def title(self) -> str:
        return str(self.__title)

    @title.setter
    def title(self, new_title: str):

        if not new_title:
            raise ValueError("Title cannot be empty")

        self.__title = new_title

    @property
    def text(self) -> str:
        return str(self.__text)

    @text.setter
    def text(self, new_text: str):
        self.__text = new_text

    def add_tags(self, tags: List[str]):
        self.__tags.update(tags)

    def remove_tags(self, tags: List[str]):
        for tag in tags:
            self.__tags.discard(tag)

    def get_tags(self):
        return [str(tag) for tag in self.__tags]

    def __str__(self) -> str:

        terminal_width = os.get_terminal_size().columns
        if terminal_width < 50:
            raise Exception(f"The width of terminal is {
                            terminal_width}. Please set width not less than 50")

        title = self.title
        text = self.text
        tags = [f"#{tag}" for tag in self.__tags]

        wrapped_text = wrap_text(text, 40)
        wrapped_tags = wrap_text(", ".join(tags), 40)

        TAB_COLOR = Fore.CYAN
        TEXT_COLOR = Fore.LIGHTBLACK_EX

        res = f"{TAB_COLOR}"

        res += "┌" + "─" * 10 + "┬" + "─" * 31 + "┐\n"

        res += "│{:<23}│ {:<40}│\n".format(
            f"\033[1mTitle\033[0m{TAB_COLOR}", f"{TEXT_COLOR}{title}{TAB_COLOR}")

        res += "├" + "─" * 10 + "┴" + "─" * 31 + "┤\n"

        res += "│{:<55}│\n".format(f"\033[1mText\033[0m{TAB_COLOR}")
        res += "│" + " " * 42 + "│\n"

        for row in wrapped_text:
            res += "│{:<52}│\n".format(f"{TEXT_COLOR}{str(row)}{TAB_COLOR}")

        res += "├" + "─" * 10 + "─" + "─" * 31 + "┤\n"

        res += "│{:<55}│\n".format(f"\033[1mTags\033[0m{TAB_COLOR}")
        res += "│" + " " * 42 + "│\n"
        for row in wrapped_tags:
            res += "│{:<52}│\n".format(f"{TEXT_COLOR}{str(row)}{TAB_COLOR}")

        res += "└" + "─" * 42 + "┘\n"

        return res
