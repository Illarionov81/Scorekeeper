from tkinter import *
from pathlib import Path


def to_uppercase(*args, text_var):
    text = text_var.get()
    text_uppercase = text.upper()
    text_var.set(text_uppercase)


def click_button(target, set_points):
    points = int(target.get())
    result = points + set_points
    target.set(result)


def get_all_country():
    root_path = Path(__file__).parent.parent
    flags_folder = root_path / 'img' / 'flags-iso'
    names = []
    for file_path in flags_folder.iterdir():
        if file_path.is_file():
            names.append(file_path.name)
    return names
