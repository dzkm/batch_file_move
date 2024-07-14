from common import Args
import gui
import migration
from tkinter import messagebox

IS_GUI_MODE = True


def main(args: Args):
    global IS_GUI_MODE

    for key, value in vars(args).items():
        if value is not None:
            IS_GUI_MODE = False
            break

    if IS_GUI_MODE:
        args = gui.draw()

    raise SystemExit(0)
    menu_args = menu.menu(args)
    migration_result = migration.start_migration(menu_args)
    if migration_result:
        print("Migration failed for the following files:")
        for x in migration_result:
            print(x)
    messagebox.showinfo("Success", "Migration completed successfully.")
