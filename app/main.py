from tkinter import *
from tkinter import ttk 


from control_frame import ControlPanel
from timer_frame import TimeFrame
from spectators_window import SpectatorsWindow
from athlete_frame import Athlete_Frame
from styles import Style


if TclVersion < 8.5:
    print(f'Версия Tkinter {TclVersion} не поддерживает стили. Пожалуйста, обновите Tkinter до версии 8.5 или выше.')
else:
    print(f'Версия Tkinter {TclVersion} поддерживает стили.')

class App:
	def __init__(self, master):
		self.master = master
		self.styles = Style()
		self.create_main_frame()
		self.create_variables()
		self.control_panel = ControlPanel(
			self.master,
			self.title_of_spectators_window,
			self.styles.color_1,
			self.styles.color_2,
			self.styles.entry_style_1,
			self.styles.entry_style_2,
			self.styles.label_1_style,
			self.styles.label_2_style,
			self.name_1,
			self.club_1,
			self.points_1,
			self.fall_1,
			self.adv_1,
			self.name_2,
			self.club_2,
			self.points_2,
			self.fall_2,
			self.adv_2,
			self.timer,
			)
		self.spectators_window = SpectatorsWindow(
			self.master,
			self.title_of_spectators_window,
			self.styles.color_1,
			self.styles.color_2,
			self.styles.label_1_style,
			self.styles.label_2_style,
			self.styles.fall_point_style,
			self.styles.dark,
			self.name_1,
			self.club_1,
			self.points_1,
			self.fall_1,
			self.adv_1,
			self.name_2,
			self.club_2,
			self.points_2,
			self.fall_2,
			self.adv_2,
			self.control_panel.stage_val,
			self.control_panel.group_val,
			self.control_panel.belt_val,
			self.timer,
			self.control_panel.flag_path_1_for_spectators,
			self.control_panel.flag_path_2_for_spectators,
			 )
		self.spectators_timer = self.spectators_window.spectators_timer
		self.time_frame = TimeFrame(self.master, self.timer, self.spectators_timer)

		self.athlete_1 = Athlete_Frame(
			self.master,
			self.points_1,
			self.adv_1,
			self.fall_1,
			self.styles.color_1,
			self.styles.button_style_1,
			)
		self.athlete_2 = Athlete_Frame(
			self.master,
			self.points_2,
			self.adv_2,
			self.fall_2,
			self.styles.color_2,
			self.styles.button_style_2,
			)
		self.frame_placement()

	def create_main_frame(self):
		icon = PhotoImage(file = "./../img/icons/ickon.png")
		self.master.iconphoto(False, icon)
		self.master.title("Carpe Diem")
		self.master.configure(bg='#A09DA5')
		self.master.geometry("740x480")
		self.master.resizable(True, True)
		
	def create_variables(self):
		self.title_of_spectators_window = StringVar(self.master, value='Соревнования по ....')
		self.name_1 = StringVar(self.master, value='NAME OF SPORTSMAN 1')
		self.club_1 = StringVar(self.master, value='SPORT CLUB NAME 1')
		self.points_1 = IntVar(self.master, value=0)
		self.fall_1 = IntVar(self.master, value=0)
		self.adv_1 = IntVar(self.master, value=0)

		self.name_2 = StringVar(self.master, value='NAME OF SPORTSMAN 1')
		self.club_2 = StringVar(self.master, value='SPORT CLUB NAME 2')
		self.points_2 = IntVar(self.master, value=0)
		self.fall_2 = IntVar(self.master, value=0)
		self.adv_2 = IntVar(self.master, value=0)

		self.timer = StringVar(self.master, value='00:00')

	def frame_placement(self):
		for i in range(6):
			self.master.grid_rowconfigure(i, weight=1)

		self.master.grid_columnconfigure(0, weight=1)

		self.master.rowconfigure(index=0, weight=18, uniform="row1")
		self.master.rowconfigure(index=1, weight=6, uniform="row1")
		self.master.rowconfigure(index=2, weight=20, uniform="row1")
		self.master.rowconfigure(index=3, weight=28, uniform="row1")
		self.master.rowconfigure(index=4, weight=14, uniform="row1")
		self.master.rowconfigure(index=5, weight=14, uniform="row1")

		self.control_panel.general_info_frame.grid(row=0, column=0, sticky='nsew')
		self.control_panel.flag_choice_frame.grid(row=1, column=0, sticky='nsew')
		self.control_panel.sportsman_frame.grid(row=2, column=0, sticky='nsew')
		self.time_frame.frame.grid(row=3, column=0, sticky='nsew')
		self.athlete_1.frame.grid(row=4, column=0, sticky='nsew')
		self.athlete_2.frame.grid(row=5, column=0, sticky='nsew')


if __name__ == '__main__':
	root = Tk()
	app = App(root)
	root.mainloop()
