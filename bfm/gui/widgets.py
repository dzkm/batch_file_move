from tkinter import ttk
import bfm.menu.prompt as prompt
import tkinter


def _folder_selector(
    root: ttk.Widget | tkinter.Frame | tkinter.Tk, label: str
) -> tuple[ttk.Frame, tkinter.StringVar]:
    frame = ttk.Frame(root)

    path = tkinter.StringVar()

    ttk.Label(frame, text=label).pack(side=tkinter.LEFT)
    ttk.Entry(frame, textvariable=path).pack(side=tkinter.LEFT, fill=tkinter.X)
    ttk.Button(
        frame, text="Selecionar", command=lambda: path.set(prompt.ask_source())
    ).pack(side=tkinter.LEFT, padx=10)
    frame.pack(pady=5)
    return (frame, path)


def _file_selector(root: ttk.Widget, label: str) -> tuple[ttk.Frame, tkinter.StringVar]:
    frame = ttk.Frame(root)

    path = tkinter.StringVar()

    ttk.Label(frame, text=label).pack(side=tkinter.LEFT)
    ttk.Entry(frame, textvariable=path).pack(side=tkinter.LEFT)
    ttk.Button(
        frame, text="Selecionar", command=lambda: path.set(prompt.ask_txt_file())
    ).pack(side=tkinter.LEFT, padx=10)
    frame.pack(pady=5)
    return (frame, path)


def _prefix_input(root: tkinter.Tk | ttk.Widget) -> tkinter.StringVar:
    frame = ttk.Frame(root)

    prefix = tkinter.StringVar()

    ttk.Label(frame, text="Prefixo").pack(side=tkinter.LEFT)
    ttk.Entry(frame, textvariable=prefix).pack(side=tkinter.RIGHT, fill=tkinter.X)
    frame.pack()
    return prefix


def _list_input(root: ttk.Widget) -> tuple[ttk.Frame, tkinter.StringVar]:
    frame = ttk.Frame(root)

    list_input = tkinter.StringVar()

    ttk.Label(frame, text="Lista").pack(side=tkinter.LEFT)
    ttk.Entry(frame, textvariable=list_input).pack(side=tkinter.LEFT, fill=tkinter.X)
    frame.pack()
    return (frame, list_input)


def _frame_operation_type(root: tkinter.Tk | ttk.Frame) -> tkinter.IntVar:
    labelframe = ttk.Labelframe(master=root, text="Operação", labelanchor="n")

    operation_type = tkinter.IntVar()

    ttk.Radiobutton(labelframe, text="Mover", value=0, variable=operation_type).pack(
        side=tkinter.LEFT
    )
    ttk.Radiobutton(labelframe, text="Copiar", value=1, variable=operation_type).pack(
        side=tkinter.LEFT
    )
    labelframe.pack()
    return operation_type


def __frame_input_type_change_type(
    value: tkinter.IntVar,
    file_selector_widget: ttk.Widget,
    list_input_widget: ttk.Widget,
):
    if value.get() == 0:
        file_selector_widget.pack(pady=5, side=tkinter.TOP)
        list_input_widget.pack_forget()
    elif value.get() == 1:
        file_selector_widget.pack_forget()
        list_input_widget.pack(pady=5, side=tkinter.TOP)


def _frame_input_type(
    root: tkinter.Tk | ttk.Frame,
) -> tuple[tkinter.IntVar, tkinter.StringVar, tkinter.StringVar]:
    labelframe = ttk.Labelframe(master=root, text="Tipo da Lista", labelanchor="n")
    input_frame = ttk.Frame(master=root)

    file_selector_frame, file_selector_value = _file_selector(
        input_frame, "Arquivo de texto"
    )
    comma_separated_frame, comma_separated_value = _list_input(input_frame)

    file_selector_frame.pack(pady=5, side=tkinter.TOP)
    comma_separated_frame.pack_forget()

    list_type = tkinter.IntVar()

    ttk.Radiobutton(
        labelframe,
        text="Arquivo de texto",
        value=0,
        variable=list_type,
        command=lambda: __frame_input_type_change_type(
            list_type, file_selector_frame, comma_separated_frame
        ),
    ).pack(side=tkinter.LEFT)
    ttk.Radiobutton(
        labelframe,
        text="Lista separada por virgula",
        value=1,
        variable=list_type,
        command=lambda: __frame_input_type_change_type(
            list_type, file_selector_frame, comma_separated_frame
        ),
    ).pack(side=tkinter.LEFT)
    labelframe.pack()
    input_frame.pack()
    return (list_type, file_selector_value, comma_separated_value)


def draw(root: tkinter.Tk):
    origin_folder = _folder_selector(root, "Pasta de origem").pack()
    dest_folder = _folder_selector(root, "Pasta de destino").pack()
    ttk.Separator(master=root, orient="horizontal").pack(fill="x", pady=15)
    list_type = _frame_input_type(root)
    operation_type = _frame_operation_type(root)

    ttk.Button(
        root, text="Mover", command=lambda: print(list_type.get(), operation_type.get())
    ).pack(ipady=5, fill="x")
