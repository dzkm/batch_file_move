from bfm.common import Args
from bfm.menu import prompt
from bfm.file_handler import txt_file_parser
from bfm.gui import show_error_dialog
from types import FunctionType
from bfm.common import LIST_TYPE

def _call_if_none(arg: any, func: FunctionType, *fargs: any):
    if not arg:
        return func(*fargs)
    return arg 

def menu(args: Args):
    finished = False
    
    while(not finished):
        try:
            args.source = _call_if_none(args.source, prompt.ask_source)
            args.destination = _call_if_none(args.destination, prompt.ask_destination)
            
            if(args.source == args.destination):
                show_error_dialog("Source and destination cannot be the same.")
                args.destination = None
            
            args.prefix = _call_if_none(args.prefix, prompt.ask_prefix)
            kind_list = prompt.ask_kind_list()
            
            if kind_list == LIST_TYPE.TXT_FILE.value[0]:
                args.txt = txt_file_parser(_call_if_none(args.txt, prompt.ask_txt_file))
            elif kind_list == LIST_TYPE.INPUT.value[0]:
                args.raw = _call_if_none(args.raw, prompt.ask_raw_list)

            finished = True
            print(args)
        except Exception as e:
            show_error_dialog(msg = e)
            continue    