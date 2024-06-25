from pathlib import Path
import bfm.file_handler as fm
from bfm.common import Args

def start_migration(args: Args) -> list[Path] | None:
    id_list = args.txt or args.raw
    failed = []
    
    for file in fm.get_files_to_move(args.source, args.prefix, id_list):
        move_file_result = fm.move_file(file, args.destination)
        if not move_file_result[0]:
            failed.append(file)
        continue
    
    return failed if len(failed) > 0 else None