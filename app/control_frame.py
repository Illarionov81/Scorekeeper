from tkinter import ttk, Frame, StringVar, PhotoImage

import config
from utils import get_all_country


class ControlPanel:
    def __init__(
            self,
            master,
            title,
            name_1,
            club_1,
            points_1,
            fall_1,
            adv_1,
            name_2,
            club_2,
            points_2,
            fall_2,
            adv_2,
            timer,
    ):
        self.master = master
        self.title = title
        self.name_1 = name_1
        self.club_1 = club_1
        self.points_1 = points_1
        self.fall_1 = fall_1
        self.adv_1 = adv_1
        self.name_2 = name_2
        self.club_2 = club_2
        self.points_2 = points_2
        self.fall_2 = fall_2
        self.adv_2 = adv_2
        self.timer = timer
        self.create_general_info_frame()
        self.create_flag_choice()
        self.create_sportsman_frame()

    def create_general_info_frame(self):
        self.general_info_frame = Frame(self.master)
        self.general_info_frame.configure(bg=config.CONTROL_GENERAL_BG)

        for r in range(5):
            self.general_info_frame.rowconfigure(index=r, weight=1)

        for c in range(3):
            self.general_info_frame.columnconfigure(index=c, weight=1)

        self.stage_val = StringVar()
        self.group_val = StringVar()
        self.belt_val = StringVar()

        stage_choice = [
            'EIGHTH-FINALS',
            'QUARTERFINALS',
            'SEMIFINALS',
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

        self.title = ttk.Entry(self.general_info_frame, textvariable=self.title, justify='center')

        self.stage_label = ttk.Label(self.general_info_frame, text='Stage: ', anchor='c')
        self.group_label = ttk.Label(self.general_info_frame, text='Group: ', anchor='c')
        self.belt_label = ttk.Label(self.general_info_frame, text='Belt: ', anchor='c')

        self.stage = ttk.Combobox(self.general_info_frame, textvariable=self.stage_val, values=stage_choice,
                                  justify='center')
        self.stage.current(0)
        self.group = ttk.Combobox(self.general_info_frame, textvariable=self.group_val, values=group_choice,
                                  justify='center')
        self.group.current(0)
        self.belt = ttk.Combobox(self.general_info_frame, textvariable=self.belt_val, values=belt_choice,
                                 justify='center')
        self.belt.current(0)

        self.title.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.stage_label.grid(row=2, column=0, sticky='nsew')
        self.group_label.grid(row=2, column=1, sticky='nsew')
        self.belt_label.grid(row=2, column=2, sticky='nsew')
        self.stage.grid(row=3, column=0, sticky='nsew')
        self.group.grid(row=3, column=1, sticky='nsew')
        self.belt.grid(row=3, column=2, sticky='nsew')

    def create_flag_choice(self):
        self.flag_choice_frame = Frame(self.master)
        self.flag_choice_frame.configure(bg=config.CONTROL_GENERAL_BG)

        for r in range(1):
            self.flag_choice_frame.rowconfigure(index=r, weight=1)

        for c in range(4):
            self.flag_choice_frame.columnconfigure(index=c, weight=1)

        country_name = sorted(get_all_country())
        self.flag_str = "./../img/flags-iso/{country}"
        self.flag_var_1 = StringVar(value='KG.png')
        self.flag_var_2 = StringVar(value='KG.png')
        self.flag_path_1 = self.flag_str.format(country=self.flag_var_1.get())
        self.flag_path_2 = self.flag_str.format(country=self.flag_var_2.get())
        self.flag_path_1_for_spectators = StringVar(value=self.flag_path_1)
        self.flag_path_2_for_spectators = StringVar(value=self.flag_path_2)

        self.flag_label_1 = ttk.Label(self.flag_choice_frame, text='flag sportsman 1: ', anchor='e')
        self.flag_label_2 = ttk.Label(self.flag_choice_frame, text='flag sportsman 2: ', anchor='e')
        self.flag_box1 = ttk.Combobox(self.flag_choice_frame, textvariable=self.flag_var_1, values=country_name)
        self.flag_box2 = ttk.Combobox(self.flag_choice_frame, textvariable=self.flag_var_2, values=country_name)

        self.flag_box1.bind("<<ComboboxSelected>>", self.select_flag)
        self.flag_box2.bind("<<ComboboxSelected>>", self.select_flag)

        self.flag_label_1.grid(row=0, column=0, sticky='nsew')
        self.flag_label_2.grid(row=0, column=2, sticky='nsew')
        self.flag_box1.grid(row=0, column=1, sticky='nsew')
        self.flag_box2.grid(row=0, column=3, sticky='nsew')
        self.flag_label_1.grid_configure(padx=(20, 0))
        self.flag_label_2.grid_configure(padx=(10, 0))
        self.flag_box1.grid_configure(padx=(0, 10))
        self.flag_box2.grid_configure(padx=(0, 20))

    def select_flag(self, event):
        selected = event.widget.get()
        flag_path = self.flag_str.format(country=selected)
        width = self.sportsman_frame.winfo_width()
        if event.widget == self.flag_box1:
            self.flag_path_1_for_spectators.set(flag_path)
            self.flag_path_1 = flag_path
            self.flag_img_1 = self.change_flag(width, self.flag_1, flag_path)
        if event.widget == self.flag_box2:
            self.flag_path_2_for_spectators.set(flag_path)
            self.flag_path_2 = flag_path
            self.flag_img_2 = self.change_flag(width, self.flag_2, flag_path)

    def create_sportsman_frame(self):
        self.sportsman_frame = Frame(self.master)
        self.sportsman_frame.configure(bg=config.CONTROL_GENERAL_BG)

        for r in range(8): self.sportsman_frame.rowconfigure(index=r, weight=1)
        for c in range(5): self.sportsman_frame.columnconfigure(index=c, weight=1)

        self.sportsman_frame.columnconfigure(index=0, weight=6, uniform="row1")  # flag
        self.sportsman_frame.columnconfigure(index=1, weight=90, uniform="row1")  # sportsmen name & club
        self.sportsman_frame.columnconfigure(index=2, weight=3, uniform="row1")  # fall label & adv label
        self.sportsman_frame.columnconfigure(index=3, weight=3, uniform="row1")  # fall & adv
        self.sportsman_frame.columnconfigure(index=4, weight=6, uniform="row1")  # points

        self.flag_1 = ttk.Label(self.sportsman_frame)
        name_1 = ttk.Entry(self.sportsman_frame, textvariable=self.name_1)
        club_1 = ttk.Entry(self.sportsman_frame, textvariable=self.club_1)
        fall_1 = ttk.Entry(self.sportsman_frame, textvariable=self.fall_1, justify='center')
        adv_1 = ttk.Entry(self.sportsman_frame, textvariable=self.adv_1, justify='center')
        points_1 = ttk.Entry(self.sportsman_frame, textvariable=self.points_1, style=config.ENTRY_STYLE_1,
                             font=('Arial', 18, 'bold'), justify='center')

        self.flag_2 = ttk.Label(self.sportsman_frame)
        name_2 = ttk.Entry(self.sportsman_frame, textvariable=self.name_2)
        club_2 = ttk.Entry(self.sportsman_frame, textvariable=self.club_2)
        fall_2 = ttk.Entry(self.sportsman_frame, textvariable=self.fall_2, justify='center')
        adv_2 = ttk.Entry(self.sportsman_frame, textvariable=self.adv_2, justify='center')
        points_2 = ttk.Entry(self.sportsman_frame, textvariable=self.points_2, style=config.ENTRY_STYLE_2,
                             font=('Arial', 18, 'bold'), justify='center')

        label_1_fall = ttk.Label(self.sportsman_frame, text='fall', style=config.LABEL_STYLE_1)
        label_1_adv = ttk.Label(self.sportsman_frame, text='adv', style=config.LABEL_STYLE_1)
        label_2_fall = ttk.Label(self.sportsman_frame, text='fall', style=config.LABEL_STYLE_2)
        label_2_adv = ttk.Label(self.sportsman_frame, text='adv', style=config.LABEL_STYLE_2)

        self.flag_1.grid(row=0, column=0, rowspan=2, sticky='nsew')
        name_1.grid(row=0, column=1, sticky='nsew')
        club_1.grid(row=1, column=1, sticky='nsew')
        label_1_fall.grid(row=0, column=2, sticky='nsew')
        label_1_adv.grid(row=1, column=2, sticky='nsew')
        fall_1.grid(row=0, column=3, sticky='nsew')
        adv_1.grid(row=1, column=3, sticky='nsew')
        points_1.grid(row=0, column=4, rowspan=2, sticky='nsew')

        self.flag_2.grid(row=3, column=0, rowspan=2, sticky='nsew')
        name_2.grid(row=3, column=1, sticky='nsew')
        club_2.grid(row=4, column=1, sticky='nsew')
        label_2_fall.grid(row=3, column=2, sticky='nsew')
        label_2_adv.grid(row=4, column=2, sticky='nsew')
        fall_2.grid(row=3, column=3, sticky='nsew')
        adv_2.grid(row=4, column=3, sticky='nsew')
        points_2.grid(row=3, column=4, rowspan=2, sticky='nsew')

        self.sportsman_frame.bind('<Configure>', self.img_size_configure)

    @staticmethod
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

    def img_size_configure(self, event):
        width = event.width
        self.flag_img_1 = self.change_flag(width, self.flag_1, self.flag_path_1)
        self.flag_img_2 = self.change_flag(width, self.flag_2, self.flag_path_2)
