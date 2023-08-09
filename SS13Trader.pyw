import PySimpleGUI as sg
from math import ceil

def name(name):
        return sg.Text(name + ' - ')

def getValue(value,mult):
    return ceil(float(value)*float(mult))

layout = [
    [sg.Input(key="NumInput"),sg.Button("Calculate",key="Calc",bind_return_key=True)],
    [name("Random"),sg.Text(key="RandomL"),sg.VSep(),sg.Text(key="Random")],
    [name("This is my final offer. Can't do better than this.")],
    [sg.HSep()],

    [name("Grag"),sg.Text(key="GragL"),sg.VSep(),sg.Text(key="Grag")],
    [name("FINE. BUT ENOUGH TALK. TRADE NOW OR FORGET IT.")],
    [sg.HSep()],

    [name("Vurdulak"),sg.Text(key="VurdulakL"),sg.VSep(),sg.Text(key="Vurdulak")],
    [name("We will afford you no further leniency. Make the transaction now.")],
    [sg.HSep()],

    [name("Josh"),sg.Text(key="JoshL"),sg.VSep(),sg.Text(key="Josh")],
    [name("That sounds fine enough. You sure you don't want to buy any more broriffic goods?")],
    [sg.HSep()],

    [name("Buford"),sg.Text(key="BufordL"),sg.VSep(),sg.Text(key="Buford")],
    [name("Aight man, but you're really pushing it. Let's make the trade now, yeah?")],
    [sg.HSep()],

    [name("Buford Stoned"),sg.Text(key="BufordSL"),sg.VSep(),sg.Text(key="BufordS")],
    [name("Uh.. shit.. sure! I think? ..fuck. I'm getting a headache.")],
    [sg.HSep()],

    [name("Pianzi"),sg.Text(key="PianziL"),sg.VSep(),sg.Text(key="Pianzi")],
    [name("Well, my good friend. This is my final offer, I'd have to be insane to cut you a better bargain than this!")],
    [sg.HSep()],

    [sg.Button("Quit",key="Close")]
]

window = sg.Window("Trader Menu",layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Close":
        break
    if event == "Calc":
        value = values["NumInput"]
        print(value)

        window["Random"].update(getValue(value,1.2))
        window["RandomL"].update(getValue(value,0.8))

        window["Grag"].update(getValue(value,1.15))
        window["GragL"].update(getValue(value,0.85))

        window["Vurdulak"].update(getValue(value,1.10))
        window["VurdulakL"].update(getValue(value,0.9))

        window["Josh"].update(getValue(value,1.15))
        window["JoshL"].update(getValue(value,0.85))

        window["Buford"].update(getValue(value,1.3))
        window["BufordL"].update(getValue(value,0.7))

        window["BufordS"].update(getValue(value, 1.95))
        window["BufordSL"].update(getValue(value, 0.05))

        window["Pianzi"].update(getValue(value,1.33))
        window["PianziL"].update(getValue(value,0.67))

window.close()
