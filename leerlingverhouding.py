import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from create_form import create_form
from calculations import calculations

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



if __name__=='__main__':
    main()