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
		):
		self.master = master
		self.points_1 = points_1
		self.adv_1 = adv_1
		self.fall_1 = fall_1
		self.create_frame()


	def create_frame(self):
		self.frame = Frame(self.master)

		for c in range(16): self.frame.columnconfigure(index=c, weight=1)

		btn1_1 = ttk.Button(self.frame, text="+1", command=lambda *args: click_button(*args, target=self.points_1, set_points=1)).grid(row=0, column=0)
		btn2_1 = ttk.Button(self.frame, text="+2", command=lambda *args: click_button(*args, target=self.points_1, set_points=2)).grid(row=0, column=1)
		btn3_1 = ttk.Button(self.frame, text="+3", command=lambda *args: click_button(*args, target=self.points_1, set_points=3)).grid(row=0, column=2)
		btn4_1 = ttk.Button(self.frame, text="+4", command=lambda *args: click_button(*args, target=self.points_1, set_points=4)).grid(row=0, column=3)
		btn5_1 = ttk.Button(self.frame, text="+5", command=lambda *args: click_button(*args, target=self.points_1, set_points=5)).grid(row=0, column=4)
		btn6_1 = ttk.Button(self.frame, text="+6", command=lambda *args: click_button(*args, target=self.points_1, set_points=6)).grid(row=0, column=5)
		btn_m_1_1 = ttk.Button(self.frame, text="-1", command=lambda *args: click_button(*args, target=self.points_1, set_points=-1)).grid(row=1, column=0)
		btn_m_2_1 = ttk.Button(self.frame, text="-2", command=lambda *args: click_button(*args, target=self.points_1, set_points=-2)).grid(row=1, column=1)
		btn_m_3_1 = ttk.Button(self.frame, text="-3", command=lambda *args: click_button(*args, target=self.points_1, set_points=-3)).grid(row=1, column=2)
		btn_m_4_1 = ttk.Button(self.frame, text="-4", command=lambda *args: click_button(*args, target=self.points_1, set_points=-4)).grid(row=1, column=3)
		btn_m_5_1 = ttk.Button(self.frame, text="-5", command=lambda *args: click_button(*args, target=self.points_1, set_points=-5)).grid(row=1, column=4)
		btn_m_6_1 = ttk.Button(self.frame, text="-6", command=lambda *args: click_button(*args, target=self.points_1, set_points=-6)).grid(row=1, column=5)
		btn_advp_1 = ttk.Button(self.frame, text="+adv", command=lambda *args: click_button(*args, target=self.adv_1, set_points=1)).grid(row=0, column=6)
		btn_advm_1 = ttk.Button(self.frame, text="-adv", command=lambda *args: click_button(*args, target=self.adv_1, set_points=-1)).grid(row=1, column=6)
		btn_fallp_1 = ttk.Button(self.frame, text="+fall", command=lambda *args: click_button(*args, target=self.fall_1, set_points=1)).grid(row=0, column=7)
		btn_fallm_1 = ttk.Button(self.frame, text="-fall", command=lambda *args: click_button(*args, target=self.fall_1, set_points=-1)).grid(row=1, column=7)
