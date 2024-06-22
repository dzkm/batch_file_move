from bfm.common import LIST_TYPE

def ask_source() -> str:
    source = input("Enter source file: ")
    if source:
        return source
    raise ValueError("Source file is invalid.")

def ask_destination() -> str | bool:
    destination = input("Enter destination file: ")
    if destination:
        return destination
    raise ValueError("Destination file is invalid.")

def ask_prefix() -> str | bool:
    prefix = input("Enter prefix: ")
    if prefix:
        return prefix
    raise ValueError("Prefix is invalid.")

def ask_kind_list() -> int | bool:
    print("What kind of list is it?")
    
    for kind in LIST_TYPE:
        print(f"{kind.value[0]}: {kind.value[1]}")
    kind_list = input("Enter the kind ID: ")
    
    if not kind_list.isnumeric():
        raise TypeError("Please, insert number")
    
    kind_list = int(kind_list.strip())
    
    list_type_enum = set([x.value[0] for x in LIST_TYPE]) # Hack. Python 3.12 has Enum.__contains__
    
    if kind_list in list_type_enum:
        return kind_list
    raise ValueError("The list kind is invalid.")

def ask_raw_list() -> list[str] | bool:
    raw_list = input("Enter raw list separated by commas: ")
    
    if raw_list.strip().length > 0:
        split_list = raw_list.split(",")
        if(split_list.count > 0):
            return [x.strip() for x in split_list]
    
    raise ValueError("Invalid raw list. Please check your list again")

def ask_txt_file() -> str | bool:
    txt_file = input("Enter txt file: ")
    if txt_file:
        return txt_file
    
    raise ValueError("Invalid txt file. Please check your file again.")