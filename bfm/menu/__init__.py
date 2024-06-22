from bfm.common import Args
from bfm.menu import prompt
from bfm.file_handler import txt_file_parser
from types import FunctionType

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
            args.prefix = _call_if_none(args.prefix, prompt.ask_prefix)
            kind_list = prompt.ask_kind_list()
            
            if kind_list == 0:
                args.txt = txt_file_parser(_call_if_none(args.txt, prompt.ask_txt_file))
            elif kind_list == 1:
                args.raw = _call_if_none(args.raw, prompt.ask_raw_list)
 
            finished = True
            print(args)
        except Exception as e:
            print(e)
            continue    