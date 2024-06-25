from pathlib import Path
import bfm.file_handler as fm
from bfm.common import Args
from alive_progress import alive_bar
from time import sleep

def start_migration(args: Args) -> list[Path] | None:
    id_list = args.txt or args.raw
    failed = []
    files_to_move = fm.get_files_to_move(args.source, args.prefix, id_list)
    
    if not files_to_move:
        print("NO FILES")
        return None
    
    with alive_bar((len(files_to_move))) as bar:
        for file in files_to_move:
            bar()
            move_file_result = fm.move_file(file, args.destination)
            print(move_file_result[1])
            if move_file_result[0] == False:
                failed.append(file)
            sleep(0.1) # Just so the user gets more feedback, can be removed if needed
            continue
    
    return failed if len(failed) > 0 else None