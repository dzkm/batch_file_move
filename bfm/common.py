from dataclasses import dataclass
from enum import Enum


@dataclass
class Args:
    source: str
    destination: str
    prefix: str
    txt: str
    raw: list[str]


class LIST_TYPE(Enum):
    TXT_FILE = 1, ".txt"
    INPUT = 2, "input"
