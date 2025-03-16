import asyncio
import logging
from pathlib import Path
from argparse import ArgumentParser
import aiofiles

DEFAULT_FOLDER = "dist"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def copy_file(src: Path, dest: Path):
    try:
        dest.mkdir(parents=True, exist_ok=True)
        async with aiofiles.open(src, 'rb') as f_src:
            async with aiofiles.open(dest / src.name, 'wb') as f_dest:
                await f_dest.write(await f_src.read())
        logging.info(f"Copied: {src} -> {dest / src.name}")
    except Exception as e:
        logging.error(f"Failed to copy {src}: {e}")

async def read_folder(src: Path, dest: Path):
    tasks = []
    for item in src.iterdir():
        if item.name in {".git", ".venv"}:
            continue
        if item.is_dir():
            tasks.append(read_folder(item, dest))
        else:
            ext = item.suffix.lstrip('.') or "unknown"
            tasks.append(copy_file(item, dest / ext))
    await asyncio.gather(*tasks)

async def main():
    parser = ArgumentParser(description="Asynchronous file sorter")
    parser.add_argument("source", type=Path, help="Source folder")
    parser.add_argument("destination", type=Path, nargs='?', default=Path(DEFAULT_FOLDER), help="Destination folder")
    args = parser.parse_args()

    if not args.source.exists():
        logging.error("Source folder does not exist")
        return

    await read_folder(args.source, args.destination)

if __name__ == "__main__":
    asyncio.run(main())
