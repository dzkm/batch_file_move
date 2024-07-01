from tkinter import ttk
import bfm.gui.styles as style
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
        style='Button.Leave.TButton'
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
    
    path = tkinter.StringVar()
    
    ttk.Label(frame, text=label).pack(side=tkinter.LEFT)
    ttk.Entry(frame, textvariable=path).pack(side=tkinter.LEFT)
    ttk.Button(frame, text="Selecionar", command=lambda: print("...")).pack(side=tkinter.LEFT, padx=10)
    return frame


def draw(root: tkinter.Tk):
    origin_folder_selector = _folder_selector(root, "Pasta de origem")
    dest_folder_selector = _folder_selector(root, "Pasta de destino")
    
    op_frame = ttk.Labelframe(root, text="Operação", labelanchor="n")
    operation_type = tkinter.IntVar()
    op_frame_radio_1 = ttk.Radiobutton(op_frame, text="Mover", value=0, variable=operation_type)
    op_frame_radio_2 = ttk.Radiobutton(op_frame, text="Copiar", value=1, variable=operation_type)
    
    list_frame = ttk.Labelframe(root, text="Tipo da Lista", labelanchor="n")
    list_type = tkinter.IntVar()
    list_frame_radio_1 = ttk.Radiobutton(list_frame, text="Arquivo de texto", value=0, variable=list_type)
    list_frame_radio_2 = ttk.Radiobutton(list_frame, text="Lista separada por virgula", value=1, variable=list_type)
    
    origin_folder_selector.pack(pady=5)
    dest_folder_selector.pack(pady=5)
    ttk.Separator(master=root, orient="horizontal").pack(fill='x', pady=15)
    op_frame_radio_1.pack()
    op_frame_radio_2.pack()
    op_frame.pack(pady=5, side=tkinter.TOP)
    list_frame_radio_1.pack()
    list_frame_radio_2.pack()
    list_frame.pack(pady=5, side=tkinter.TOP)
    _button(root, "Mover", lambda: print(list_type.get(), operation_type.get())).pack(ipady=5, fill='x')
    
    