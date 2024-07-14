from pathlib import Path
import os
import bfm.file_handler as fm
from bfm.common import Args
from alive_progress import alive_bar
from time import sleep
import FreeSimpleGUI as sg


def migrate_file(file: Path, destination: str, copy: bool = False) -> tuple[bool, str]:
    if copy:
        return fm.copy_file(file, destination)

    return fm.move_file(file, destination)


def cli_migration(
    files_to_move: set[Path], destination: str, copy: bool = False
) -> tuple[list[str], list[str]]:
    success = []
    failed = []
    with alive_bar((len(files_to_move))) as bar:
        for file in files_to_move:
            bar()
            move_file_result = migrate_file(file, destination, copy)
            sleep(3)  # Just so the user gets more feedback, can be removed if needed
            if not move_file_result[0]:
                failed.append(move_file_result[1])
                continue
            success.append(move_file_result[1])
            continue
    return success, failed


def gui_migration(
    files_to_move: set[Path], destination: str, copy: bool = False
) -> tuple[list[str], list[str]]:
    window = sg.Window(
        "Migração de arquivos",
        layout=[
            [sg.Text("Migrando arquivos...")],
            [
                sg.ProgressBar(
                    len(files_to_move), orientation="h", size=(20, 20), key="progress"
                )
            ],
            [sg.Button("Interromper")],
            [
                sg.Multiline(
                    size=(50, 10), key="output", disabled=True, echo_stdout_stderr=True
                )
            ],
        ],
    )

    progressbar = window["progress"]

    success = []
    failed = []
    total_files = len(files_to_move)
    current_file = 1
    for file in files_to_move:
        event, values = window.read(timeout=100)
        if event == "Interromper":
            cancel_yes_no = sg.popup_yes_no(
                "Deseja realmente cancelar a migração?", title="Cancelar migração"
            )
            if cancel_yes_no == "yes":
                break
        current_file += 1
        progressbar.UpdateBar(current_file, total_files)
        move_file_result = migrate_file(file, destination, copy)
        if not move_file_result[0]:
            print("Falha ao mover %s\n" % move_file_result[1])
            failed.append(move_file_result[1])
        else:
            print("Movido com sucesso %s\n" % move_file_result[1])
            success.append(move_file_result[1])
        sleep(0.1)
        continue
    return success, failed


def start_migration(args: Args, is_gui: bool) -> list[str] | bool:
    id_list = args.raw if not os.path.isfile(args.txt) else fm.txt_file_parser(args.txt)

    files_to_move = fm.get_files_to_move(args.source, args.prefix, id_list)

    if not files_to_move:
        if not is_gui:
            print("[ERROR] Nenhum arquivo para mover")
            return False

        sg.popup(
            "Nenhum arquivo encontrado para mover.",
            title="Erro",
            keep_on_top=True,
            button_type=sg.POPUP_BUTTONS_CANCELLED,
        )
        return False

    if not is_gui:
        migration_results = cli_migration(files_to_move, args.destination)
        return migration_results[1] if len(migration_results[1]) > 0 else True

    migration_results = gui_migration(files_to_move, args.destination)
    return migration_results[1] if len(migration_results[1]) > 0 else True
