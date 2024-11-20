# 1
# def convert(str):
#     keys = {
#         '1': ',.?!:',
#         '2': 'abc',
#         '3': 'def',
#         '4': 'ghi',
#         '5': 'jkl',
#         '6': 'mno',
#         '7': 'pqrs',
#         '8': 'tuv',
#         '9': 'wxyz',
#         '0': ' ',
#     }
#     pressed = {}
#     for key, chars in keys.items():
#         for i, char in enumerate(chars):
#             pressed[char] = key * (i + 1)
#     res = []
#     for char in str:
#         if char in pressed:
#             res.append(pressed[char])
#     return ''.join(res)
#
# print("Like nums: " + convert(input("Enter text: ").lower()))

# 2
# import PySimpleGUI as sg
#
# sg.theme('LightGray1')
#
# def convert(word):
#     score = {
#         'a': 1,
#         'e': 1,
#         'i': 1,
#         'l': 1,
#         'n': 1,
#         'o': 1,
#         'r': 1,
#         's': 1,
#         't': 1,
#         'u': 1,
#         'd': 2,
#         'g': 2,
#         'b': 3,
#         'c': 3,
#         'm': 3,
#         'p': 3,
#         'f': 4,
#         'h': 4,
#         'v': 4,
#         'w': 4,
#         'y': 4,
#         'k': 5,
#         'j': 8,
#         'x': 8,
#         'q': 10,
#         'z': 10
#     }
#     total_score = 0
#     for char in word.lower():
#         if char in score:
#             total_score += score[char]
#     return total_score
#
# layout = [
#     [sg.Text('Ваше слово:'), sg.Input(size=10, key='-WORD-')],
#     [sg.Text('Баллы:'), sg.Input(size=24, key='-RESULT-', disabled=True)],
#     [sg.Button('OK'), sg.Button('ВЫЙТИ')]
# ]
#
# window = sg.Window('Игра "Эрудит"', layout)
#
# while True:
#     event, values = window.read()
#     if event in (sg.WINDOW_CLOSED, 'ВЫЙТИ'):
#         break
#     if event == 'OK':
#         your_word = values['-WORD-']
#         if your_word:
#             word_score = convert(your_word)
#             window['-RESULT-'].update(word_score)
#         else:
#             sg.popup_error("Введите слово.")
#
# window.close()

# 3
# emails = {
#     'gryffindor.com': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'k_stepanov'],
#     'hufflepuff.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
#     'hogwarts.com': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
#     'slytherin.com': ['ekaterina_ivanova', 'glebova_nastya'],
#     'ravenclaw.com': ['john.doe', 'mark.zuckerberg', 'helen_hunt']
# }
#
# for domain, user in emails.items():
#     for i in user:
#         print(f"{i}@{domain}")

# 4 GUI
# import PySimpleGUI as sg
# import random
#
# sg.theme('LightGray1')
# def rand(i_from, i_to):
#     if i_from >= i_to:
#         return "Invalid input"
#     else:
#         return random.randint(i_from, i_to)
#
# layout = [[sg.Image(filename='kosti.png', key='-IMAGE-', size=(500, 500))],
#           [sg.Text('Borders of random:')],
#           [sg.Text('From:'), sg.Input(size=10, key='-LOWER-'),sg.Text('To:'), sg.Input(size=10, key='-UPPER-')],
#           [sg.Button('GENERATE',size=(80,2))],
#           [sg.Text('Your rand:'), sg.Input(size=24, key='-RESULT-')],
#           [sg.Button('EXIT', size=(15))]
#           ]
#
# window = sg.Window('Random', layout)
#
# while True:
#     event, values = window.read()
#     if event in (sg.WINDOW_CLOSED, 'EXIT'):
#         break
#     if event == 'GENERATE':
#         lower_bound = int(values['-LOWER-'])
#         upper_bound = int(values['-UPPER-'])
#         random_number = rand(lower_bound, upper_bound)
#         window['-RESULT-'].update(random_number)
# window.close()
