# 1 
# n = int(input())
# if n <= 0:
#     print("Invalid count of people")
#     exit(1)
# name_role = []
# sort = []
# for _ in range(n):
#     name_role.append(list(input().split()))
#
# for j in range(3):
#     for i in range(n):
#         if name_role[i][1] == "woman" and j == 0:
#             sort.append(name_role[i][0])
#         if name_role[i][1] == "child" and j == 0:
#             sort.append(name_role[i][0])
#         elif name_role[i][1] == "man" and j == 1:
#             sort.append(name_role[i][0])
#         elif name_role[i][1] == "captain" and j == 2:
#             sort.append(name_role[i][0])
#
# for i in range(len(sort)):
#     print(sort[i])
# import random

# 2
# n = int(input())
# s = input()
# if len(s) != n:
#     print("Error! Questions and answers more than num!")
# elif s.count("Q") + s.count("A") != len(s):
#     print("Other symbols in str!")
#     exit(1)
# elif s.count("Q") == s.count("A") and s[0] == "Q" and s[-1] == "A":
#     print("+")
# else:
#     print("-")

# 3
# import PySimpleGUI as sg
#
# c_image = [[sg.Image("bio.png")]]
# c_input = [[sg.Text("Введите количество бактерий:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="micro")],
#            [sg.Text("Количество секунд:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="count")],
#            [sg.Text("Результат:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(5, 0), key="res")],
#            [sg.Button("Рассчитать", font="Arial 20")]]
#
# layout = [
#     [sg.Column(c_image), sg.VSeperator(), sg.Column(c_input, justification='right')]
# ]
#
# window = sg.Window("Калькулятор бактерий", layout)
#
# while 1:
#
#     event, value = window.read()
#
#     if event == sg.WIN_CLOSED:
#         break
#
#     micro = int(value["micro"])  #здесь хранится количество бактерий изначально
#     count = int(value["count"])  #здесь хранится количество секунд для которых требуется рассчитать
#     b = random.randrange(5)
#     for i in range(count):
#         micro = micro * 2
#     res = micro + b
#
#     if event == "Рассчитать":
#         window["res"].update(res)
#
# window.close()

# 4
# import PySimpleGUI as sg
#
# def to_binary(n):
#     return bin(n).replace("0b", "").replace("-", "").zfill(8)
#
# def to_inverse_code(n):
#     if n >= 0:
#         return to_binary(n)
#     n = abs(n)
#     binary = to_binary(n)
#     inverse = ''.join('1' if bit == '0' else '0' for bit in binary)
#     return inverse
#
#
# def to_complement_code(n):
#     if n >= 0:
#         return to_binary(n)
#     inverse = to_inverse_code(n)
#     complement = bin(int(inverse, 2) + 1).replace("0b", "")
#     return complement.zfill(8)
#
# sg.theme('LightGray1')
# layout = [
#     [sg.Text('Your value:              '), sg.Input(size=8, key='-VALUE-')],
#     [sg.Text('In binary code:         '), sg.Input(size=8, key='-RESULT_BIN-', disabled=True)],
#     [sg.Text('In inverse code:       '), sg.Input(size=8, key='-RESULT_INV-', disabled=True)],
#     [sg.Text('In complement code:'), sg.Input(size=8, key='-RESULT_COM-', disabled=True)],
#     [sg.Button('SOLVE', size=(11)), sg.Button('EXIT', size=(11))]
# ]
#
# window = sg.Window('Number Code Converter', layout)
#
# while True:
#     event, values = window.read()
#     if event in (sg.WINDOW_CLOSED, 'EXIT'):
#         break
#     if event == 'SOLVE':
#         try:
#             value = int(values['-VALUE-'])  # Преобразуем ввод в целое число
#             if value <= 127 and value >= -128:
#                 binar = bin(value).replace("0b", "").replace("-", "").zfill(8)
#                 binar = binar.replace("0", "2")
#                 binar = binar.replace("1", "0")
#                 binar = binar.replace("2", "1")
#                 inv = to_inverse_code(value)
#                 comp = to_complement_code(value)
#                 window['-RESULT_BIN-'].update(binar)
#                 window['-RESULT_INV-'].update(inv)
#                 window['-RESULT_COM-'].update(comp)
#             else:
#                 sg.popup("Invalid input. Please enter a value between -128 and 127.")
#         except ValueError:
#             sg.popup("Invalid input. Please enter a valid integer.")
#
# window.close()
