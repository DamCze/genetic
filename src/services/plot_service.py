import tkinter as tk

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use('TkAgg')


def set_up_primary_plot(x, fx, fxstd, fxaverage, label):
    plt2.clf()
    plt2.cla()
    plot_basis = tk.Tk()
    fig = plt2.figure(1, dpi=80, figsize=(12, 12))
    plt2.subplot(221)
    plt2.plot(x, fx)
    plt.title('Wartość funkcji')
    plt2.subplot(222)
    plt2.plot(x, fxstd)
    plt.title('Odchylenie standardowe')
    plt2.subplot(223)
    plt2.plot(x, fxaverage)
    plt.title('Średnia wartość funkcji')
    plt2.xlabel(label)
    canvas = FigureCanvasTkAgg(fig, master=plot_basis)
    plot_widget = canvas.get_tk_widget()
    plot_widget.grid(row=0, column=0)
