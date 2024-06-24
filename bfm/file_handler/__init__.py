from pathlib import Path
from typing import Generator
def txt_file_parser(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        file_lines: list[str] | None = [line.strip() for line in file.readlines() if line.strip() != ""]
        if not file_lines:
            raise ValueError("File is empty.")
        return file_lines
    
def file_to_move_generator(source_path: str, prefix: str, id_list: list[str]) -> Generator[str, None, None]:
    source_path: Path = Path(source_path)
    id_set = set(id_list)
    
    for file in source_path.glob("%s*" % prefix):
        if not file.is_file():
            print(f"{file.name} is not a file. Skipping.")
            continue
        
        file_id = file.stem[len(prefix):]
        if file_id in id_set:
            yield str(file)

def move_file(file: Path, destination: str) -> dict[str, bool]:
    destination = Path(destination)
    try:
        file.rename(destination / file.name)
        print(f"Moved {file.name} to {destination}")
        return {"success": True, "message": "Moved %s to %s" % (file.name, destination)}
    except FileExistsError as e:
        return {"success": False, "message": f"File {file.name} already exists in {destination}"}