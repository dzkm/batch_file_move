from tkinter import ttk
import bfm.gui.styles as style
import bfm.menu.prompt as prompt
import tkinter

def _folder_selector(root: tkinter.Tk, label: str) -> tkinter.StringVar:
    frame = ttk.Frame(root)
    
    path = tkinter.StringVar()
    
    ttk.Label(frame, text=label).pack(side=tkinter.LEFT)
    ttk.Entry(frame, textvariable=path).pack(side=tkinter.LEFT)
    ttk.Button(frame, text="Selecionar", command=lambda: path.set(prompt.ask_source())).pack(side=tkinter.LEFT, padx=10)
    frame.pack(pady=5)
    return path

def _file_selector(root: tkinter.Tk, label: str) -> tkinter.StringVar:
    frame = ttk.Frame(root)
    
    path = tkinter.StringVar()
    
    ttk.Label(frame, text=label).pack(side=tkinter.LEFT)
    ttk.Entry(frame, textvariable=path).pack(side=tkinter.LEFT)
    ttk.Button(frame, text="Selecionar", command=lambda: path.set(prompt.ask_txt_file())).pack(side=tkinter.LEFT, padx=10)
    frame.pack(pady=5)
    return path

def _prefix_input(root: tkinter.Tk) -> tkinter.StringVar:
    frame = ttk.Frame(root)
    
    prefix = tkinter.StringVar()
    
    ttk.Label(frame, text="Prefixo").pack(side=tkinter.LEFT)
    ttk.Entry(frame, textvariable=prefix).pack(side=tkinter.LEFT)
    frame.pack()
    return prefix

def _list_input(root: tkinter.Tk) -> tkinter.StringVar:
    frame = ttk.Frame(root)
    
    list = tkinter.StringVar()
    
    ttk.Label(frame, text="Lista").pack(side=tkinter.LEFT)
    ttk.Entry(frame, textvariable=list).pack(side=tkinter.LEFT)
    ttk.Button(frame, text="Selecionar", command=lambda: print("...")).pack(side=tkinter.LEFT, padx=10)
    frame.pack()
    return list

def _frame_operation_type(root: tkinter.Tk) -> tkinter.IntVar:
    labelframe = ttk.Labelframe(master=root, text="Operação", labelanchor="n")
    
    operation_type = tkinter.IntVar()
    
    ttk.Radiobutton(labelframe, text="Mover", value=0, variable=operation_type).pack(side=tkinter.LEFT)
    ttk.Radiobutton(labelframe, text="Copiar", value=1, variable=operation_type).pack(side=tkinter.LEFT)
    labelframe.pack()
    return operation_type

def _frame_input_type(root: tkinter.Tk) -> tkinter.IntVar:
    labelframe = ttk.Labelframe(master=root, text="Tipo da Lista", labelanchor="n")
    
    list_type = tkinter.IntVar()
    
    ttk.Radiobutton(labelframe, text="Arquivo de texto", value=0, variable=list_type).pack(side=tkinter.LEFT)
    ttk.Radiobutton(labelframe, text="Lista separada por virgula", value=1, variable=list_type).pack(side=tkinter.LEFT)
    labelframe.pack()
    return list_type

def draw(root: tkinter.Tk):
    origin_folder = _folder_selector(root, "Pasta de origem")
    dest_folder = _folder_selector(root, "Pasta de destino")
    ttk.Separator(master=root, orient="horizontal").pack(fill='x', pady=15)
    list_type = _frame_input_type(root)
    operation_type = _frame_operation_type(root)
    

    ttk.Button(root, text="Mover", command=lambda: print(list_type.get(), operation_type.get())).pack(ipady=5, fill='x')
    
    