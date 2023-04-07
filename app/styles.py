from tkinter import ttk

import config


def create_styles():
    ttk.Style().configure(
        config.ENTRY_STYLE_1,
        fieldbackground=config.ATHLETE_1_COLOR,
        foreground='white',
    )

    ttk.Style().configure(
        config.ENTRY_STYLE_2,
        fieldbackground=config.ATHLETE_2_COLOR,
        foreground='white',
    )

    ttk.Style().configure(
        config.LABEL_STYLE_1,
        background=config.ATHLETE_1_COLOR,
        foreground="white",
        anchor="center",
        font=('Arial', 8, 'bold'),
    )

    ttk.Style().configure(
        config.LABEL_STYLE_2,
        background=config.ATHLETE_2_COLOR,
        foreground="white",
        anchor="center",
        font=('Arial', 8, 'bold'),
    )

    ttk.Style().configure(
        config.FALL_LABEL_STYLE,
        background=config.SPECTATOR_WINDOW_BG,
        foreground="white",
        anchor="center",
        font=('Arial', 26, 'bold'),
    )

    ttk.Style().configure(
        config.SPECTATORS_THEME_DARK,
        background=config.SPECTATOR_WINDOW_BG,
        foreground="#C9C9D2",
    )
    ttk.Style().configure(
        config.FALL_POINTS_STYLE,
        background=config.SPECTATOR_WINDOW_BG,
        foreground="#C9C9D2",
        anchor="center",
        font=('Arial', 18),
    )

    ttk.Style().configure(
        config.SPECTATORS_TIMER_THEME,
        background=config.SPECTATOR_WINDOW_BG,
        font=('Arial', 125, 'bold'),
        foreground=config.SPECTATORS_TIMER_COLOR,
        anchor='n',
    )
