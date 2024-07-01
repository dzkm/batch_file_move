from tkinter import ttk
import tkinter

def example_lable(root: tkinter.Tk, **kwargs):
    label = ttk.Label(
        root, 
        text="Hello, World!",
        style="Label.TLabel")

def _button(root: tkinter.Tk, text: str, command: callable, **kwargs) -> ttk.Button:
    button = ttk.Button(
        root,
        text=text,
        command=command,
        style='Button.Static.TButton'
    )
    return button

def _label(root: tkinter.Tk, text: str, **kwargs) -> ttk.Label:
    label = ttk.Label(
        root, 
        text=text,
        style="Label.TLabel")
    return label

def _textbox(root: tkinter.Tk, **kwargs) -> ttk.Entry:
    textbox = ttk.Entry(
        root,
        style='Entry.TEntry'
    )
    return textbox

def _folder_selector(root: tkinter.Tk, label: str) -> ttk.Frame:
    frame = ttk.Frame(root)
    _label(frame, label).pack(side=tkinter.LEFT)
    _textbox(frame).pack(side=tkinter.LEFT)
    button = _button(frame, "...", lambda: print("..."))
    button.bind("<Enter>", lambda e: button.config(style='Button.Hover.TButton', cursor="hand2"))
    button.bind("<Leave>", lambda e: button.config(style='Button.Static.TButton', cursor="arrow"))
    button.pack(side=tkinter.RIGHT, padx=5)
    return frame


def draw(root: tkinter.Tk):
    origin_folder_selector = _folder_selector(root, "Pasta de origem")
    dest_folder_selector = _folder_selector(root, "Pasta de destino")
    
    op_frame = ttk.Labelframe(root, text="Operação", style="Labelframe.TLabelframe")
    operation_type = tkinter.IntVar()
    op_frame_radio_1 = ttk.Radiobutton(op_frame, text="Mover", value=0, variable=operation_type)
    op_frame_radio_2 = ttk.Radiobutton(op_frame, text="Copiar", value=1, variable=operation_type)
    
    list_frame = ttk.Labelframe(root, text="Tipo da Lista", style="Labelframe.TLabelframe")
    list_type = tkinter.IntVar()
    list_frame_radio_1 = ttk.Radiobutton(list_frame, text="Arquivo de texto", value=0, variable=list_type)
    list_frame_radio_2 = ttk.Radiobutton(list_frame, text="Lista separada por virgula", value=1, variable=list_type)
    
    origin_folder_selector.pack(pady=5)
    dest_folder_selector.pack(pady=5)
    ttk.Separator(master=root, orient="horizontal").pack(fill='x', pady=15)
    op_frame_radio_1.pack()
    op_frame_radio_2.pack()
    op_frame.pack(pady=5, fill='x')
    list_frame_radio_1.pack()
    list_frame_radio_2.pack()
    list_frame.pack(pady=5, fill='x')
    _button(root, "Mover", lambda: print("Mover")).pack(ipady=5, fill='x')
    
    