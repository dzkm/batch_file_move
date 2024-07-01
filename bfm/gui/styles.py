import tkinter
from tkinter import ttk

CATPPUCCIN_ACCENT = '#cba6f7'
CATPPUCCIN_TEXT = '#cdd6f4'
CATPPUCCIN_SUBTEXT = '#bac2de'
CATPPUCCIN_SURFACE = '#313244'
CATPPUCCIN_BASE = '#1e1e2e'
CATPPUCCIN_MANTLE = '#181825'

def load_styles(root: tkinter.Tk):
    style = ttk.Style(root)
    style.theme_use('clam')
    style.configure('TFrame', background=CATPPUCCIN_MANTLE)
    
    style.configure('Main.TFrame', background=CATPPUCCIN_BASE, padding=10, relief='flat')
    
    style.configure('ButtonFrame.TFrame', background=CATPPUCCIN_BASE, padding=30, relief='flat')
    
    style.configure('Button.Static.TButton', background=CATPPUCCIN_ACCENT, foreground=CATPPUCCIN_TEXT, padding=1, relief='flat')
    style.configure('Button.Hover.TButton', background=CATPPUCCIN_MANTLE, foreground=CATPPUCCIN_SUBTEXT, padding=1, relief='flat')
    
    style.configure('Label.TLabel', foreground=CATPPUCCIN_SUBTEXT, background=CATPPUCCIN_BASE, padding=3, relief='flat')
    
    style.configure('Entry.TEntry', foreground=CATPPUCCIN_TEXT, background=CATPPUCCIN_SURFACE, padding=3, relief='flat')
    
    
    style.configure('Labelframe.TLabelframe', background=CATPPUCCIN_BASE, foreground=CATPPUCCIN_TEXT, padding=10, relief='flat')
    style.configure('Labelframe.TLabelframe.Label', foreground=CATPPUCCIN_TEXT, background=CATPPUCCIN_BASE, padding=3, relief='flat')
    style.configure('Labelframe.TLabelframe.TRadioButton', foreground=CATPPUCCIN_TEXT, background=CATPPUCCIN_BASE, padding=3, relief='flat')
    
    style.configure('Radio.Inactive.TRadiobutton', foreground=CATPPUCCIN_SURFACE, padding=3, relief='flat')
        
    style.configure('Radio.Active.TRadiobutton', foreground=CATPPUCCIN_ACCENT, padding=3, relief='flat')