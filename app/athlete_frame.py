from tkinter import ttk, Frame

from utils import click_button


class AthleteFrame:
    def __init__(
            self,
            master,
            points,
            adv,
            fall,
            color,
            style_name,
    ):
        self.master = master
        self.points = points
        self.adv = adv
        self.fall = fall
        self.color = color
        self.frame = None
        self.style_name = style_name
        self.create_frame()

    def create_frame(self):
        self.frame = Frame(self.master)

        for c in range(8):
            self.frame.columnconfigure(index=c, weight=1)

        for r in range(2):
            self.frame.rowconfigure(index=r, weight=1)

        btn1 = ttk.Button(self.frame, text="+1", command=lambda *args: click_button(target=self.points, set_points=1))
        btn2 = ttk.Button(self.frame, text="+2", command=lambda *args: click_button(target=self.points, set_points=2))
        btn3 = ttk.Button(self.frame, text="+3", command=lambda *args: click_button(target=self.points, set_points=3))
        btn4 = ttk.Button(self.frame, text="+4", command=lambda *args: click_button(target=self.points, set_points=4))
        btn5 = ttk.Button(self.frame, text="+5", command=lambda *args: click_button(target=self.points, set_points=5))
        btn6 = ttk.Button(self.frame, text="+6", command=lambda *args: click_button(target=self.points, set_points=6))
        btn_m1 = ttk.Button(self.frame, text="-1",
                            command=lambda *args: click_button(target=self.points, set_points=-1))
        btn_m2 = ttk.Button(self.frame, text="-2",
                            command=lambda *args: click_button(target=self.points, set_points=-2))
        btn_m3 = ttk.Button(self.frame, text="-3",
                            command=lambda *args: click_button(target=self.points, set_points=-3))
        btn_m4 = ttk.Button(self.frame, text="-4",
                            command=lambda *args: click_button(target=self.points, set_points=-4))
        btn_m5 = ttk.Button(self.frame, text="-5",
                            command=lambda *args: click_button(target=self.points, set_points=-5))
        btn_m6 = ttk.Button(self.frame, text="-6",
                            command=lambda *args: click_button(target=self.points, set_points=-6))
        btn_adv_p = ttk.Button(self.frame, text="+adv",
                               command=lambda *args: click_button(target=self.adv, set_points=1))
        btn_adv_m = ttk.Button(self.frame, text="-adv",
                               command=lambda *args: click_button(target=self.adv, set_points=-1))
        btn_fall_p = ttk.Button(self.frame, text="+fall",
                                command=lambda *args: click_button(target=self.fall, set_points=1))
        btn_fall_m = ttk.Button(self.frame, text="-fall",
                                command=lambda *args: click_button(target=self.fall, set_points=-1))

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
        btn_adv_p.grid(row=0, column=6, sticky='nsew')
        btn_adv_m.grid(row=1, column=6, sticky='nsew')
        btn_fall_p.grid(row=0, column=7, sticky='nsew')
        btn_fall_m.grid(row=1, column=7, sticky='nsew')

        style = ttk.Style()
        style.configure(self.style_name, background=self.color)

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
        btn_adv_p.configure(style=self.style_name)
        btn_adv_m.configure(style=self.style_name)
        btn_fall_p.configure(style=self.style_name)
        btn_fall_m.configure(style=self.style_name)
