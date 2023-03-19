from tkinter import *
from tkinter import ttk

from utils import click_button


class Athlete_Frame:
	def __init__(
		self,
		master,
		points_1,
		adv_1,
		fall_1,
		color,
		style_name,
		):
		self.master = master
		self.points_1 = points_1
		self.adv_1 = adv_1
		self.fall_1 = fall_1
		self.color = color
		self.style_name = style_name
		self.create_frame()


	def create_frame(self):
		self.frame = Frame(self.master)

		for c in range(8): self.frame.columnconfigure(index=c, weight=1)
		for r in range(2): self.frame.rowconfigure(index=r, weight=1)

		btn1 = ttk.Button(self.frame, text="+1", command=lambda *args: click_button(*args, target=self.points_1, set_points=1))
		btn2 = ttk.Button(self.frame, text="+2", command=lambda *args: click_button(*args, target=self.points_1, set_points=2))
		btn3 = ttk.Button(self.frame, text="+3", command=lambda *args: click_button(*args, target=self.points_1, set_points=3))
		btn4 = ttk.Button(self.frame, text="+4", command=lambda *args: click_button(*args, target=self.points_1, set_points=4))
		btn5 = ttk.Button(self.frame, text="+5", command=lambda *args: click_button(*args, target=self.points_1, set_points=5))
		btn6 = ttk.Button(self.frame, text="+6", command=lambda *args: click_button(*args, target=self.points_1, set_points=6))
		btn_m1 = ttk.Button(self.frame, text="-1", command=lambda *args: click_button(*args, target=self.points_1, set_points=-1))
		btn_m2 = ttk.Button(self.frame, text="-2", command=lambda *args: click_button(*args, target=self.points_1, set_points=-2))
		btn_m3 = ttk.Button(self.frame, text="-3", command=lambda *args: click_button(*args, target=self.points_1, set_points=-3))
		btn_m4 = ttk.Button(self.frame, text="-4", command=lambda *args: click_button(*args, target=self.points_1, set_points=-4))
		btn_m5 = ttk.Button(self.frame, text="-5", command=lambda *args: click_button(*args, target=self.points_1, set_points=-5))
		btn_m6 = ttk.Button(self.frame, text="-6", command=lambda *args: click_button(*args, target=self.points_1, set_points=-6))
		btn_advp = ttk.Button(self.frame, text="+adv", command=lambda *args: click_button(*args, target=self.adv_1, set_points=1))
		btn_advm = ttk.Button(self.frame, text="-adv", command=lambda *args: click_button(*args, target=self.adv_1, set_points=-1))
		btn_fallp = ttk.Button(self.frame, text="+fall", command=lambda *args: click_button(*args, target=self.fall_1, set_points=1))
		btn_fallm = ttk.Button(self.frame, text="-fall", command=lambda *args: click_button(*args, target=self.fall_1, set_points=-1))

		btn1.grid(row=0, column=0, sticky='nsew')
		btn2.grid(row=0, column=1, sticky='nsew')
		btn3.grid(row=0, column=2, sticky='nsew')
		btn4.grid(row=0, column=3, sticky='nsew')
		btn5.grid(row=0, column=4, sticky='nsew')
		btn6.grid(row=0, column=5, sticky='nsew')
		btn_m1.grid(row=1, column=0, sticky='nsew')
		btn_m2.grid(row=1, column=1, sticky='nsew')
		btn_m3.grid(row=1, column=2, sticky='nsew')
		btn_m4.grid(row=1, column=3, sticky='nsew')
		btn_m5.grid(row=1, column=4, sticky='nsew')
		btn_m6.grid(row=1, column=5, sticky='nsew')
		btn_advp.grid(row=0, column=6, sticky='nsew')
		btn_advm.grid(row=1, column=6, sticky='nsew')
		btn_fallp.grid(row=0, column=7, sticky='nsew')
		btn_fallm.grid(row=1, column=7, sticky='nsew')

		style = ttk.Style()
		style.configure(self.style_name, background=self.color)
		print(self.style_name)

		btn1.configure(style=self.style_name)
		btn2.configure(style=self.style_name)
		btn3.configure(style=self.style_name)
		btn4.configure(style=self.style_name)
		btn5.configure(style=self.style_name)
		btn6.configure(style=self.style_name)
		btn_m1.configure(style=self.style_name)
		btn_m2.configure(style=self.style_name)
		btn_m3.configure(style=self.style_name)
		btn_m4.configure(style=self.style_name)
		btn_m5.configure(style=self.style_name)
		btn_m6.configure(style=self.style_name)
		btn_advp.configure(style=self.style_name)
		btn_advm.configure(style=self.style_name)
		btn_fallp.configure(style=self.style_name)
		btn_fallm.configure(style=self.style_name)
