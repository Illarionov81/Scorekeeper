from tkinter import *
from tkinter import ttk

import config
from utils import to_uppercase


class AthleteInfo:
	def __init__(
			self,
			bg,
			window,
			flag_path,
			bg_style,
			name,
			club,
			points,
			label_style,
			fall,
			adv,
			fall_point_style,
			border_color,
	):
		self.window = window
		self.bg = bg
		self.flag_path = flag_path
		self.common_bg_style = bg_style
		self.name = name
		self.club = club
		self.points = points
		self.label_style = label_style
		self.fall = fall
		self.adv = adv
		self.fall_point_style = fall_point_style
		self.border_color = border_color
		self.sportsman_frame = None
		self.create_frame()
		self.change_flag()

	def create_frame(self):
		self.sportsman_frame = Frame(self.window)
		self.sportsman_frame.configure(
			bg=self.bg,
			highlightbackground=self.border_color,
			highlightthickness=1,
			borderwidth=1,
			relief='ridge'
		)
		for r in range(2): self.sportsman_frame.rowconfigure(index=r, weight=1)
		for c in range(4): self.sportsman_frame.columnconfigure(index=c, weight=1)

		self.sportsman_frame.columnconfigure(index=0, weight=5, uniform="col1")  # flag
		self.sportsman_frame.columnconfigure(index=1, weight=71, uniform="col1")  # sportsmen name & club
		self.sportsman_frame.columnconfigure(index=2, weight=4, uniform="col1")  # fall label & adv label
		self.sportsman_frame.columnconfigure(index=3, weight=20, uniform="col1")  # points

		self.sportsman_frame.rowconfigure(index=0, weight=70, uniform="row2")
		self.sportsman_frame.rowconfigure(index=1, weight=30, uniform="row2")

		val = str(self.flag_path.get()).split('/')[-1].split('.')[0]
		self.flag_val = StringVar(value=val)
		self.flag = ttk.Label(self.sportsman_frame, textvariable=self.flag_val)
		self.flag.config(
			style=self.common_bg_style,
			compound='top',
			font=('Arial', 18, 'bold'),
			anchor="n",
		)
		name = ttk.Label(self.sportsman_frame, textvariable=self.name)
		name.config(
			style=self.common_bg_style,
			font=('monospace', 72, 'bold'),
			anchor='sw',
		)
		club = ttk.Label(self.sportsman_frame, textvariable=self.club)
		club.config(
			style=self.common_bg_style,
			font=('Arial', 24, 'bold'),
			anchor='n',
		)
		points = ttk.Label(self.sportsman_frame, textvariable=self.points, style=self.label_style)
		points.config(font=('Arial', 125, 'bold'))
		fall_points_frame = self.additional_points_frame()

		self.flag.grid(row=0, column=0, rowspan=2, sticky='nsew')
		name.grid(row=0, column=1, sticky='nsew')
		club.grid(row=1, column=1, sticky='nsew')
		fall_points_frame.grid(row=0, column=2, rowspan=2, sticky='nsew')
		points.grid(row=0, column=3, rowspan=2, sticky='nsew')

		self.name.trace("w", lambda *args: to_uppercase(*args, text_var=self.name))
		self.club.trace("w", lambda *args: to_uppercase(*args, text_var=self.club))
		self.flag_path.trace("w", self.change_flag)

	def additional_points_frame(self):
		fall_points_frame = Frame(self.sportsman_frame, bg=self.bg)

		label_fall = ttk.Label(fall_points_frame, text='fall', style='label_5.TLabel')
		label_adv = ttk.Label(fall_points_frame, text='adv', style='label_5.TLabel')
		fall = ttk.Label(fall_points_frame, textvariable=self.fall, style=self.fall_point_style)
		adv = ttk.Label(fall_points_frame, textvariable=self.adv, style=self.fall_point_style)

		label_fall.grid(row=0, column=0, sticky='nsew')
		fall.grid(row=1, column=0, sticky='nsew')
		label_adv.grid(row=2, column=0, sticky='nsew')
		adv.grid(row=3, column=0, sticky='nsew')

		return fall_points_frame

	def change_flag(self, *args, **kwargs):
		flag_path = self.flag_path.get()
		self.flag_img = PhotoImage(file=flag_path)
		self.flag.config(image=self.flag_img, anchor="center")
		val = str(flag_path).split('/')[-1].split('.')[0]
		self.flag_val.set(val)


class SpectatorsWindow:
	def __init__(
			self,
			master,
			title,
			color_1,
			color_2,
			label_1_style,
			label_2_style,
			fall_point_style,
			dark,
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
			stage,
			group,
			belt,
			timer,
			flag_path_1,
			flag_path_2,
	):
		self.master = master
		self.title = title
		self.color_1 = color_1,
		self.color_2 = color_2,
		self.label_1_style = label_1_style,
		self.label_2_style = label_2_style,
		self.fall_point_style = fall_point_style,
		self.dark = dark
		self.name_1 = name_1
		self.club_1 = club_1
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
		self.stage = stage
		self.group = group
		self.belt = belt
		self.timer = timer
		self.flag_path_1 = flag_path_1
		self.flag_path_2 = flag_path_2
		self.bg = config.SPECTATOR_WINDOW_BG
		self.info_frame = None
		self.window = None
		self.sportsman_1_frame = None
		self.create_window()
		self.create_total_info_frame()
		self.athlete_1 = AthleteInfo(
			self.bg,
			self.window,
			self.flag_path_1,
			self.dark,
			self.name_1,
			self.club_1,
			self.points_1,
			self.label_1_style,
			self.fall_1,
			self.adv_1,
			self.fall_point_style,
			config.ATHLETE_1_BORDER_COLOR
		)
		self.create_timer_frame()
		self.athlete_2 = AthleteInfo(
			self.bg,
			self.window,
			self.flag_path_2,
			self.dark,
			self.name_2,
			self.club_2,
			self.points_2,
			self.label_2_style,
			self.fall_2,
			self.adv_2,
			self.fall_point_style,
			config.ATHLETE_2_BORDER_COLOR,
		)
		self.frame_placement()

	def update_title(self, *args):
		self.window.title(self.title.get())

	def create_window(self):
		self.window = Toplevel(self.master, bg=self.bg)
		self.window.attributes("-zoomed", True)
		self.window.attributes("-fullscreen", False)
		self.window.bind("<Double-Button-1>", self.toggle_fullscreen)

		# Обновление заголовка окна при изменении переменной StringVar
		self.window.title(self.title.get())
		self.title.trace_add("write", self.update_title)

	def toggle_fullscreen(self, event):
		if not self.window.attributes('-fullscreen'):
			self.window.attributes('-fullscreen', True)
		else:
			self.window.attributes('-fullscreen', False)

	def create_total_info_frame(self):
		self.info_frame = Frame(self.window, bg=self.bg)
		for r in range(1): self.info_frame.rowconfigure(index=r, weight=1)
		for c in range(3): self.info_frame.columnconfigure(index=c, weight=1)

		self.info_frame.columnconfigure(index=0, weight=33, uniform="row1")
		self.info_frame.columnconfigure(index=1, weight=33, uniform="row1")
		self.info_frame.columnconfigure(index=2, weight=33, uniform="row1")

		stage = ttk.Label(self.info_frame, textvariable=self.stage, style=self.dark)
		stage.config(font=('Arial', 24, 'bold'), anchor='c')
		group = ttk.Label(self.info_frame, textvariable=self.group, style=self.dark)
		group.config(font=('Arial', 24, 'bold'), anchor='c')
		belt = ttk.Label(self.info_frame, textvariable=self.belt, style=self.dark)
		belt.config(font=('Arial', 24, 'bold'), anchor='c')

		stage.grid(row=0, column=0)
		group.grid(row=0, column=1)
		belt.grid(row=0, column=2)

		self.stage.trace("w", lambda *args: to_uppercase(*args, text_var=self.stage))
		self.group.trace("w", lambda *args: to_uppercase(*args, text_var=self.group))
		self.belt.trace("w", lambda *args: to_uppercase(*args, text_var=self.belt))

		for i in [self.stage, self.group, self.belt]:
			to_uppercase(text_var=i)

	def create_timer_frame(self):
		self.timer_frame = Frame(self.window, bg=self.bg)

		for r in range(1): self.timer_frame.rowconfigure(index=r, weight=1)
		for c in range(1): self.timer_frame.columnconfigure(index=c, weight=1)

		self.spectators_timer = ttk.Label(self.timer_frame, textvariable=self.timer, style=self.dark)
		self.spectators_timer.config(font=('Arial', 125, 'bold'), anchor='c')

		self.spectators_timer.grid(row=0, column=0, columnspan=3, rowspan=2)

	def frame_placement(self):
		for i in range(5):
			self.window.grid_rowconfigure(i, weight=1)

		self.window.grid_columnconfigure(0, weight=1)

		self.window.rowconfigure(index=0, weight=10, uniform="window_row1")
		self.window.rowconfigure(index=1, weight=33, uniform="window_row1")
		self.window.rowconfigure(index=2, weight=23, uniform="window_row1")
		self.window.rowconfigure(index=3, weight=33, uniform="window_row1")

		self.info_frame.grid(row=0, column=0, sticky='nsew')
		self.athlete_1.sportsman_frame.grid(row=1, column=0, sticky='nsew')
		self.timer_frame.grid(row=2, column=0, sticky='nsew')
		self.athlete_2.sportsman_frame.grid(row=3, column=0, sticky='nsew')
