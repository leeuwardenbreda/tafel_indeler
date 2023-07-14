import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import pandas as pd

def main():
    next_action, file_location = start_menu()
    if next_action == "een invulformulier creeëren":
        create_form()
    if next_action == "bevestigen":
        calculations(file_location)


def start_menu():
    sg.theme('Neutralblue')     
    layout = [
        [sg.Text('Bestandslocatie Invulformulier_leerlingverhoudingtabel_xxxxxxx-xxxxxx.xlsx')],
        [sg.Text('names', size =(15, 5)), sg.InputText(size=(100,10),default_text='plak hier de bestandslocatie van een bestaand invulformulier (C:/../invulformulier.xlsx)')],
        [sg.Submit('bevestigen'), sg.Cancel('een invulformulier creeëren'), sg.Cancel('annuleren')]
    ]

    window = sg.Window('Simple data entry window', layout)
    event, values = window.read()
    window.close()
    return event, values


def create_form(prefill_names=None):
    next_action, names_string = fill_in_names(prefill_names)
    if next_action == 'klaar':
        names = names_string[0].split(', ')
        next_action = verify_names(names)
    if next_action == 'annuleren':
        return None

    if next_action == 'Nee, opnieuw':
        create_form(names=values1[0])

    if next_action=='Ja':
        create_table(names)

def calculations(file_location):
    names = ['gijs', 'henk','piet', file_location]
    matrix = create_mock_matrix(names)
    fig = create_figuur(names, matrix)
    figuur_laten_zien(fig)


def fill_in_names(names):
    sg.theme('Neutralblue')     
    layout = [
        [sg.Text('Vul de leerlingnames kommagescheiden in. Voorbeeld: hans, piet, klaas')],
        [sg.Text('namen', size =(15, 5)), sg.InputText(size=(100,10),default_text=names)],
        [sg.Submit('klaar'), sg.Cancel('annuleren')]
    ]

    window = sg.Window('Simple data entry window', layout)
    event1, values1 = window.read()
    window.close()
    return event1, values1

def verify_names(names):
    layout = [[sg.Text(f'Waren dit de #{len(names)} names')]]+\
    [[sg.Text(str(i+1) +': '+naam)] for i, naam in enumerate(names)]+\
    [[sg.Submit('Ja')]]+\
    [[sg.Submit('Nee, opnieuw')]]
    window = sg.Window('Simple data entry window', layout)
    event, values = window.read()
    window.close()
    return event

def create_table(names):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = f'Invulformulier_leerlingverhoudingtabel_{timestr}.xlsx'
    writer = pd.ExcelWriter(filename)
    df = pd.DataFrame(index=names, data=0, columns=['rangschikking'])
    for name in names:
        df.drop(name).to_excel(writer, sheet_name=name)
    writer.close()


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

if __name__=='__main__':
    main()