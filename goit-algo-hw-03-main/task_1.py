import sys
import shutil
from pathlib import Path


DEFAULT_FOLDER = "dist"


def main():

    try:
        args = sys.argv

        if len(args) < 2:
            raise Exception(
                "Specify folder!")

        folder_from = Path(args[1])
        folder_to = Path(args[2]) if len(args) >= 3 else Path(DEFAULT_FOLDER)

        folder_recursion(folder_from, folder_to)

        if (not folder_from.exists()):
            raise FileNotFoundError("Folder not found")

    except Exception as err:
        print(err)


def folder_recursion(path: Path, to: Path):
    for item in path.iterdir():
        if item.name == ".git" or item.name == ".venv":
            continue

        if item.is_dir():
            inner_path = path / item.name
            folder_recursion(inner_path, to)
        else:
            ext = item.suffix.split(".")[1]
            destination_path = to / ext
            destination_path.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, destination_path)


if __name__ == "__main__":
    main()
