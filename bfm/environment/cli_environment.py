import FreeSimpleGUI
from bfm.common import OVERRIDE_METHOD
from tqdm import tqdm
import FreeSimpleGUI as sg
from bfm.environment.environment_protocol import Environment


class ProgressBar:
    def __init__(self, total: int):
        self.total = total
        self.current = 0

    # Following function was grabbed from https://stackoverflow.com/a/34325723
    def draw(self):
        percent = ("{0:.2f}").format(100 * (self.current / float(self.total)))
        filledLength = int(self.total * self.current // self.total)
        bar = "+" * filledLength + "-" * (self.total - filledLength)
        print(f'\r{"Progress"} |{bar}| {percent}% {"Complete"}', end="\r\n")
        # Print New Line on Complete
        if self.current == self.total:
            print()

    def update(self, value: int) -> None:
        self.current = value
        print(f"Progress: {self.current} of {self.total}")


class CliEnvironment(Environment):
    def __init__(self):
        self.override_state = OVERRIDE_METHOD.ASK

    def show_message(self, message: str) -> None:
        print(message)

    def ask_confirmation(self, message: str, title: str) -> bool:
        print("%s\n%s(Y/n)" % (title, message))
        while True:
            answer = input()
            if answer.lower() not in ["y", "n"]:
                print("Invalid input, please type 'y' or 'n'")
            return answer.lower() != "n"

    def migration_progressbar(self, files_to_process: int) -> sg.ProgressBar | tqdm:
        return tqdm(
            desc="Migrating files",
            total=files_to_process,
            ascii=True,
            unit="files",
            unit_scale=True,
            gui=False,
        )

    def ask_override(self, file_name: str) -> bool:

        if self.override_state == OVERRIDE_METHOD.SKIP:
            return False

        if self.override_state == OVERRIDE_METHOD.ALL:
            return True

        print(
            "File %s already exists in destination, override? ((y)es/(n)o/Yes to (A)ll/(S)kip to all/(C)ancel)"
            % file_name
        )
        while True:
            answer = input()
            if answer.lower() not in ["y", "n", "a", "s", "c"]:
                print("Invalid input, please type 'y', 'n', 'a' or 's'")

            if answer.lower() == "c":
                raise SystemExit(0)

            if answer.lower() == "a":
                self.override_state = OVERRIDE_METHOD.ALL
                return True
            if answer.lower() == "s":
                self.override_state = OVERRIDE_METHOD.SKIP
                return False
            return answer.lower() == "y"
