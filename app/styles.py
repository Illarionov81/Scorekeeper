from tkinter import *
from tkinter import ttk


class Style:
	def __init__(
		self,
		color_1,
		color_2,
		button_style_1,
		button_style_2,
		entry_style_1,
		entry_style_2,
		label_1_style,
		label_2_style,
	):
		self.color_1_name = color_1
		self.color_2_name = color_2

		self.button_style_1_name = button_style_1
		self.button_style_2_name = button_style_2
		
		self.entry_style_1_name = entry_style_1
		self.entry_style_2_name = entry_style_2

		self.label_1_style_name = label_1_style
		self.label_2_style_name = label_2_style

		self.create_all_styles()

	def create_all_styles(self):
		ttk.Style().configure(
			self.entry_style_1_name,
			fieldbackground=self.color_1_name,
			foreground='white',
			)

		ttk.Style().configure(
			self.entry_style_2_name,
			fieldbackground=self.color_2_name,
			foreground='white',
			)

		ttk.Style().configure(
			self.label_1_style_name,
			background=self.color_1_name,
			foreground="white",
			anchor="center",
			font=('Arial', 8, 'bold'),
			)

		ttk.Style().configure(
			self.label_2_style_name,
			background=self.color_2_name,
			foreground="white",
			anchor="center",
			font=('Arial', 8, 'bold'),
			)
