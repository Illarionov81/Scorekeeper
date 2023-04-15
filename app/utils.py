from pathlib import Path
from tkinter import PhotoImage


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


def change_flag(width, flag, flag_path):
    rate = 1
    if width <= 650:
        rate = 3
    if 650 < width <= 1150:
        rate = 2

    flag_img = PhotoImage(file=flag_path)
    flag_img = flag_img.subsample(rate)
    flag.config(image=flag_img, anchor="center")
    return flag_img
