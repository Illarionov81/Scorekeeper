from tkinter import *
from tkinter import ttk

from utils import get_all_country


class ControlPanel:
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
		):
		self.master = master
		self.title = title
		self.color_1 = color_1,
		self.color_2 = color_2,
		self.entry_style_1 = entry_style_1,
		self.entry_style_2 = entry_style_2,
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
		self.create_general_info_frame()
		self.create_sporsmens_frame()

	def create_general_info_frame(self):
		self.general_info_frame = Frame(self.master)
		self.general_info_frame.configure(bg='#32323D')

		for r in range(4): self.general_info_frame.rowconfigure(index=r, weight=1)
		for c in range(3): self.general_info_frame.columnconfigure(index=c, weight=1)

		title = ttk.Entry(self.general_info_frame, textvariable=self.title, justify='center')
		stage=ttk.Entry(self.general_info_frame, textvariable=self.stage)
		group=ttk.Entry(self.general_info_frame, textvariable=self.group)
		explanation=ttk.Entry(self.general_info_frame, textvariable=self.explanation)

		title.grid(row=0, column=0, columnspan=3, sticky='nsew')
		stage.grid(row=2, column=0, sticky='nsew')
		group.grid(row=2, column=1, sticky='nsew')
		explanation.grid(row=2, column=2, sticky='nsew')

	def create_sporsmens_frame(self):
		self.sportsman_frame = Frame(self.master)
		self.sportsman_frame.configure(bg='#32323D')

		for r in range(6): self.sportsman_frame.rowconfigure(index=r, weight=1)
		for c in range(5): self.sportsman_frame.columnconfigure(index=c, weight=1)

		self.sportsman_frame.columnconfigure(index=0, weight=6, uniform="row1") # sportsmen name
		self.sportsman_frame.columnconfigure(index=1, weight=90, uniform="row1") # sportsmen name
		self.sportsman_frame.columnconfigure(index=1, weight=90, uniform="row1") # club 
		self.sportsman_frame.columnconfigure(index=2, weight=3, uniform="row1") # fall label
		self.sportsman_frame.columnconfigure(index=2, weight=3, uniform="row1") # adv label
		self.sportsman_frame.columnconfigure(index=3, weight=3, uniform="row1") # fall
		self.sportsman_frame.columnconfigure(index=3, weight=3, uniform="row1") # adv
		self.sportsman_frame.columnconfigure(index=4, weight=6, uniform="row1") # points

		style = ttk.Style()
		style.configure(
			self.entry_style_1,
			fieldbackground=self.color_1,
			foreground='white',
			)

		style_2 = ttk.Style()
		style_2.configure(
			self.entry_style_2,
			fieldbackground=self.color_2,
			foreground='white',
			)

		label_1_style = ttk.Style().configure(
			'label_1.TLabel',
			background=self.color_1,
			foreground="white",
			anchor="center",
			)

		label_2_style = ttk.Style()
		label_2_style.configure(
			'label_2.TLabel',
			background=self.color_2,
			foreground="white",
			anchor="center",
			)

		country_name = get_all_country()
		flag_box = ttk.Combobox(values=country_name)
		default_flag = 'KG.png'
		self.flag_path = f"./../img/flags-iso/{default_flag}"

		self.flag_1 = ttk.Label(self.sportsman_frame)
		name_1 = ttk.Entry(self.sportsman_frame, textvariable=self.name_1)
		club_1 = ttk.Entry(self.sportsman_frame, textvariable=self.club_1)
		fall_1 = ttk.Entry(self.sportsman_frame, textvariable=self.fall_1, justify='center')
		adv_1 = ttk.Entry(self.sportsman_frame, textvariable=self.adv_1, justify='center')
		points_1 = ttk.Entry(self.sportsman_frame, textvariable=self.points_1, style=self.entry_style_1, font=('Arial', 18, 'bold'), justify='center')

		self.flag_2 = ttk.Label(self.sportsman_frame)
		name_2 = ttk.Entry(self.sportsman_frame, textvariable=self.name_2)
		club_2 = ttk.Entry(self.sportsman_frame, textvariable=self.club_2)
		fall_2 = ttk.Entry(self.sportsman_frame, textvariable=self.fall_2, justify='center')
		adv_2 = ttk.Entry(self.sportsman_frame, textvariable=self.adv_2, justify='center')
		points_2 = ttk.Entry(self.sportsman_frame, textvariable=self.points_2, style=self.entry_style_2, font=('Arial', 18, 'bold'), justify='center')

		label_1_fall = ttk.Label(self.sportsman_frame, text='fall', style='label_1.TLabel',  font=('Arial', 8, 'bold'))
		label_1_adv = ttk.Label(self.sportsman_frame, text='adv', style='label_1.TLabel', font=('Arial', 8, 'bold'))
		label_2_fall = ttk.Label(self.sportsman_frame, text='fall', style='label_2.TLabel', font=('Arial', 8, 'bold'))
		label_2_adv = ttk.Label(self.sportsman_frame, text='adv', style='label_2.TLabel', font=('Arial', 8, 'bold'))

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

	def img_size_configure(self, event):
	    rate = 1
	    if event.width <= 650:
	    	rate = 3
	    if 650 < event.width <= 1150:
	    	rate = 2

	    self.flag_img = PhotoImage(file=self.flag_path)
	    self.flag_img = self.flag_img.subsample(rate)
	    self.flag_1.config(image=self.flag_img, anchor="center")
	    self.flag_2.config(image=self.flag_img, anchor="center")
