import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def calculations(file_location):
    names = ['gijs', 'henk','piet', file_location]
    matrix = create_mock_matrix(names)
    fig = create_figuur(names, matrix)
    figuur_laten_zien(fig)

def create_mock_matrix(names):
    a = np.random.random((len(names), len(names)))*2-1
    np.fill_diagonal(a,0)
    return a

def create_figuur(names, matrix):
    length_longest_naam = max(len(naam) for naam in names)
    fig, ax = plt.subplots()
    subplot = ax.imshow(matrix, cmap='bwr', interpolation='nearest', aspect='auto')
    subplot.autoscale()
    ax.set_xticks(ticks = range(len(names)),labels=names, rotation=90)
    ax.set_yticks(ticks = range(len(names)),labels=names)
    return fig

def draw_figure(canvas, figure):
   tkcanvas = FigureCanvasTkAgg(figure, canvas)
   tkcanvas.draw()
   tkcanvas.get_tk_widget().pack(side='top', fill='both', expand=0.1)
   return tkcanvas

def figuur_laten_zien(fig):
    layout = [
        [sg.Text('Leerling verhouding matrix')],
        [sg.Canvas(key='-CANVAS-')], 
        [sg.Button('Sluiten')]]

    # layout = [,
    #           [sg.Column(column_layout, scrollable=True,size=100)],
    #          ]

    window = sg.Window('LeerlingVerhoudingMatrix',
                       layout,size=(600,600),
                       finalize=True,
                       element_justification='center',
                       font='Helvetica 18'
            )

    # add the plot to the window
    tkcanvas = draw_figure(window['-CANVAS-'].TKCanvas, fig)
    event3, values3 = window.read()
    window.close()
    return event3, values3