import PySimpleGUI as sg


layout = [
    [sg.Text("Very Basic Calculator")],
    [sg.Text('A'),sg.InputText(key='alpha', size=(5, 2), do_not_clear=False),sg.Text('B'),sg.InputText(key='beta', size=(5, 2), do_not_clear=False)],
    [sg.Button('+', size=(3, 2)), sg.Button('-', size=(3, 2)), sg.Button('*', size=(3, 2)), sg.Button('/', size=(3, 2))],
    [sg.Cancel()]
    
]

window = sg.Window('Basic Calc', layout=layout)

operations = {
    '+': (lambda x, y:x+y),
    '-': (lambda x, y:x-y),
    '*': (lambda x, y:x*y),
    '/': (lambda x, y:x/y),
}


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel', None): break
    a = int(values['alpha'])
    b = int(values['beta'])
    try:
        result = operations[event](a,b)
    except ZeroDivisionError:
        #sg.popup_error('You tried to divide by zero!')
        result = "ERROR"
    finally:
        sg.popup_auto_close(f"The answer is {result}")
    
    #debug statement
    print(event, values, result)