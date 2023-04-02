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
		entry_style_1,
		entry_style_2,
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
		explanation,
		timer,
		flag_path_1,
		flag_path_2,
		):
		self.master = master
		self.title = title
		self.color_1 = color_1,
		self.color_2 = color_2,
		self.entry_style_1 = entry_style_1,
		self.entry_style_2 = entry_style_2,
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
		self.explanation = explanation
		self.timer = timer
		self.flag_path_1 = flag_path_1
		self.flag_path_2 = flag_path_2
		self.create_window()
		self.create_total_info_frame()
		self.create_sportsman_1_frame()
		self.create_timer_frame()
		self.create_sportsman_2_frame()
		self.frame_placement()

	def update_title(self, *args):
	    self.window.title(self.title.get())

	def create_window(self):
		self.window = Toplevel(self.master)
		self.window.attributes("-zoomed", True)
		self.window.attributes( "-type", "toplevel")

		# Обновление заголовка окна при изменении переменной StringVar
		self.window.title(self.title.get())
		self.title.trace_add("write", self.update_title)

	def create_total_info_frame(self):
		"""First row - info"""
		self.info_frame = Frame(self.window)

		for r in range(1): self.info_frame.rowconfigure(index=r, weight=1)
		for c in range(2): self.info_frame.columnconfigure(index=c, weight=1)

		self.info_frame.columnconfigure(index=0, weight=16, uniform="row1") 
		self.info_frame.columnconfigure(index=1, weight=94, uniform="row1")

		stage=ttk.Label(self.info_frame, textvariable=self.stage) # add choise for stage and category/group
		group=ttk.Label(self.info_frame, textvariable=self.group)

		stage.grid(row=0, column=0)
		group.grid(row=0, column=1)

		self.stage.trace("w", lambda *args: to_uppercase(*args, text_var=self.stage))
		self.group.trace("w", lambda *args: to_uppercase(*args, text_var=self.group))


	def create_sportsman_1_frame(self):
		"""Row second - sportsman 1 """
		self.sportsman_1_frame = Frame(self.window)

		for r in range(2): self.sportsman_1_frame.rowconfigure(index=r, weight=1)
		for c in range(5): self.sportsman_1_frame.columnconfigure(index=c, weight=1)

		self.sportsman_1_frame.columnconfigure(index=0, weight=6, uniform="row1") # flag
		self.sportsman_1_frame.columnconfigure(index=1, weight=93, uniform="row1") # sportsmen name
		self.sportsman_1_frame.columnconfigure(index=1, weight=93, uniform="row1") # club 
		self.sportsman_1_frame.columnconfigure(index=2, weight=3, uniform="row1") # fall label
		self.sportsman_1_frame.columnconfigure(index=2, weight=3, uniform="row1") # adv label
		self.sportsman_1_frame.columnconfigure(index=4, weight=6, uniform="row1") # points


		label_1_style = ttk.Style().configure(
			'label_1_s.TLabel',
			background=self.color_1,
			foreground="white",
			anchor="center",
			)

		self.flag_1 = ttk.Label(self.sportsman_1_frame)
		athlete_1_name=ttk.Label(self.sportsman_1_frame, textvariable=self.name_1)
		athlete_1_club=ttk.Label(self.sportsman_1_frame, textvariable=self.club_1)
		athlete_fall_1 = ttk.Label(self.sportsman_1_frame, textvariable=self.fall_1, style='label_1_s.TLabel',  font=('Arial', 8, 'bold'))
		athlete_adv_1 = ttk.Label(self.sportsman_1_frame, textvariable=self.adv_1, style='label_1_s.TLabel', font=('Arial', 8, 'bold'))
		athlete_1_points=ttk.Label(self.sportsman_1_frame, textvariable=self.points_1, style='label_1_s.TLabel', font=('Arial', 18, 'bold'))

		self.flag_1.grid(row=0, column=0, rowspan=2, sticky='nsew')
		athlete_1_name.grid(row=0, column=1, sticky='nsew')
		athlete_1_club.grid(row=1, column=1, sticky='nsew')
		athlete_fall_1.grid(row=0, column=2, sticky='nsew')
		athlete_adv_1.grid(row=1, column=2, sticky='nsew')
		athlete_1_points.grid(row=0, column=3, rowspan=2, sticky='nsew')

		self.name_1.trace("w", lambda *args: to_uppercase(*args, text_var=self.name_1))
		self.club_1.trace("w", lambda *args: to_uppercase(*args, text_var=self.club_1))
		self.flag_path_1.trace("w", self.chenge_flag)

	def chenge_flag(self, *args, **kwargs):
		self.flag_img_1 = PhotoImage(file=self.flag_path_1.get())
		print(self.flag_path_1.get())
		# self.flag_img_1 = flag_img.subsample(rate)
		self.flag_1.config(image=self.flag_img_1, anchor="center")

	def create_timer_frame(self):
		"""Second row timer"""
		self.timer_frame = Frame(self.window)

		for r in range(1): self.timer_frame.rowconfigure(index=r, weight=1)
		for c in range(1): self.timer_frame.columnconfigure(index=c, weight=1)

		self.spectators_timer=ttk.Label(self.timer_frame, textvariable=self.timer)
		self.spectators_timer.grid(row=2, column=0, columnspan=3, rowspan=2)

	def create_sportsman_2_frame(self):
		self.sportsman_2_frame = Frame(self.window)

		for r in range(8): self.sportsman_2_frame.rowconfigure(index=r, weight=1)
		for c in range(3): self.sportsman_2_frame.columnconfigure(index=c, weight=1)

		# Ряд третий спортсмен - 4,5
		athlete_2_name=ttk.Label(self.sportsman_2_frame, textvariable=self.name_2)
		athlete_2_club=ttk.Label(self.sportsman_2_frame, textvariable=self.club_2)
		athlete_fall_2 = ttk.Label(self.sportsman_2_frame, textvariable=self.fall_2)
		athlete_adv_2 = ttk.Label(self.sportsman_2_frame, textvariable=self.adv_2)
		athlete_2_points=ttk.Label(self.sportsman_2_frame, textvariable=self.points_2)

		athlete_2_name.grid(row=4, column=0)
		athlete_2_club.grid(row=5, column=0)
		athlete_fall_2.grid(row=4, column=1)
		athlete_adv_2.grid(row=5, column=1)
		athlete_2_points.grid(row=4, column=2, rowspan=2)

		self.name_2.trace("w", lambda *args: to_uppercase(*args, text_var=self.name_2))
		self.club_2.trace("w", lambda *args: to_uppercase(*args, text_var=self.club_2))
		

	def frame_placement(self):
		for i in range(5):
			self.window.grid_rowconfigure(i, weight=1)

		self.window.grid_columnconfigure(0, weight=1)

		self.window.rowconfigure(index=0, weight=5, uniform="window_row1")
		self.window.rowconfigure(index=2, weight=22, uniform="window_row1")
		self.window.rowconfigure(index=3, weight=36, uniform="window_row1")
		self.window.rowconfigure(index=4, weight=22, uniform="window_row1")

		self.info_frame.grid(row=0, column=0, sticky='nsew')
		self.sportsman_1_frame.grid(row=2, column=0, sticky='nsew')
		self.timer_frame.grid(row=3, column=0, sticky='nsew')
		self.sportsman_2_frame.grid(row=4, column=0, sticky='nsew')
