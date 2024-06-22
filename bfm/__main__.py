import argparse
from typing import Sequence

def comma_separated(value: str) -> list[str]:
    return value.split(",")

def main(argv: Sequence[str] | None = None) -> int: 
    parser = argparse.ArgumentParser(
        prog=__package__ or "app",
        description="Simple application that moves files",
    )
    
    
    parser.add_argument(
        "--source", "-s",
        type=str,
        required=False,
        help="Source file path",
    )
    
    parser.add_argument(
        "--destination", "-d",
        type=str,
        required=False,
        help="Destination file path",
    )
    
    parser.add_argument(
        "--prefix", "-p",
        type=str,
        required=False,
    )
    
    input_list_group = parser.add_argument_group('input_list')
    
    input_list_group.add_argument(
        "--txt",
        type=argparse.FileType("r"),
        required=False,
        help="List of files to move in txt",
    )
    input_list_group.add_argument(
        "--raw",
        type=comma_separated,
        required=False,
        help="List of files to move", 
        
    )
    
    args = parser.parse_args(argv)
    
    from . import app
    from .app import Args
    
    args = Args(**vars(args))
    app.main(args)
    
    return 0

if __name__ == "__main__":
    raise SystemExit(main())