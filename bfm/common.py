from dataclasses import dataclass
from argparse import FileType

@dataclass
class Args:
    source: str
    destination: str
    prefix: str
    txt: FileType
    raw: list[str]