import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def main():
    namen_invullen_en_verifieren()


def namen_invullen_en_verifieren(namen=None):
    event1, values1 = namen_invullen(namen)
    if event1=='klaar':
        namen = values1[0].split(', ')
        event2, values2 = namen_verifieren(namen)
    if event1=='annuleren':
        return None

    if event2=='Nee, opnieuw':
        namen_invullen_en_verifieren(namen=values1[0])

    if event2=='Ja':
        matrix = creeer_mock_matrix(namen)
        fig = creeer_figuur(namen, matrix)
        figuur_laten_zien(fig)


def namen_invullen(namen):
    sg.theme('Neutralblue')     
    layout = [
        [sg.Text('Vul de leerlingnamen kommagescheiden in. Voorbeeld: hans, piet, klaas')],
        [sg.Text('namen', size =(15, 5)), sg.InputText(size=(100,10),default_text=namen)],
        [sg.Submit('klaar'), sg.Cancel('annuleren')]
    ]

    window = sg.Window('Simple data entry window', layout)
    event1, values1 = window.read()
    window.close()
    return event1, values1

def namen_verifieren(namen):
    layout = [[sg.Text(f'Waren dit de #{len(namen)} namen')]]+\
    [[sg.Text(str(i+1) +': '+naam)] for i, naam in enumerate(namen)]+\
    [[sg.Submit('Ja')]]+\
    [[sg.Submit('Nee, opnieuw')]]
    window = sg.Window('Simple data entry window', layout)
    event2, values2 = window.read()
    window.close()
    return event2, values2

def creeer_mock_matrix(namen):
    a = np.random.random((len(namen), len(namen)))*2-1
    np.fill_diagonal(a,0)
    return a

def creeer_figuur(namen, matrix):
    length_longest_naam = max(len(naam) for naam in namen)
    fig, ax = plt.subplots()
    subplot = ax.imshow(matrix, cmap='bwr', interpolation='nearest', aspect='auto')
    subplot.autoscale()
    ax.set_xticks(ticks = range(len(namen)),labels=namen, rotation=90)
    ax.set_yticks(ticks = range(len(namen)),labels=namen)
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

if __name__=='__main__':
    main()