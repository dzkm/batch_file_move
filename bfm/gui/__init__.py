import tkinter
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from bfm.common import LIST_TYPE

_root = tkinter.Tk()
_root.withdraw()

def _close_when_empty(response: any) -> any:
    if(isinstance(response, tuple) and response):
        return response
    
    if(isinstance(response, str) and response.strip() != ""):
        return response
    
    if(response):
        return response
    
    if messagebox.askokcancel("Quit", "You canceled your operation. Do you want to quit?"):
        _root.destroy()
        raise SystemExit(0)
    return False

def openfiledialog(**kwargs) -> str | bool: 
    return _close_when_empty(filedialog.askopenfilename(**kwargs))

def openfolderdialog(**kwargs) -> str:
    return _close_when_empty(filedialog.askdirectory(**kwargs))

def ask_prefix() -> str | None:
    return simpledialog.askstring("Prefix", "Enter prefix:", parent=_root)

def ask_kind_list() -> int:
    prompt = "What kind of list is it?"
    for kind in LIST_TYPE:
        prompt += f"\n{kind.value[0]}: {kind.value[1]}"
    return _close_when_empty(simpledialog.askinteger("Type of list", prompt, parent=_root, minvalue=1, maxvalue=999))

def ask_raw_input() -> str:
    return _close_when_empty(simpledialog.askstring("Raw input", "Enter raw input:", parent=_root))

def show_error_dialog(title: str = "Error", msg: str = "An error has occurred") -> None:
    messagebox.showerror(title, msg)