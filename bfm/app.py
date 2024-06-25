from common import Args
import menu
import migration

def main(args: Args):
    menu_args = menu.menu(args)
    print(migration.start_migration(args))