from tkinter import *
from tkinter import ttk 


from control_frame import ControlPanel
from timer_frame import TimeFrame
from spectators_window import SpectatorsWindow
from athlete_frame import Athlete_Frame


class App:
	def __init__(self, master):
		self.master = master
		self.main_frame = self.create_main_frame()
		self.create_variables()
		self.spectators_window = SpectatorsWindow(
			self.master,
			self.title_of_spectators_window,
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
			self.stage,
			self.group,
			self.explanation,
			self.timer,
			 )
		self.control_panel = ControlPanel(
			self.master,
			self.title_of_spectators_window,
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
			self.stage,
			self.group,
			self.explanation,
			self.timer,
			)

		self.spectators_timer = self.spectators_window.spectators_timer
		self.time_frame = TimeFrame(self.master, self.timer, self.spectators_timer)

		self.athlete_1 = Athlete_Frame(
			self.master,
			self.points_1,
			self.adv_1,
			self.fall_1,
			)
		self.athlete_2 = Athlete_Frame(
			self.master,
			self.points_2,
			self.adv_2,
			self.fall_2,
			)
		self.frame_placement()


	def create_main_frame(self):
		self.master.geometry("850x300") 
		icon = PhotoImage(file = "./../img/icons/ickon.png")
		self.master.iconphoto(False, icon)
		self.master.title("Carpe Diem")

	def create_variables(self):
		self.title_of_spectators_window = StringVar(self.master, value='Соревнования по ....')
		self.name_1 = StringVar(self.master, value='set name 1')  # TODO add flag choise
		self.club_1 = StringVar(self.master, value='set club')
		self.points_1 = IntVar(self.master, value=0)
		self.fall_1 = IntVar(self.master, value=0)
		self.adv_1 = IntVar(self.master, value=0)

		self.name_2 = StringVar(self.master, value='set name 2')
		self.club_2 = StringVar(self.master, value='club 2')
		self.points_2 = IntVar(self.master, value=0)
		self.fall_2 = IntVar(self.master, value=0)
		self.adv_2 = IntVar(self.master, value=0)

		self.stage = StringVar(self.master, value='final')  # TODO choise field
		self.group = StringVar(self.master, value='boys / 8-10 / newcomers')
		self.explanation = StringVar(self.master, value='новички')
		self.timer = StringVar(self.master, value='00:00')

	def frame_placement(self):
		self.control_panel.frame.grid(row=0, column=0)
		self.time_frame.frame.grid(row=1, column=0)
		self.athlete_1.frame.grid(row=2, column=0)
		self.athlete_2.frame.grid(row=3, column=0)




if __name__ == '__main__':
	root = Tk()
	app = App(root)
	root.mainloop()