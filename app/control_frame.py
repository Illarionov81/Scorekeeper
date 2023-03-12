from tkinter import *
from tkinter import ttk


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
		self.create_frame()

	def create_frame(self):
		self.frame = Frame(self.master)

		for r in range(9): self.frame.rowconfigure(index=r, weight=1)
		for c in range(3): self.frame.columnconfigure(index=c, weight=1)

		title = ttk.Entry(self.frame, textvariable=self.title, justify='center')

		stage=ttk.Entry(self.frame, textvariable=self.stage)
		group=ttk.Entry(self.frame, textvariable=self.group)
		explanation=ttk.Entry(self.frame, textvariable=self.explanation)

		name_1 = ttk.Entry(self.frame, textvariable=self.name_1)
		club_1 = ttk.Entry(self.frame, textvariable=self.club_1)
		fall_1 = ttk.Entry(self.frame, textvariable=self.fall_1)
		adv_1 = ttk.Entry(self.frame, textvariable=self.adv_1)
		points_1 = ttk.Entry(self.frame, textvariable=self.points_1)

		name_2 = ttk.Entry(self.frame, textvariable=self.name_2)
		club_2 = ttk.Entry(self.frame, textvariable=self.club_2)
		fall_2 = ttk.Entry(self.frame, textvariable=self.fall_2)
		adv_2 = ttk.Entry(self.frame, textvariable=self.adv_2)
		points_2 = ttk.Entry(self.frame, textvariable=self.points_2)

		title.grid(row=0, column=0, columnspan=3, sticky='nsew')

		name_1.grid(row=2, column=0, sticky='nsew')
		club_1.grid(row=3, column=0, sticky='nsew')
		fall_1.grid(row=2, column=1, sticky='nsew')
		adv_1.grid(row=3, column=1, sticky='nsew')
		points_1.grid(row=2, column=2, rowspan=2, sticky='nsew')

		name_2.grid(row=5, column=0, sticky='nsew')
		club_2.grid(row=6, column=0, sticky='nsew')
		fall_2.grid(row=5, column=1, sticky='nsew')
		adv_2.grid(row=6, column=1, sticky='nsew')
		points_2.grid(row=5, column=2, rowspan=2, sticky='nsew')

		stage.grid(row=8, column=0, sticky='nsew')
		group.grid(row=8, column=1, sticky='nsew')
		explanation.grid(row=8, column=2, sticky='nsew')
