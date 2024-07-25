import FreeSimpleGUI as sg
import os
from common import Args
import args_validator as av

USER_HOME_PATH = os.path.expanduser("~")

input_folder_selector_frame = [
    [sg.Text("Pasta de origem")],
    [sg.Input(key="INPUT_FOLDER", change_submits=True)],
    [
        sg.FolderBrowse(
            button_text="Procurar",
            initial_folder=USER_HOME_PATH,
            key="BROWSE_INPUT_FOLDER",
            enable_events=True,
        )
    ],
    [
        sg.pin(
            sg.Text(
                "Pasta de origem inválida",
                key="ERROR_INVALID_INPUT_FOLDER",
                visible=False,
                text_color="red",
            )
        )
    ],
]

output_folder_selector_frame = [
    [sg.Text("Pasta de destino")],
    [sg.Input(key="OUTPUT_FOLDER", enable_events=True)],
    [
        sg.FolderBrowse(
            button_text="Procurar",
            initial_folder=USER_HOME_PATH,
            key="BROWSE_OUTPUT_FOLDER",
            enable_events=True,
        )
    ],
    [
        sg.pin(
            sg.Text(
                "Pasta de destino inválida",
                key="ERROR_INVALID_OUTPUT_FOLDER",
                visible=False,
                text_color="red",
            )
        )
    ],
]

text_file_input_frame = [
    sg.pin(
        sg.Column(
            [
                [sg.Text("Arquivo de texto")],
                [sg.Input(key="TXT_INPUT", enable_events=True)],
                [
                    sg.FileBrowse(
                        button_text="Procurar",
                        file_types=(("Text Files", "*.txt"),),
                        initial_folder=USER_HOME_PATH,
                        key="BROWSER_INPUT_TXT",
                        enable_events=True,
                    )
                ],
                [
                    sg.pin(
                        sg.Text(
                            "Arquivo inválido",
                            key="ERROR_INVALID_INPUT_TXT",
                            visible=False,
                            text_color="red",
                        )
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
                [sg.Text("Exemplo: 1,2,3")],
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
        ),
        sg.Radio(
            "Lista separada por virgula",
            "INPUT_TYPE",
            enable_events=True,
            key="INPUT_TYPE_COMMA",
        ),
    ],
]

prefix_input_frame = [[sg.Text("Prefixo")], [sg.Input()]]

op_type_frame = [
    [
        sg.Radio(
            "Mover", "OP_TYPE", default=True, enable_events=True, key="OP_TYPE_MOVE"
        ),
        sg.Radio("Copiar", "OP_TYPE", enable_events=True, key="OP_TYPE_COPY"),
    ],
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
    [sg.Button("OK"), sg.Button("Sair")],
]

window = sg.Window("Batch File Mode", layout, disable_close=True)


def draw():
    while True:
        event, values = window.read(timeout=1000)
        if event == sg.WINDOW_CLOSED:
            window.close()
            exit()
        if event == "Sair":
            result = sg.popup_yes_no(
                "Deseja realmente sair?", title="Sair", keep_on_top=True
            )
            if result == "Yes":
                window.close()
                exit()
            continue

        if event == "__TIMEOUT__":
            if values["INPUT_FOLDER"] != "":
                window["ERROR_INVALID_INPUT_FOLDER"].update(
                    visible=not os.path.isdir(values["INPUT_FOLDER"])
                )
            if values["OUTPUT_FOLDER"] != "":
                window["ERROR_INVALID_OUTPUT_FOLDER"].update(
                    visible=not os.path.isdir(values["OUTPUT_FOLDER"])
                )
            if values["TXT_INPUT"] != "":
                window["ERROR_INVALID_INPUT_TXT"].update(
                    visible=not os.path.isfile(values["TXT_INPUT"])
                )

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
            if values["BROWSE_OUTPUT_FOLDER"] == values["INPUT_FOLDER"]:
                sg.popup_ok(
                    "Pasta de origem e destino não podem ser iguais.",
                    title="Erro",
                )
                continue
            window["OUTPUT_FOLDER"].update(value=values["BROWSE_OUTPUT_FOLDER"])
        if event == "BROWSER_INPUT_TXT":
            window["TXT_INPUT"].update(value=values["BROWSER_INPUT_TXT"])

        if event == "OK":
            args = Args(
                copy=values["OP_TYPE_COPY"],
                source=values["INPUT_FOLDER"],
                destination=values["OUTPUT_FOLDER"],
                prefix=values[0],
                txt=values["TXT_INPUT"],
                raw=values["COMMA_LIST_INPUT"].strip().split(","),
            )
            try:
                av.validate_all(args)
            except ValueError as e:
                sg.popup_ok(str(e), title="Erro")
                continue

            return args
