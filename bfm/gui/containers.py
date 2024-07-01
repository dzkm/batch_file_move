import tkinter
from tkinter import ttk
from . import styles

def _main(root: tkinter.Tk)-> ttk.Frame:
    container = ttk.Frame(
        root, 
        style="Main.TFrame",
        )
    container.pack()
    return container