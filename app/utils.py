from tkinter import ttk


def to_uppercase(*args, text_var):
    text = text_var.get()
    text_uppercase = text.upper()
    text_var.set(text_uppercase)

def click_button(target, set_points):
    points = int(target.get())
    result = points + set_points
    target.set(result)


def create_label(parent, text):
    label = ttk.Label(parent, text=text)
    return label