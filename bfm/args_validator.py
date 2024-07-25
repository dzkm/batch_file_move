import os
from common import Args
from pathlib import Path


def validate_folder(path: str) -> bool:
    if path is not None and os.path.isdir(path):
        return True
    raise ValueError("%s is not a valid folder" % path)


def diff_paths(path1: str, path2: str) -> bool:
    if validate_folder(path1) and validate_folder(path2):
        if path1 != path2:
            return True
    raise ValueError("Source and destination folders can't be the same")


def validate_file(path: str | Path) -> bool:
    if path is not None and os.path.isfile(path):
        return True
    raise ValueError("%s is not a valid file" % path)


def validate_raw_list(raw_list: list[str]) -> bool:
    new_list = []
    for item in raw_list:
        item = item.strip()
        if item == "" or item is None:
            continue
        new_list.append(item)

    if len(new_list) > 0:
        return True
    raise ValueError("Empty raw list")


def validate_txt_file(path: Path) -> bool:
    if path is not None:
        if path.name.endswith(".txt") and validate_file(path):
            return True
    raise ValueError("Invalid txt file")


def validate_all(args: Args) -> bool:
    validate_folder(args.source)
    validate_folder(args.destination)
    diff_paths(args.source, args.destination)
    if args.txt != "":
        args.txt = Path(args.txt)
        validate_txt_file(args.txt)
    elif args.raw != [""]:
        validate_raw_list(args.raw)
    return True
