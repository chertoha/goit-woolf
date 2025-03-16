import readline
from cli.commands import execute_command
from cli.config import Commands
from cli.parser import parse_input


def completer(text, state):
    commands = [command.value for command in Commands]
    matches = [cmd for cmd in commands if cmd.startswith(text)]
    if state < len(matches):
        return matches[state]
    return None


def main() -> None:

    readline.set_completer(completer)  # type: ignore
    readline.parse_and_bind("tab: complete")  # type: ignore

    while True:

        try:
            user_input = input("Enter a command: ").strip()
            command, *args = parse_input(user_input)

            if command in ["exit", "quit", "end"]:
                print("Bye!")
                break

            execute_command(command, args)

        except Exception as err:
            print(err)


if __name__ == "__main__":
    main()


# from prompt_toolkit import PromptSession
# from prompt_toolkit.completion import WordCompleter
# from prompt_toolkit.styles import Style

# # Команды для автокомплита
# COMMANDS = ["add-phone", "phone", "address", "specification"]

# # Настраиваем стили
# custom_style = Style.from_dict({
#     'completion-menu.completion': 'bg:#444444 fg:#ffffff',  # Цвет подсказок
#     'completion-menu.completion.current': 'bg:#888888 fg:#ffffff underline',  # Выбранный пункт
#     'completion-menu.meta': 'bg:#444444 fg:#aaaaaa',  # Полупрозрачные мета-информации
# })

# # Создаём автокомплитер
# completer = WordCompleter(COMMANDS, ignore_case=True, meta_dict={
#                           cmd: "Command" for cmd in COMMANDS})

# # Создаём сессию
# session = PromptSession(completer=completer, style=custom_style)

# # Основной цикл
# while True:
#     try:
#         user_input = session.prompt("Enter a command: ")
#         if user_input == "exit":
#             print("Goodbye!")
#             break
#         print(f"You entered: {user_input}")
#     except KeyboardInterrupt:
#         print("\nExiting...")
#         break
