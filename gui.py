from tkinter import *
from gui_functions import *
from cube_graph import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)


NOISE = 0
LIVING_REWARD = 0
GAMMA = 0.9
ALPHA = 0.1
EPSILON = 0.1

root = Tk()


def under_construction():
    return 0


main_menu = Menu(root)

file_menu = Menu(main_menu)
file_menu.add_command(label="New", command=under_construction)
file_menu.add_command(label="Open", command=under_construction)
file_menu.add_command(label="Save", command=under_construction)
file_menu.add_command(label="Save as...", command=under_construction)
file_menu.add_command(label="Close", command=under_construction)

file_menu.add_separator()

file_menu.add_command(label="Exit", command=root.quit)
main_menu.add_cascade(label="File", menu=file_menu)

root.config(menu=main_menu)

Label(root, text="noise: ").grid(row=0)
noise_input = Entry(root).grid(row=0, column=1)
Label(root, text='living reward: ').grid(row=1)
living_reward_input = Entry(root).grid(row=1, column=1)
Label(root, text='gamma: ').grid(row=2)
gamma_input = Entry(root).grid(row=2, column=1)
Label(root, text='alpha: ').grid(row=3)
alpha_input = Entry(root).grid(row=3, column=1)
Label(root, text='epsilon: ').grid(row=4)
epsilon_input = Entry(root).grid(row=4, column=1)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().grid()

run = Button(root, text="OK", command=run_learning)
run.grid()
root.mainloop()

