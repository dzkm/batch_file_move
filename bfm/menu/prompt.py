from bfm.common import LIST_TYPE
import bfm.gui as gui

def ask_source() -> str:
    source = gui.openfolderdialog(title="Select source folder")
    if source:
        return source
    raise ValueError("Source file is invalid.")

def ask_destination() -> str | bool:
    destination = gui.openfolderdialog(title="Select destination folder")
    if destination:
        return destination
    raise ValueError("Destination file is invalid.")

def ask_prefix() -> str | bool:
    prefix = gui.ask_prefix()
    if prefix:
        return prefix
    raise ValueError("Prefix is invalid.")

def ask_kind_list() -> int | bool:
    kind_list = gui.ask_kind_list()
    
    list_type_enum = set([x.value[0] for x in LIST_TYPE]) # Hack. Python 3.12 has Enum.__contains__, which allows for for-loops directly
    
    if kind_list in list_type_enum:
        return kind_list
    raise ValueError("The list kind is invalid.")

def ask_raw_list() -> list[str] | bool:
    raw_list = gui.ask_raw_input()
    
    if raw_list.strip().length > 0:
        split_list = raw_list.split(",")
        if(split_list.count > 0):
            return [x.strip() for x in split_list]
    
    raise ValueError("Invalid raw list. Please check your list again")

def ask_txt_file() -> str | bool:
    txt_file = gui.openfiledialog(title="Select txt file", filetypes=[("Text files", "*.txt")])
    if txt_file:
        return txt_file
    
    raise ValueError("Invalid txt file. Please check your file again.")