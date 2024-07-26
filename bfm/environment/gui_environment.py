from common import OVERRIDE_METHOD
import FreeSimpleGUI as sg
import tqdm
from bfm.environment.environment_protocol import Environment


class GuiEnvironment(Environment):
    def __init__(self):
        self.override_state = OVERRIDE_METHOD.ASK

    def show_message(self, message: str) -> None:
        sg.popup_ok(message)

    def ask_confirmation(self, message: str, title: str) -> bool:
        popup_answer: str = sg.popup_yes_no(title, message)
        return popup_answer == "Yes"

    def migration_progressbar(
        self, files_to_process: int
    ) -> sg.ProgressBar | tqdm.tqdm:
        layout = [
            [sg.Text("Migrating files...")],
            [
                sg.ProgressBar(
                    files_to_process, orientation="h", size=(20, 20), key="PROGRESS"
                )
            ],
            [sg.Button("Cancel")],
        ]
        window = sg.Window("Migration Progress", layout, modal=True, finalize=True, no_titlebar=True)
        return window

    def ask_override(self, file_name: str) -> bool:
        if self.override_state == OVERRIDE_METHOD.SKIP:
            return False
        if self.override_state == OVERRIDE_METHOD.ALL:
            return True

        popup_layout = [
            [sg.Text(f"File {file_name} already exists in destination, override?")],
            [
                sg.Button("Yes"),
                sg.Button("No"),
                sg.Button("Yes to All"),
                sg.Button("No to All"),
                sg.Button("Cancel"),
            ],
        ]
        popup_window = sg.Window("Override", popup_layout, modal=True)

        event, _ = popup_window.read()
        popup_window.close()

        if event == "Cancel":
            raise SystemExit(0)

        if event == "Yes to All":
            self.override_state = OVERRIDE_METHOD.ALL
            return True
        if event == "No to All":
            self.override_state = OVERRIDE_METHOD.SKIP
            return False
        return str(event) == "Yes"
