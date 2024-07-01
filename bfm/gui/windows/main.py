from bfm.gui import widgets, containers
import tkinter
from tkinter import ttk

def draw():
    window = tkinter.Tk()
    window.title("Batch File Move")
    window.resizable(False, False)
    
    
    frame = containers._main(window)
    
    folder = widgets._folder_selector(frame, "Pasta")
    file = widgets._file_selector(frame, "Arquivo")
    prefix = widgets._prefix_input(frame)
    operation_type = widgets._frame_operation_type(frame)
    
        
    
    input_type = widgets._frame_input_type(frame)
    if(input_type.get() == 0):
        input_list = widgets._file_selector(frame, "Arquivo")
    else:
        input_list = widgets._list_input(frame)
    
    ttk.Button(frame, text="Executar", command=lambda: print("...")).pack(fill=tkinter.X, ipady=10)
    frame.pack()
    
    window.update_idletasks()
    window.minsize(
        window.winfo_width(),
        window.winfo_height()
    )
    return window