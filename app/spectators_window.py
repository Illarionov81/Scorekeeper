from tkinter import *
from tkinter import ttk

from utils import to_uppercase


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
		self.bg = '#33313B'
		self.create_window()
		self.create_total_info_frame()
		self.create_sportsman_1_frame()
		self.create_timer_frame()
		self.create_sportsman_2_frame()
		self.chenge_flag()
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
		"""First row - info"""
		self.info_frame = Frame(self.window, bg=self.bg)

		for r in range(1): self.info_frame.rowconfigure(index=r, weight=1)
		for c in range(3): self.info_frame.columnconfigure(index=c, weight=1)

		self.info_frame.columnconfigure(index=0, weight=33, uniform="row1")
		self.info_frame.columnconfigure(index=1, weight=33, uniform="row1")
		self.info_frame.columnconfigure(index=2, weight=33, uniform="row1")

		stage=ttk.Label(self.info_frame, textvariable=self.stage, style=self.dark)
		stage.config(font=('Arial', 24, 'bold'),  anchor='c')
		group=ttk.Label(self.info_frame, textvariable=self.group, style=self.dark)
		group.config(font=('Arial', 24, 'bold'),  anchor='c')
		belt=ttk.Label(self.info_frame, textvariable=self.belt, style=self.dark)
		belt.config(font=('Arial', 24, 'bold'),  anchor='c')

		stage.grid(row=0, column=0)
		group.grid(row=0, column=1)
		belt.grid(row=0, column=2)

		self.stage.trace("w", lambda *args: to_uppercase(*args, text_var=self.stage))
		self.group.trace("w", lambda *args: to_uppercase(*args, text_var=self.group))
		self.belt.trace("w", lambda *args: to_uppercase(*args, text_var=self.belt))

		for i in [self.stage, self.group, self.belt]:
			to_uppercase(text_var=i)

	def create_sportsman_1_frame(self):
		self.sportsman_1_frame = Frame(self.window, bg=self.bg)

		val = str(self.flag_path_1.get()).split('/')[-1].split('.')[0]
		self.flag_val_1 = StringVar(value=val)

		for r in range(2): self.sportsman_1_frame.rowconfigure(index=r, weight=1)
		for c in range(5): self.sportsman_1_frame.columnconfigure(index=c, weight=1)

		self.sportsman_1_frame.columnconfigure(index=0, weight=5, uniform="row1") # flag
		self.sportsman_1_frame.columnconfigure(index=1, weight=80, uniform="row1") # sportsmen name & club
		self.sportsman_1_frame.columnconfigure(index=2, weight=2, uniform="row1") # fall label & adv label
		self.sportsman_1_frame.columnconfigure(index=3, weight=2, uniform="row1") # adv fall points
		self.sportsman_1_frame.columnconfigure(index=4, weight=15, uniform="row1") # points

		self.flag_1 = ttk.Label(self.sportsman_1_frame, style=self.dark)
		flag_label = ttk.Label(self.sportsman_1_frame, textvariable=self.flag_val_1)
		flag_label.config(
			style=self.dark,
			font=('Arial', 18, 'bold'),
			anchor='n',
		)

		name=ttk.Label(self.sportsman_1_frame, textvariable=self.name_1, style=self.dark)
		club=ttk.Label(self.sportsman_1_frame, textvariable=self.club_1, style=self.dark)

		label_fall = ttk.Label(self.sportsman_1_frame, text='fall', style=self.dark)
		label_adv = ttk.Label(self.sportsman_1_frame, text='adv', style=self.dark)

		fall = ttk.Label(self.sportsman_1_frame, textvariable=self.fall_1, style=self.fall_point_style)
		adv = ttk.Label(self.sportsman_1_frame, textvariable=self.adv_1, style=self.fall_point_style)

		points=ttk.Label(self.sportsman_1_frame, textvariable=self.points_1, style=self.label_1_style)
		points.config(font=('Arial', 125, 'bold'))

		self.flag_1.grid(row=0, column=0, rowspan=1, sticky='nsew')
		flag_label.grid(row=1, column=0, rowspan=1, sticky='nsew')
		name.grid(row=0, column=1, sticky='nsew')
		club.grid(row=1, column=1, sticky='nsew')
		label_fall.grid(row=0, column=2, sticky='nsew')
		label_adv.grid(row=1, column=2, sticky='nsew')
		fall.grid(row=0, column=3, sticky='nsew')
		adv.grid(row=1, column=3, sticky='nsew')
		points.grid(row=0, column=4, rowspan=2, sticky='nsew')

		self.name_1.trace("w", lambda *args: to_uppercase(*args, text_var=self.name_1))
		self.club_1.trace("w", lambda *args: to_uppercase(*args, text_var=self.club_1))
		self.flag_path_1.trace("w", self.chenge_flag)

	def create_sportsman_2_frame(self):
		"""Row second - sportsman 1 """
		self.sportsman_2_frame = Frame(self.window, bg=self.bg)
		for r in range(2): self.sportsman_2_frame.rowconfigure(index=r, weight=1)
		for c in range(4): self.sportsman_2_frame.columnconfigure(index=c, weight=1)

		self.sportsman_2_frame.columnconfigure(index=0, weight=5, uniform="col1")   # flag
		self.sportsman_2_frame.columnconfigure(index=1, weight=71, uniform="col1")  # sportsmen name & club
		self.sportsman_2_frame.columnconfigure(index=2, weight=4, uniform="col1")   # fall label & adv label
		self.sportsman_2_frame.columnconfigure(index=3, weight=20, uniform="col1")   # points

		self.sportsman_2_frame.rowconfigure(index=0, weight=70, uniform="row2")
		self.sportsman_2_frame.rowconfigure(index=1, weight=30, uniform="row2")

		val = str(self.flag_path_2.get()).split('/')[-1].split('.')[0]
		self.flag_val_2 = StringVar(value=val)
		self.flag_2 = ttk.Label(self.sportsman_2_frame, textvariable=self.flag_val_2)
		self.flag_2.config(
			style=self.dark,
			compound='top',
			font=('Arial', 18, 'bold'),
			anchor="n",
		)
		name = ttk.Label(self.sportsman_2_frame, textvariable=self.name_2)
		name.config(
			style=self.dark,
			font=('monospace', 67, 'bold'),
			anchor='sw',
		)
		club = ttk.Label(self.sportsman_2_frame, textvariable=self.club_2)
		club.config(
			style=self.dark,
			font=('Arial', 24, 'bold'),
			anchor='n',
		)
		points=ttk.Label(self.sportsman_2_frame, textvariable=self.points_2, style=self.label_2_style)
		points.config(font=('Arial', 125, 'bold'))
		self.fall_points_frame = self.additional_points_frame()

		self.flag_2.grid(row=0, column=0, rowspan=2, sticky='nsew')
		name.grid(row=0, column=1, sticky='nsew')
		club.grid(row=1, column=1, sticky='nsew')
		self.fall_points_frame.grid(row=0, column=2, rowspan=2, sticky='nsew')
		points.grid(row=0, column=3, rowspan=2, sticky='nsew')

		self.name_2.trace("w", lambda *args: to_uppercase(*args, text_var=self.name_2))
		self.club_2.trace("w", lambda *args: to_uppercase(*args, text_var=self.club_2))
		self.flag_path_2.trace("w", self.chenge_flag)

	def additional_points_frame(self):
		fall_points_frame = Frame(self.sportsman_2_frame, bg=self.bg)

		label_fall = ttk.Label(fall_points_frame, text='fall', style='label_5.TLabel')
		label_adv = ttk.Label(fall_points_frame, text='adv', style='label_5.TLabel')
		fall = ttk.Label(fall_points_frame, textvariable=self.fall_2, style=self.fall_point_style)
		adv = ttk.Label(fall_points_frame, textvariable=self.adv_2, style=self.fall_point_style)

		label_fall.grid(row=0, column=0, sticky='nsew')
		fall.grid(row=1, column=0, sticky='nsew')
		label_adv.grid(row=2, column=0, sticky='nsew')
		adv.grid(row=3, column=0, sticky='nsew')

		return fall_points_frame

	def chenge_flag(self, *args, **kwargs):
		self.flag_img_1 = PhotoImage(file=self.flag_path_1.get())
		self.flag_1.config(image=self.flag_img_1, anchor="center")
		val_1 = str(self.flag_path_1.get()).split('/')[-1].split('.')[0]
		self.flag_val_1.set(val_1)

		self.flag_img_2 = PhotoImage(file=self.flag_path_2.get())
		self.flag_2.config(image=self.flag_img_2, anchor="center")
		val_2 = str(self.flag_path_2.get()).split('/')[-1].split('.')[0]
		self.flag_val_2.set(val_2)

	def create_timer_frame(self):
		"""Second row timer"""
		self.timer_frame = Frame(self.window, bg=self.bg)

		for r in range(1): self.timer_frame.rowconfigure(index=r, weight=1)
		for c in range(1): self.timer_frame.columnconfigure(index=c, weight=1)

		self.spectators_timer=ttk.Label(self.timer_frame, textvariable=self.timer, style=self.dark)
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
		self.sportsman_1_frame.grid(row=1, column=0, sticky='nsew')
		self.timer_frame.grid(row=2, column=0, sticky='nsew')
		self.sportsman_2_frame.grid(row=3, column=0, sticky='nsew')
