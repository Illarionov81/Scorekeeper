from pathlib import Path
from tkinter import ttk, Frame, StringVar

import config
from utils import get_all_country


class Sportsman:
    def __init__(
            self,
            main,
            bg,
            border_color,
            name,
            surname,
            club,
            fall,
            adv,
            points,
            point_style,
            label_style,
    ):
        self.main = main
        self.bg = bg
        self.border_color = border_color
        self.name = name
        self.surname = surname
        self.club = club
        self.fall = fall
        self.adv = adv
        self.points = points
        self.point_style = point_style
        self.label_style = label_style
        self.flag = None
        self.frame = Frame(self.main)
        self.create_sportsman_frame()

    def create_sportsman_frame(self):
        self.frame.configure(
            bg=self.bg,
            highlightbackground=self.border_color,
            highlightthickness=1,
            borderwidth=1,
            relief='ridge'
        )

        for r in range(2):
            self.frame.rowconfigure(index=r, weight=1)

        for c in range(6):
            self.frame.columnconfigure(index=c, weight=1)

        self.frame.columnconfigure(index=0, weight=6, uniform="sp_col")  # flag
        self.frame.columnconfigure(index=1, weight=25, uniform="sp_col")  # sportsmen name
        self.frame.columnconfigure(index=2, weight=50, uniform="sp_col")  # sportsmen surname
        self.frame.columnconfigure(index=3, weight=5, uniform="sp_col")  # fall label & adv label
        self.frame.columnconfigure(index=4, weight=5, uniform="sp_col")  # fall & adv
        self.frame.columnconfigure(index=5, weight=9, uniform="sp_col")  # points

        self.flag = ttk.Label(self.frame)
        name = ttk.Entry(self.frame, textvariable=self.name)
        surname = ttk.Entry(self.frame, textvariable=self.surname)
        club = ttk.Entry(self.frame, textvariable=self.club)
        fall = ttk.Entry(self.frame, textvariable=self.fall, font=('Roboto', 12, 'bold'), justify='center')
        adv = ttk.Entry(self.frame, textvariable=self.adv, font=('Roboto', 12, 'bold'), justify='center')
        points = ttk.Entry(self.frame, textvariable=self.points, style=self.point_style,
                           font=('Roboto', 22, 'bold'), justify='center')

        label_fall = ttk.Label(self.frame, text='fall', style=self.label_style)
        label_adv = ttk.Label(self.frame, text='adv', style=self.label_style)

        self.flag.grid(row=0, column=0, rowspan=2, sticky='nsew')
        name.grid(row=0, column=1, sticky='nsew')
        surname.grid(row=0, column=2, sticky='nsew')
        club.grid(row=1, column=1, columnspan=2, sticky='nsew')
        label_fall.grid(row=0, column=3, sticky='nsew')
        label_adv.grid(row=1, column=3, sticky='nsew')
        fall.grid(row=0, column=4, sticky='nsew')
        adv.grid(row=1, column=4, sticky='nsew')
        points.grid(row=0, column=5, rowspan=2, sticky='nsew')


class GeneralInfo:
    def __init__(self, main, title, stage_val, group_val, belt_val):
        self.main = main
        self.title = title
        self.frame = Frame(self.main)
        self.stage_val = stage_val
        self.group_val = group_val
        self.belt_val = belt_val
        self.create_general_info_frame()

    def create_general_info_frame(self):
        self.frame.configure(bg=config.CONTROL_GENERAL_BG)

        for r in range(5):
            self.frame.rowconfigure(index=r, weight=1)

        for c in range(3):
            self.frame.columnconfigure(index=c, weight=1)

        stage_choice = [
            'EIGHTH-FINALS',
            'QUARTERFINALS',
            'SEMI-FINALS',
            'FINALS',
        ]

        group_choice = [
            'Kids 1',
            'Kids 2',
            'Kids 3',
            'Infant',
            'Junior',
            'Junior',
            'Youth',
            'Amateur',
            'Professional',
            'Master 1',
            'Master 2',
        ]

        belt_choice = [
            'White',
            'Grey',
            'Yellow',
            'Orange',
            'Green',
            'Blue',
            'Purple',
            'Brown',
            'Black',
        ]

        title = ttk.Entry(self.frame, textvariable=self.title, justify='center')

        stage_label = ttk.Label(self.frame, text='Stage: ', anchor='c')
        group_label = ttk.Label(self.frame, text='Group: ', anchor='c')
        belt_label = ttk.Label(self.frame, text='Belt: ', anchor='c')

        stage = ttk.Combobox(self.frame, textvariable=self.stage_val, values=stage_choice, justify='center')
        stage.current(0)
        group = ttk.Combobox(self.frame, textvariable=self.group_val, values=group_choice, justify='center')
        group.current(0)
        belt = ttk.Combobox(self.frame, textvariable=self.belt_val, values=belt_choice, justify='center')
        belt.current(0)

        title.grid(row=0, column=0, columnspan=3, sticky='nsew')
        stage_label.grid(row=2, column=0, sticky='nsew')
        group_label.grid(row=2, column=1, sticky='nsew')
        belt_label.grid(row=2, column=2, sticky='nsew')
        stage.grid(row=3, column=0, sticky='nsew')
        group.grid(row=3, column=1, sticky='nsew')
        belt.grid(row=3, column=2, sticky='nsew')


class FlagChoice:
    def __init__(
            self,
            main,
            flag_str,
            label_text,
    ):
        self.main = main
        self.flag_str = flag_str
        self.label_text = label_text
        self.frame = Frame(self.main)
        self.flag_box = None
        self.flag_path = None
        self.flag_path_for_spectators = None
        self.root_path = Path(__file__).parent.parent

        self.create_flag_choice()

    def create_flag_choice(self):
        self.frame.configure(bg=config.CONTROL_GENERAL_BG)

        for r in range(1):
            self.frame.rowconfigure(index=r, weight=1)

        for c in range(4):
            self.frame.columnconfigure(index=c, weight=1)

        country_name = sorted(get_all_country())
        self.flag_path = self.flag_str.format(root_path=self.root_path, country="KG.png")
        self.flag_path_for_spectators = StringVar(value=self.flag_path)

        flag_label = ttk.Label(self.frame, text=self.label_text, anchor='e')
        self.flag_box = ttk.Combobox(self.frame, values=country_name)

        flag_label.grid(row=0, column=0, sticky='nsew')
        self.flag_box.grid(row=0, column=1, sticky='nsew')


class FlagChoiceFrame:
    def __init__(self, main, flag_str):
        self.main = main
        self.flag_str = flag_str
        self.frame = Frame(self.main)
        self.frame.configure(bg=config.CONTROL_GENERAL_BG)

        self.flag_choice_1 = FlagChoice(
            self.frame,
            self.flag_str,
            'sportsman 1 flag: '
        )
        self.flag_choice_2 = FlagChoice(
            self.frame,
            self.flag_str,
            'sportsman 2 flag: '
        )
        self.frame_placement()

    def frame_placement(self):
        for i in range(1):
            self.frame.grid_rowconfigure(i, weight=1)

        for i in range(2):
            self.frame.grid_columnconfigure(i, weight=1)

        self.frame.columnconfigure(index=0, weight=50, uniform="flag_row1")
        self.frame.columnconfigure(index=1, weight=50, uniform="flag_row1")

        self.flag_choice_1.frame.grid(row=0, column=0, sticky='ns')
        self.flag_choice_2.frame.grid(row=0, column=1, sticky='ns')
