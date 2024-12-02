import PySimpleGUI as sg

sg.theme('LightGray1')
def who_win(step):
    if step % 2 == 0:
        sg.popup("Win player 2! (green)", title="Победа")
        with open('logfile.txt', 'a') as f:
            f.write(f"Win player 2! (green) on step: {step+1}\n")
    else:
        sg.popup("Win player 1! (red)", title="Победа")
        with open('logfile.txt', 'a') as f:
            f.write(f"Win player 1! (red) on step: {step+1}\n")


def check_win(matrix):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for condition in win_conditions:
        if matrix[condition[0]] == matrix[condition[1]] == matrix[condition[2]] != 0:
            return True
    return False


def minimax(matrix, depth, is_maximizing):
    if check_win(matrix):
        return -1 if is_maximizing else 1
    if all(cell != 0 for cell in matrix):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if matrix[i] == 0:
                matrix[i] = 'O'
                score = minimax(matrix, depth + 1, False)
                matrix[i] = 0
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if matrix[i] == 0:
                matrix[i] = 'X'
                score = minimax(matrix, depth + 1, True)
                matrix[i] = 0
                best_score = min(score, best_score)
        return best_score


def bot_move(matrix):
    best_score = float('-inf')
    best_move = None

    for i in range(9):
        if matrix[i] == 0:
            matrix[i] = 'O'
            score = minimax(matrix, 0, False)
            matrix[i] = 0
            if score > best_score:
                best_score = score
                best_move = i

    return best_move


layout_choice = [[sg.Text("Выберите режим игры:")],
                 [sg.Button("Игра на двоих"), sg.Button("Игра против компьютера")]]

window_choice = sg.Window('Выбор режима', layout_choice)

mode = None
while True:
    event, values = window_choice.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Игра на двоих":
        mode = "two_players"
        break
    elif event == "Игра против компьютера":
        mode = "vs_computer"
        break

window_choice.close()

if mode is None:
    sg.popup("Режим игры не выбран. Закрытие приложения.")
else:
    layout = [[sg.Text("Step:"), sg.Input(size=3, key="-STEP-", disabled=True),
               sg.Text("           Player's step:"), sg.Input(size=3, key="-PLAYER-", disabled=True)],
              [sg.Button("", size=(2, 2), key=f'button{i}') for i in range(3)],
              [sg.Button("", size=(2, 2), key=f'button{i}') for i in range(3,6)],
              [sg.Button("", size=(2, 2), key=f'button{i}') for i in range(6,9)]]

    matrix = [0] * 9

    window = sg.Window('Крестики-нолики', layout)
    step = 0

    while True:
        event, values = window.read()

        window['-STEP-'].update(step + 1)

        if step % 2 == 0:
            window['-PLAYER-'].update(1)
        else:
            window['-PLAYER-'].update(2)

        if event == sg.WIN_CLOSED:
            break

        if event.startswith('button'):
            button_index = int(event.replace('button', ''))

            if matrix[button_index] == 0:
                # Ход игрока
                matrix[button_index] = 'X' if step % 2 == 0 else 'O'
                window[event].update(text=matrix[button_index],
                                     button_color=('white', 'red' if step % 2 == 0 else 'green'))
                step += 1

                if check_win(matrix):
                    who_win(step)
                    break

                if all(cell != 0 for cell in matrix):
                    sg.popup("Draw!", title="Ничья")
                    break

                if mode == "vs_computer" and step % 2 == 1:
                    bot_index = bot_move(matrix)
                    if bot_index is not None:
                        matrix[bot_index] = 'O'
                        window[f'button{bot_index}'].update(text='O', button_color=('white', 'green'))
                        step += 1

                        if check_win(matrix):
                            who_win(step)
                            break

                        if all(cell != 0 for cell in matrix):
                            sg.popup("Draw!", title="Ничья")
                            with open('logfile.txt', 'a') as f:
                                f.write(f"Draw on step: {step + 1}\n")
                            break

window.close()
