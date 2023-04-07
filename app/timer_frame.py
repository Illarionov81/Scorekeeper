import threading
from tkinter import ttk, Frame

import config


class TimeFrame:
    def __init__(self, master, timer, championship_timer):
        self.master = master
        self.frame = None
        self.timer = timer
        self.championship_timer = championship_timer
        self.started = False
        self.on_pause = False
        self.default_time = 300
        self.time_lock = threading.Lock()
        self.create_frame()

    def create_frame(self):
        self.frame = Frame(self.master)

        # установка начального значения времени
        self.timer.set("{:02d}:{:02d}".format(self.default_time // 60, self.default_time % 60))

        for c in range(4):
            self.frame.columnconfigure(index=c, weight=1)

        for r in range(3):
            self.frame.rowconfigure(index=r, weight=1)

        self.entry_timer = ttk.Entry(self.frame, textvariable=self.timer, font=('Arial', 18), justify='center')
        self.start = ttk.Button(self.frame, text="Start", command=self.start_timer)
        self.reset = ttk.Button(self.frame, text="Reset", command=self.reset_timer)

        mp = ttk.Button(self.frame, text="+1 min", command=lambda: self.change_time(60))
        mm = ttk.Button(self.frame, text="-1 min", command=lambda: self.change_time(-60))
        sec_p = ttk.Button(self.frame, text="+1 sec", command=lambda: self.change_time(1))
        sec_m = ttk.Button(self.frame, text="-1 sec", command=lambda: self.change_time(-1))

        self.entry_timer.grid(row=0, column=0, columnspan=4, sticky='ns')
        self.start.grid(row=1, column=0, rowspan=2, sticky='nsew')
        self.reset.grid(row=1, column=3, rowspan=2, sticky='nsew')
        mp.grid(row=1, column=1, sticky='nsew')
        mm.grid(row=1, column=2, sticky='nsew')
        sec_p.grid(row=2, column=1, sticky='nsew')
        sec_m.grid(row=2, column=2, sticky='nsew')

    def reset_timer(self):
        self.started = False
        self.on_pause = False
        self.start.configure(text='Start')
        self.entry_timer.configure(foreground='black')
        self.championship_timer.configure(foreground=config.SPECTATORS_TIMER_COLOR)
        self.timer.set("{:02d}:{:02d}".format(self.default_time // 60, self.default_time % 60))

    def start_timer(self):
        if not self.started:
            self.started = True
            self.start.configure(text='Pause')
            self.time_ticker()
            return
        if not self.on_pause:
            self.on_pause = True
            self.start.configure(text='Start')
        elif self.on_pause:
            self.on_pause = False
            self.start.configure(text='Pause')

    def time_ticker(self):

        if not self.started:
            return

        if self.on_pause:
            t = self.entry_timer.after(100, self.time_ticker)
            return

        self.change_time(-1)
        t = self.entry_timer.after(1000, self.time_ticker)

    def change_time(self, value):
        t = self.timer.get()
        minutes, seconds = map(int, t.split(':'))
        new_time = minutes * 60 + seconds + int(value)
        if new_time > 0:
            with self.time_lock:
                self.timer.set("{:02d}:{:02d}".format(new_time // 60, new_time % 60))
        elif new_time == 0:
            self.entry_timer.configure(foreground='red')
            self.championship_timer.configure(foreground='red')
            with self.time_lock:
                self.timer.set("{:02d}:{:02d}".format(new_time // 60, new_time % 60))
