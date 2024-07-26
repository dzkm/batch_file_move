from dataclasses import dataclass
from enum import Enum
from pathlib import Path


@dataclass
class Args:
    copy: bool
    source: str
    destination: str
    prefix: str
    txt: Path
    raw: list[str]


class LIST_TYPE(Enum):
    TXT_FILE = 1, ".txt"
    INPUT = 2, "input"


class OVERRIDE_METHOD(Enum):
    ASK = 0
    ALL = 1
    SKIP = 2
