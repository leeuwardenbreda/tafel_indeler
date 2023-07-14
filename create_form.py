
import PySimpleGUI as sg
import time
import pandas as pd

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
