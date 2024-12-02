import PySimpleGUI as sg

def who_win(step):
    if step % 2 == 0:
        sg.popup("Win player 2! (green)", title="Победа")
        with open('logfile.txt', 'a') as f:
            f.write(f"Win player 2! (green) on step: {step+1}\n")
    else:
        sg.popup("Win player 1! (red)", title="Победа")
        with open('logfile.txt', 'a') as f:
            f.write(f"Win player 1! (red) on step: {step+1}\n")
def check_win(matrix, step):
    if matrix[0] == matrix[4] == matrix[8] and matrix[0] in ["X", "O"]:
        who_win(step)
        return True
    elif matrix[2] == matrix[4] == matrix[6] and matrix[2] in ["X", "O"]:
        who_win(step)
        return True
    for i in [0, 1, 2]:
        if matrix[i * 3] == matrix[i * 3 + 1] == matrix[i * 3 + 2] and matrix[i * 3] in ["X", "O"]:
            who_win(step)
            return True
    for i in [0, 1, 2]:
        if matrix[i] == matrix[i + 3] == matrix[i + 6] and matrix[i] in ["X", "O"]:
            who_win(step)
            return True
    if (matrix[0] == matrix[4] == matrix[8] and matrix[0] in ["X", "O"]) or (matrix[2] == matrix[4] == matrix[6] and matrix[2] in ["X", "O"]):
        who_win(step)
        return True
    return False

sg.theme('LightGray1')
layout = [[sg.Text("Step:"), sg.Input(size = 3, key = "-STEP-", disabled=True, text_color="white"), sg.Text("           Player's step:"), sg.Input(size = 3, key = "-PLAYER-", disabled=True, text_color="white")],
    [sg.Button("", size=(2, 2), key=f'button{i}') for i in range(3)],
    [sg.Button("", size=(2, 2), key=f'button{i}') for i in range(3, 6)],
    [sg.Button("", size=(2, 2), key=f'button{i}') for i in range(6, 9)]
]

matrix = [0, 0, 0,
          0, 0, 0,
          0, 0, 0]

window = sg.Window('Крестики-нолики', layout)
step = 0

while True:
    event, values = window.read()

    window[('-STEP-')].update(step + 1)

    if step % 2 == 0:
        window[('-PLAYER-')].update(1)
    else:
        window[('-PLAYER-')].update(2)

    if event == sg.WIN_CLOSED:
        break

    if event.startswith('button'):
        button_index = int(event.replace('button', ''))

        if matrix[button_index] == 0:
            if step % 2 == 0:
                window[event].update(text='X', button_color=('white', 'red'))
                matrix[button_index] = 'X'
            else:
                window[event].update(text='O', button_color=('white', 'green'))
                matrix[button_index] = 'O'

            print(matrix)
            step += 1

            if check_win(matrix, step):
                break

            if 0 not in matrix:
                sg.popup("Draw!", title="Ничья")
                with open('logfile.txt', 'a') as f:
                    f.write(f"Draw on step: {step+1}\n")
                break
window.close()
