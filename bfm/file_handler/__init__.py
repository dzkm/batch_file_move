from pathlib import Path
from typing import Generator
from alive_progress import alive_bar

def txt_file_parser(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        file_lines: list[str] | None = [line.strip() for line in file.readlines() if line.strip() != ""]
        if not file_lines:
            raise ValueError("File is empty.")
        return file_lines
    
def get_files_to_move(source_path: str, prefix: str, id_list: list[str]) -> set[Path] | None:
    source_path: Path = Path(source_path)
    id_set = set(id_list)
    found_ids = set()
    files_got = set()
    
    for file in source_path.glob("%s*" % prefix):
        if not file.is_file():
            continue
        
        file_id = file.stem[len(prefix):]
        if file_id in id_set:
            found_ids.add(file_id)
            files_got.add(file)
    
    [print("O id %s não foi encontrado" % id) for id in id_set if id not in found_ids]
    return files_got if len(files_got) > 0 else None
        

def move_file(file: Path, destination: str) -> list[bool, str]:
    destination = Path(destination)
    try:
        file.rename(destination / file.name)
        return [True, "Moved %s to %s/" % (file.name, destination)]
    except FileExistsError as e:
        return [False, "File %s already exists in %s" % (file.name, destination)]
    except Exception as e:
        return [False, "Unknown error on file %s" % (file.name)]