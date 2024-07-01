from common import Args
import menu
import migration
import gui
from tkinter import messagebox

def main(args: Args):
    gui.draw_gui()
    raise SystemExit(0)
    menu_args = menu.menu(args)
    migration_result = migration.start_migration(menu_args)
    if migration_result:
        print("Migration failed for the following files:")
        for x in migration_result:
            print(x)
    messagebox.showinfo("Success", "Migration completed successfully.")