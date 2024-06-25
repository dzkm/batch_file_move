from common import Args
import menu
import migration
from tkinter import messagebox

def main(args: Args):
    menu_args = menu.menu(args)
    migration_result = migration.start_migration(menu_args)
    if migration_result:
        print("Migration failed for the following files:")
        for x in migration_result:
            print(x)
    messagebox.showinfo("Success", "Migration completed successfully.")