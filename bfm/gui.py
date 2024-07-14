import FreeSimpleGUI as sg
import os

USER_HOME_PATH = os.path.expanduser("~")

input_folder_selector_frame = [
    [sg.Text("Pasta de origem")],
    [sg.Input(key="INPUT_FOLDER")],
    [
        sg.FolderBrowse(
            button_text="Procurar",
            initial_folder=USER_HOME_PATH,
            key="BROWSE_INPUT_FOLDER",
            enable_events=True,
        )
    ],
]

output_folder_selector_frame = [
    [sg.Text("Pasta de destino")],
    [
        sg.Input(
            key="OUTPUT_FOLDER",
        )
    ],
    [
        sg.FolderBrowse(
            button_text="Procurar",
            initial_folder=USER_HOME_PATH,
            key="BROWSE_OUTPUT_FOLDER",
            enable_events=True,
        )
    ],
]

text_file_input_frame = [
    sg.pin(
        sg.Column(
            [
                [sg.Text("Arquivo de texto")],
                [sg.Input(key="TXT_INPUT")],
                [
                    sg.FileBrowse(
                        file_types=(("Text Files", "*.txt"),),
                        initial_folder=USER_HOME_PATH,
                        key="BROWSER_INPUT_TXT",
                        enable_events=True,
                    )
                ],
            ],
            key="TXT_INPUT_FRAME",
            visible=True,
        )
    )
]

comma_list_input_frame = [
    sg.pin(
        sg.Column(
            [
                [sg.Text("Lista separada por virgula")],
                [sg.Input(key="COMMA_LIST_INPUT")],
            ],
            key="COMMA_INPUT_FRAME",
            visible=False,
        )
    )
]

input_type_frame = [
    [
        sg.Radio(
            "Arquivo de texto",
            "INPUT_TYPE",
            default=True,
            enable_events=True,
            key="INPUT_TYPE_TXT",
        )
    ],
    [
        sg.Radio(
            "Lista separada por virgula",
            "INPUT_TYPE",
            enable_events=True,
            key="INPUT_TYPE_COMMA",
        )
    ],
]

prefix_input_frame = [[sg.Text("Prefixo")], [sg.Input()]]

op_type_frame = [
    [
        sg.Radio(
            "Mover", "OP_TYPE", default=True, enable_events=True, key="OP_TYPE_MOVE"
        )
    ],
    [sg.Radio("Copiar", "OP_TYPE", enable_events=True, key="OP_TYPE_COPY")],
]

layout = [
    [
        sg.Frame(
            "Localizações",
            [
                [sg.Column(input_folder_selector_frame)],
                [sg.Column(output_folder_selector_frame)],
            ],
        )
    ],
    prefix_input_frame,
    [sg.Frame("Tipo de Operação", op_type_frame)],
    [sg.Frame("Tipo de Entrada", input_type_frame)],
    text_file_input_frame,
    comma_list_input_frame,
    [sg.Button("OK")],
]

window = sg.Window("Window Title", layout)


def draw():
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == "INPUT_TYPE_TXT":
            window["COMMA_LIST_INPUT"].update(value="")
            window["TXT_INPUT_FRAME"].update(visible=True)
            window["COMMA_INPUT_FRAME"].update(visible=False)
        elif event == "INPUT_TYPE_COMMA":
            window["TXT_INPUT"].update(value="")
            window["TXT_INPUT_FRAME"].update(visible=False)
            window["COMMA_INPUT_FRAME"].update(visible=True)

        if event == "BROWSE_INPUT_FOLDER":
            window["INPUT_FOLDER"].update(value=values["BROWSE_INPUT_FOLDER"])
        if event == "BROWSE_OUTPUT_FOLDER":
            window["OUTPUT_FOLDER"].update(value=values["BROWSE_OUTPUT_FOLDER"])
        if event == "BROWSER_INPUT_TXT":
            window["TXT_INPUT"].update(value=values["BROWSER_INPUT_TXT"])

        print("\nEvent: %s\nValues:%s" % (event, values))
