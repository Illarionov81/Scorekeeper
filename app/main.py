from pathlib import Path
from tkinter import TclVersion, PhotoImage, StringVar, IntVar

import config
from utils import change_flag
from athlete_frame import AthleteFrame
from control_frame import Sportsman, FlagChoiceFrame, GeneralInfo
from spectators_window import SpectatorsWindow
from styles import create_styles
from timer_frame import TimeFrame

if TclVersion < 8.5:
    print(f'Версия Tkinter {TclVersion} не поддерживает стили. Пожалуйста, обновите Tkinter до версии 8.5 или выше.')
else:
    print(f'Версия Tkinter {TclVersion} поддерживает стили.')


class App:
    flag_str = "{root_path}/img/flags-iso/{country}"

    def __init__(self, main):
        self.main = main
        self.flag_img_1 = None
        self.flag_img_2 = None
        self.root_path = Path(__file__).parent.parent

        self.stage_val = StringVar()
        self.group_val = StringVar()
        self.belt_val = StringVar()

        self.title_of_spectators_window = StringVar(self.main, value='... COMPETITION')
        self.name_1 = StringVar(self.main, value='NAME-1')
        self.surname_1 = StringVar(self.main, value='SURNAME')
        self.club_1 = StringVar(self.main, value='SPORT CLUB NAME')
        self.points_1 = IntVar(self.main, value=0)
        self.fall_1 = IntVar(self.main, value=0)
        self.adv_1 = IntVar(self.main, value=0)

        self.name_2 = StringVar(self.main, value='NAME-2')
        self.surname_2 = StringVar(self.main, value='SURNAME')
        self.club_2 = StringVar(self.main, value='SPORT CLUB NAME')
        self.points_2 = IntVar(self.main, value=0)
        self.fall_2 = IntVar(self.main, value=0)
        self.adv_2 = IntVar(self.main, value=0)

        self.timer = StringVar(self.main, value='00:00')

        create_styles()
        self.create_main_frame()

        self.general_info = GeneralInfo(
            main=self.main,
            title=self.title_of_spectators_window,
            stage_val=self.stage_val,
            group_val=self.group_val,
            belt_val=self.belt_val,
        )

        self.flag_frame = FlagChoiceFrame(self.main, self.flag_str)
        self.flag_frame.flag_choice_1.flag_box.bind("<<ComboboxSelected>>", self.select_flag)
        self.flag_frame.flag_choice_2.flag_box.bind("<<ComboboxSelected>>", self.select_flag)

        self.sportsman_1 = Sportsman(
            main=self.main,
            bg=config.CONTROL_GENERAL_BG,
            border_color=config.ATHLETE_1_COLOR,
            name=self.name_1,
            surname=self.surname_1,
            club=self.club_1,
            fall=self.fall_1,
            adv=self.adv_1,
            points=self.points_1,
            point_style=config.ENTRY_STYLE_1,
            label_style=config.LABEL_STYLE_1,
        )
        self.sportsman_2 = Sportsman(
            main=self.main,
            bg=config.CONTROL_GENERAL_BG,
            border_color=config.ATHLETE_2_COLOR,
            name=self.name_2,
            surname=self.surname_2,
            club=self.club_2,
            fall=self.fall_2,
            adv=self.adv_2,
            points=self.points_2,
            point_style=config.ENTRY_STYLE_2,
            label_style=config.LABEL_STYLE_2,
        )
        self.sportsman_1.frame.bind('<Configure>', self.img_size_configure)
        self.sportsman_2.frame.bind('<Configure>', self.img_size_configure)

        self.spectators_window = SpectatorsWindow(
            self.main,
            self.title_of_spectators_window,
            self.name_1,
            self.surname_1,
            self.club_1,
            self.points_1,
            self.fall_1,
            self.adv_1,
            self.name_2,
            self.surname_2,
            self.club_2,
            self.points_2,
            self.fall_2,
            self.adv_2,
            self.stage_val,
            self.group_val,
            self.belt_val,
            self.timer,
            self.flag_frame.flag_choice_1.flag_path_for_spectators,
            self.flag_frame.flag_choice_2.flag_path_for_spectators,
        )
        self.spectators_timer = self.spectators_window.spectators_timer
        self.time_frame = TimeFrame(self.main, self.timer, self.spectators_timer)

        self.athlete_1 = AthleteFrame(
            self.main,
            self.points_1,
            self.adv_1,
            self.fall_1,
            config.ATHLETE_1_COLOR,
            config.SET_BUTTON_1,
        )
        self.athlete_2 = AthleteFrame(
            self.main,
            self.points_2,
            self.adv_2,
            self.fall_2,
            config.ATHLETE_2_COLOR,
            config.SET_BUTTON_2,
        )
        self.frame_placement()

    def create_main_frame(self):
        icon = PhotoImage(file=f"{self.root_path}/img/icons/icon.png")
        self.main.iconphoto(False, icon)
        self.main.title("Carpe Diem")
        self.main.configure(bg=config.CONTROL_GENERAL_BG)
        self.main.geometry("740x480")
        self.main.resizable(True, True)

    def img_size_configure(self, event):
        width = event.width
        self.flag_img_1 = change_flag(width, self.sportsman_1.flag, self.flag_frame.flag_choice_1.flag_path)
        self.flag_img_2 = change_flag(width, self.sportsman_2.flag, self.flag_frame.flag_choice_2.flag_path)

    def select_flag(self, event):
        selected = event.widget.get()
        flag_path = self.flag_str.format(root_path=self.root_path, country=selected)
        width = self.flag_frame.frame.winfo_width()
        if event.widget == self.flag_frame.flag_choice_1.flag_box:
            self.flag_frame.flag_choice_1.flag_path_for_spectators.set(flag_path)
            self.flag_frame.flag_choice_1.flag_path = flag_path
            self.flag_img_1 = change_flag(width, self.sportsman_1.flag, flag_path)
        if event.widget == self.flag_frame.flag_choice_2.flag_box:
            self.flag_frame.flag_choice_2.flag_path_for_spectators.set(flag_path)
            self.flag_frame.flag_choice_2.flag_path = flag_path
            self.flag_img_2 = change_flag(width, self.sportsman_2.flag, flag_path)

    def frame_placement(self):
        for i in range(7):
            self.main.grid_rowconfigure(i, weight=1)

        self.main.grid_columnconfigure(0, weight=1)

        self.main.rowconfigure(index=0, weight=18, uniform="row1")  # general info
        self.main.rowconfigure(index=1, weight=6, uniform="row1")   # flag choice
        self.main.rowconfigure(index=2, weight=14, uniform="row1")  # sportsman name
        self.main.rowconfigure(index=3, weight=14, uniform="row1")  # sportsman name
        self.main.rowconfigure(index=4, weight=20, uniform="row1")  # time
        self.main.rowconfigure(index=5, weight=14, uniform="row1")  # button rad
        self.main.rowconfigure(index=6, weight=14, uniform="row1")  # button blue

        self.general_info.frame.grid(row=0, column=0, sticky='nsew')
        self.flag_frame.frame.grid(row=1, column=0, sticky='nsew')
        self.sportsman_1.frame.grid(row=2, column=0, sticky='nsew')
        self.sportsman_2.frame.grid(row=3, column=0, sticky='nsew')
        self.time_frame.frame.grid(row=4, column=0, sticky='nsew')
        self.athlete_1.frame.grid(row=5, column=0, sticky='nsew')
        self.athlete_2.frame.grid(row=6, column=0, sticky='nsew')
