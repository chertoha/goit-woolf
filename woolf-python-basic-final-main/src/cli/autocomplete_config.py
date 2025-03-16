from typing import List
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.styles import Style

autocmplete_style = Style.from_dict({
    'completion-menu.completion': 'bg:#444444 fg:#ffffff',
    'completion-menu.completion.current': 'bg:#888888 fg:#ffffff underline',
    'completion-menu.meta': 'bg:#444444 fg:#aaaaaa',
})


class CommandCompleter(Completer):

    def __init__(self, commands: List[str]) -> None:
        self.__commands = commands
        super().__init__()

    def get_completions(self, document, complete_event):
        text_before_cursor = document.text_before_cursor

        if not text_before_cursor.strip() or " " in text_before_cursor:
            return

        for cmd in self.__commands:
            if cmd.startswith(text_before_cursor):
                yield Completion(cmd, start_position=-len(text_before_cursor))
