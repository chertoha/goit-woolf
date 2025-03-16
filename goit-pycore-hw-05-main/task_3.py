import sys
from pathlib import Path
from logs import *


levels = ["error", "info", "debug", "warning"]


def main():
    level: str = None

    try:
        _, *args = sys.argv
        if len(args) == 0:
            raise ValueError("No arguments")

        path = Path(args[0])
        if not path.exists() or not path.is_file():
            raise FileNotFoundError(
                f"File with path '{args[0]}' not found")

        if len(args) > 1:
            if not args[1] in levels:
                raise ValueError("Wrong level argument")
            else:
                level = args[1].lower()

        logs = load_logs(path)
        filtered_logs = filter_logs_by_level(
            logs, level) if level != None else logs

        display_log_counts(count_logs_by_level(logs), level)

        display_log_details(filtered_logs, level)

    except Exception as err:
        print(Fore.RED, "Error, ", err, Style.RESET_ALL)


if __name__ == "__main__":
    main()
