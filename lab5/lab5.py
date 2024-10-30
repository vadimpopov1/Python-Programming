# лабораторная работа

# sec = int(input("Seconds: "))
# min = int(input("Minutes: "))
# hours = int(input("Hours: "))
# days = int(input("Days: "))
# print("Sum seconds:", sec + min * 60 + hours * 3600 + days * 24 * 3600)

# последние K цифр от числа
#
# N = input()
# K = int(input())
# print(N[len(N)-K:])

# сумма чисел

# N = int(input())
# print(N % 10 + N // 10 % 10 + N // 100)

# Игра "Царство драконов"
# ans = bool
#
# def ans_game():
#     global ans
#     r = input("Желаете переиграть? (Да/Нет)\n")
#     if r == "Да":
#         ans = False
#     if r == "Нет":
#         ans = True
#
# ans = False
#
# while (not ans):
#     print("Вы находитесь в землях, заселенных драконами. Перед собой вы видите две пещеры. \n"
#         "В одной из них — дружелюбный дракон, который готов поделиться с вами своими сокровищами. \n"
#         "Во второй — жадный и голодный дракон, который мигом вас съест.\n"
#         "В какую пещеру вы войдете? (нажмите клавишу 1 или 2)")
#     c1 = int(input())
#     if c1 == 1:
#         print("Вы приближаетесь к пещере... \n"
#                         "Ее темнота заставляет вас дрожать от страха...\n"
#                         "Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и делится с вами своими сокровищами!")
#     elif c1 == 2:
#         print("Вы приближаетесь к пещере... \n"
#                         "Ее темнота заставляет вас дрожать от страха...\n"
#                         "Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и моментально вас съедает!")
#     print(" ")
#     ans_game()

# про треугольники

# a = int(input("Input 1 side of triangle: "))
# b = int(input("Input 2 side of triangle: "))
# c = int(input("Input 3 side of triangle: "))

# if a + b > c and a + c > b or c + b > a and a != 0 and b != 0 and c != 0:
#     if a == b or b == c or a == c:
#         if a == b == c:
#             print("Равносторонний")
#         else:
#             print("Равнобедренный")
#     else:
#         print("Разносторонний")
# else:
#     print("Такого быть не может")

# про месяцы и дни в них

# days_30 = ["April", "June", "September", "November"]
# days_31 = ["January", "March", "May", "July", "August", "October", "Decebmer"]
# days_other = ["February"]
# month = input("Print month: ")
# if month in days_30:
#     print(month, "got 30 days")
# elif month in days_31:
#     print(month, "got 31 days")
# else:
#     print(month, "got 28 or 29 days")

# номерные знаки
# def isdigit(numofcar):
#     if len(number) == 6 and number[:3].isalpha() and number[:3].isupper() and number[4:].isdigit():
#         return "It is old number"
#     elif len(number) == 7 and number[:4].isdigit() and number[4:].isalpha() and number[4:].isupper():
#         return "It is a new format"
#     else:
#         return "Other format"
#
#
# number = input("Print car number: ")
# print(isdigit(number))
