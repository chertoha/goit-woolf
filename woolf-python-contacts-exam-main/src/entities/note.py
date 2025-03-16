from typing import List
from entities.tag import Tag


class Note():
    def __init__(self, title: str, text: str) -> None:
        self.__title = None
        self.__text = None

        self.__tags: List[Tag] = []
        self.title = title
        self.text = text

    def add_tag(self, new_tag: str):
        self.__tags.append(Tag(new_tag))

    def find_tag(self, searched_tag: str):
        return next((tag for tag in self.__tags if str(tag) == searched_tag), None)

    def remove_tag(self, searched_tag: str):
        self.__tags = list(
            filter(lambda tag: str(tag) != searched_tag, self.__tags))

    def update_tag(self, old_tag: str, new_tag: str):
        index = next(index for index, tag in enumerate(
            self.__tags) if str(tag) == old_tag)
        self.__tags[index] = Tag(new_tag)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title: str):

        if not new_title:
            raise ValueError("Title cannot be empty")

        self.__title = new_title

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, new_text: str):
        self.__text = new_text
