import tqdm
from typing import Protocol
import FreeSimpleGUI as sg


class Environment(Protocol):

    def __init__(self): ...

    def show_message(self, message: str) -> None: ...

    def migration_progressbar(
        self, files_to_process: int
    ) -> sg.ProgressBar | tqdm.tqdm: ...

    def ask_confirmation(
        self,
        message: str,
        title: str,
    ) -> bool: ...

    def ask_override(self, file_name: str) -> bool: ...
