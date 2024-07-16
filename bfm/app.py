from common import Args
import gui
import migration
import args_validator as av
import FreeSimpleGUI as sg

IS_GUI_MODE = True


def main(args: Args) -> int:
    global IS_GUI_MODE

    # Checks if any argument has been passed to the program.
    for key, value in vars(args).items():
        if value:
            IS_GUI_MODE = False  # If any argument, disable GUI and makes user use CLI.
            break

    if IS_GUI_MODE:
        args = gui.draw()
    if not IS_GUI_MODE:
        try:
            av.validate_all(args)
        except ValueError as e:
            print(str(e))
            return 1

    migration_result = migration.start_migration(args, IS_GUI_MODE)
    if migration_result is True:
        if IS_GUI_MODE:
            sg.popup_ok(
                "Migração concluída com sucesso.",
                title="Migração",
            )
        print("Migration completed successfully.")
        return 0

    if type(migration_result) is list:
        print("Migration failed for the following files:")
        for x in migration_result:
            print(x)

    if IS_GUI_MODE:
        sg.popup_ok(
            "Houve erros durante a migração. Verifique o console para mais informações.",
            title="Migração",
        )
    return 1
