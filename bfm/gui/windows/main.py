from bfm.gui import widgets, containers
import tkinter
from tkinter import ttk


def draw():
    window = tkinter.Tk()
    window.title("Batch File Move")
    window.resizable(False, False)

    frame: ttk.Frame = containers._main(window)

    folder_frame, folder_value = widgets._folder_selector(frame, "Pasta")
    prefix = widgets._prefix_input(frame)
    operation_type = widgets._frame_operation_type(frame)
    input_type, text_file, id_list = widgets._frame_input_type(frame)

    ttk.Button(frame, text="Executar", command=lambda: print("...")).pack(
        fill=tkinter.X, ipady=10
    )
    frame.pack()

    window.update_idletasks()
    window.minsize(window.winfo_width(), window.winfo_height())
    return window
