def txt_file_parser(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        file_lines: list[str] | None = [line.strip() for line in file.readlines() if line.strip() != ""]
        if not file_lines:
            raise ValueError("File is empty.")
        return file_lines  