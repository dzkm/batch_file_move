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
    if raw_list is not None and len(raw_list) > 0:
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
    if (args.txt != "" and args.txt is not None) and (
        args.raw != "" and args.raw is not None
    ):
        raise ValueError("Can't use txt and raw list at the same time")
    if args.txt != "":
        validate_txt_file(args.txt)
    elif args.raw != "":
        validate_raw_list(args.raw)
    return True
