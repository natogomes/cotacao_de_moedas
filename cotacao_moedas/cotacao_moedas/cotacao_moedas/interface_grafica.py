import PySimpleGUI as sg
from moedas import moedas


def win_inicial():
    """
    -> Cria a janela do programa.
    :return: Sem retorno
    """
    sg.theme('DarkTeal12')

    layout = [
        [sg.Image('cotacao de moedas.png', pad=(7, 5))],
        [sg.Text('De:', font='arial 12', )],
        [sg.InputCombo(moedas, font='arial 12', key='moeda_ent', pad=(5, (0, 10)))],
        [sg.Text('Para:', font='arial 12')],
        [sg.InputCombo(moedas, 'Real brasileiro', font='arial 12', key='moeda_sai', pad=(5, (0, 30)))],
        [sg.Button('Pesquisar', font='arial 12 bold', size=(10, 1), pad=(145, 10))],
        [sg.Output(font='arial 12 bold', size=(42, 4), key='saida')],
        [sg.Button('Sair', font='arial 12', size=(6, 1), pad=(167, 20))]
    ]

    inicial = sg.Window('Cotação de Moedas', layout=layout, size=(430, 400), finalize=True)
