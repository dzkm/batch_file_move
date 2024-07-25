from pathlib import Path
import os

import bfm.file_handler as fm
from bfm.common import Args
import FreeSimpleGUI as sg


def migrate_file(file: Path, destination: str, copy: bool = False) -> bool:
    if copy:
        status, message = fm.copy_file(file, destination)
    else:
        status, message = fm.move_file(file, destination)
    print(message)
    return status


def cli_migration(
    files_to_move: set[Path], destination: str, copy: bool = False
) -> tuple[list[str], list[str]]:
    success_list: list[str] = []
    failed_list: list[str] = []
    for file in files_to_move:
        if fm.file_already_exists(destination + "/" + file.name):
            answer = input(
                "File %s already exists in destination, override? (Y/n): " % file.name
            )
            if answer.lower() != "y":
                print("Skipping file %s" % file.name)
                failed_list.append(file.name)
                continue
        migration_success = migrate_file(file, destination, copy)
        if migration_success:
            success_list.append(file.name)
            continue
        failed_list.append(file.name)
    return success_list, failed_list


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
        ],
    )

    progressbar = window["progress"]

    success_list = []
    failed_list = []
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
        if fm.file_already_exists(destination + "/" + file.name):
            answer = sg.popup_yes_no(
                "O arquivo %s já existe no destino, deseja sobrescrever?" % file.name,
                title="Arquivo já existe",
            )
            if answer == "no":
                failed_list.append(file.name)
                continue
        migration_success = migrate_file(file, destination, copy)
        if migration_success:
            success_list.append(file.name)
            continue
        failed_list.append(file.name)
    return success_list, failed_list


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
        migration_results = cli_migration(files_to_move, args.destination, args.copy)
        return migration_results[1] if len(migration_results[1]) > 0 else True

    migration_results = gui_migration(files_to_move, args.destination, args.copy)
    return migration_results[1] if len(migration_results[1]) > 0 else True
