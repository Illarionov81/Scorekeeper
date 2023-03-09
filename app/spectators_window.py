from tkinter import *
from tkinter import ttk

from utils import to_uppercase


class SpectatorsWindow:
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
		stage,
		group,
		explanation,
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
		self.stage = stage
		self.group = group
		self.explanation = explanation
		self.timer = timer
		self.create_window()

	def update_title(self, *args):
	    self.window.title(self.title.get())

	def create_window(self):
		self.window = Toplevel(self.master)
		# window.attributes('-fullscreen', True)
		self.window.geometry("850x400")
		self.window.title(self.title.get())

		# Обновление заголовка окна при изменении переменной StringVar
		self.title.trace_add("write", self.update_title)

		self.name_1.trace("w", lambda *args: to_uppercase(*args, text_var=self.name_1))
		self.club_1.trace("w", lambda *args: to_uppercase(*args, text_var=self.club_1))
		self.name_2.trace("w", lambda *args: to_uppercase(*args, text_var=self.name_2))
		self.club_2.trace("w", lambda *args: to_uppercase(*args, text_var=self.club_2))
		self.stage.trace("w", lambda *args: to_uppercase(*args, text_var=self.stage))
		self.group.trace("w", lambda *args: to_uppercase(*args, text_var=self.group))
		self.explanation.trace("w", lambda *args: to_uppercase(*args, text_var=self.explanation))

		for r in range(8): self.window.rowconfigure(index=r, weight=1)
		for c in range(3): self.window.columnconfigure(index=c, weight=1)

		# Ряд первый спортсмен - 0,1
		athlete_1_name=ttk.Label(self.window, textvariable=self.name_1).grid(row=0, column=0, ipadx=6, ipady=6)
		athlete_1_club=ttk.Label(self.window, textvariable=self.club_1).grid(row=1, column=0)
		athlete_fall_1 = ttk.Label(self.window, textvariable=self.fall_1).grid(row=0, column=1)
		athlete_adv_1 = ttk.Label(self.window, textvariable=self.adv_1).grid(row=1, column=1)
		athlete_1_points=ttk.Label(self.window, textvariable=self.points_1).grid(row=0, column=2, rowspan=2)

		# Ряд второй- тймер - 2,3
		self.spectators_timer=ttk.Label(self.window, textvariable=self.timer)
		self.spectators_timer.grid(row=2, column=0, columnspan=3, rowspan=2)

		# Ряд третий спортсмен - 4,5
		athlete_2_name=ttk.Label(self.window, textvariable=self.name_2).grid(row=4, column=0)
		athlete_2_club=ttk.Label(self.window, textvariable=self.club_2).grid(row=5, column=0)
		athlete_fall_2 = ttk.Label(self.window, textvariable=self.fall_2).grid(row=4, column=1)
		athlete_adv_2 = ttk.Label(self.window, textvariable=self.adv_2).grid(row=5, column=1)
		athlete_2_points=ttk.Label(self.window, textvariable=self.points_2).grid(row=4, column=2, rowspan=2)

		# Четвертый ряд - данные - 6,7
		championship_stage=ttk.Label(self.window, textvariable=self.stage).grid(row=6, column=0)
		championship_group=ttk.Label(self.window, textvariable=self.group).grid(row=7, column=0)
		championship_explanation=ttk.Label(self.window, textvariable=self.explanation).grid(row=8, column=0)