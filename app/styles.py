from tkinter import ttk


class Style:
	def __init__(
		self,
	):
		self.set_styles_name()
		self.create_all_styles()

	def set_styles_name(self):
		self.color_1 = '#CC443E'
		self.color_2 = '#2A4EB9'
		self.button_style_1 = '1.TButton'
		self.button_style_2 = '2.TButton'
		self.entry_style_1 = '1.TEntry'
		self.entry_style_2 = '2.TEntry'
		self.label_1_style = 'label_1.TLabel'
		self.label_2_style = 'label_2.TLabel'
		self.fall_point_style = 'label_3.TLabel'
		self.dark = 'label_4.TLabel'
		self.additional_points_style = 'label_5.TLabel'

	def create_all_styles(self):
		ttk.Style().configure(
			self.entry_style_1,
			fieldbackground=self.color_1,
			foreground='white',
			)

		ttk.Style().configure(
			self.entry_style_2,
			fieldbackground=self.color_2,
			foreground='white',
			)

		ttk.Style().configure(
			self.label_1_style,
			background=self.color_1,
			foreground="white",
			anchor="center",
			font=('Arial', 8, 'bold'),
			)

		ttk.Style().configure(
			self.label_2_style,
			background=self.color_2,
			foreground="white",
			anchor="center",
			font=('Arial', 8, 'bold'),
			)

		ttk.Style().configure(
			self.fall_point_style,
			background='#33313B',
			foreground="white",
			anchor="center",
			font=('Arial', 26, 'bold'),
			)

		ttk.Style().configure(
			self.dark,
			background='#33313B',
			foreground="#C9C9D2",
			)
		ttk.Style().configure(
			self.additional_points_style,
			background='#33313B',
			foreground="#C9C9D2",
			anchor="center",
			font=('Arial', 18),
		)
