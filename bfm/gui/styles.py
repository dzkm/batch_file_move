import tkinter
from tkinter import ttk

CATPPUCCIN_ACCENT = "#cba6f7"
CATPPUCCIN_TEXT = "#cdd6f4"
CATPPUCCIN_SUBTEXT = "#bac2de"
CATPPUCCIN_SURFACE = "#313244"
CATPPUCCIN_BASE = "#1e1e2e"
CATPPUCCIN_MANTLE = "#181825"


def load_styles(root: tkinter.Tk):
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("TFrame", background=CATPPUCCIN_BASE)

    style.configure("Main.TFrame", background=CATPPUCCIN_BASE, padding=10, relief="flat")

    style.configure(
        "TLabel",
        foreground=CATPPUCCIN_SUBTEXT,
        background=CATPPUCCIN_BASE,
        padding=3,
        relief="flat",
    )
    style.configure("TButton", 
                    padding=3, 
                    relief="flat", 
                    foreground=CATPPUCCIN_TEXT, 
                    background=CATPPUCCIN_MANTLE
                    )
    style.map(
        "TButton",
        foreground=[
            ("pressed", CATPPUCCIN_TEXT), 
            ("active", CATPPUCCIN_ACCENT),
        ],
        background=[
            ("pressed", "!disabled", CATPPUCCIN_ACCENT),
            ("active", CATPPUCCIN_SURFACE),
        ],
    )
    style.configure(
        "TRadiobutton",
        foreground=CATPPUCCIN_SUBTEXT,
        background=CATPPUCCIN_BASE,
        padding=3,
        relief="flat",
        indicatorbackground=CATPPUCCIN_MANTLE,
        indicatorforeground=CATPPUCCIN_ACCENT,
    )
    style.map(
        "TRadiobutton",
        foreground=[
            ("pressed", CATPPUCCIN_TEXT),
            ("active", CATPPUCCIN_ACCENT),
        ],
        background=[
            ("pressed", "!disabled", CATPPUCCIN_ACCENT),
            ("active", CATPPUCCIN_SURFACE),
        ],)
    style.configure(
        "TLabelframe",
        background=CATPPUCCIN_BASE,
        foreground=CATPPUCCIN_TEXT,
        relief="flat",
        highlightforeground=CATPPUCCIN_ACCENT,
        highlightbackground=CATPPUCCIN_MANTLE,
        padding=10, 
    )
    style.configure(
        "TLabelframe.Label",
        background=CATPPUCCIN_BASE,
        foreground=CATPPUCCIN_TEXT,
        relief="flat",
        font=("Helvetica", 12, "bold"),
    )
