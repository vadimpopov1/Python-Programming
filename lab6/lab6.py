# Лабораторный практикум

# Список с ростом

# rost = []
# while 0 not in rost:
#     n = int(input())
#     rost.append(n)
# rost.remove(0)
#
# for i in range(len(rost)-1):
#     if rost[i] < 0:
#         rost.remove(rost[i])
#
# if len(rost) <= 1:
#     print("Некого сравнивать")
# else:
#     print(f"Самый высокий человек с ростом: {max(rost)}\n"
#           f"Самый низкий человек с ростом: {min(rost)}")

# сумма цифр от 2 до 100

# s = 0
# for i in range(2,100+1):
#     if i % 2 == 0:
#         s += i
# print(s)


# уравнение

# n = int(input())
# y = 0
# for i in range(n+1):
#     y += i**2
# print(y)


# елочка

# n = int(input())
#
# for i in range(n):
#     len = n - i
#     print(len * " " + (i * 2 - 1) * "#")
# print(( n - 1 ) *  " " + "#")

# возраст собаки

# age = int(input("Enter age of dog: "))
# if age >= 0:
#     if age > 2:
#         print((age - 2) * 4 + 21)
#     else:
#         print(age * 10.5)
# else:
#     print("Your num less 0")

# Угадай число

# import random
#
# secret = random.randint(1, 10)
#
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
# print("Хорошо, я загадал число. Попробуй его отгадать")
# numofat = 0
#
# while (not ans):
#     num = int(input(f"Количество твоих попыток: {numofat}. Введи число! "))
#     if num == secret:
#         print(f"Поздравляю! Вы угадали с {numofat+1} попытки!")
#         numofat = 0
#         ans_game()
#     else:
#         numofat += 1
#         if num > secret:
#             print("Нее, ты не угадал. Попробуй снова, но твое число больше загаданого!")
#         else:
#             print("Нее, ты не угадал. Попробуй снова, но твое число меньше загаданого!")

# счастливый билет

# bilet = input("Enter your ticket: ")
# if len(bilet) != 6:
#     print("Incorrect")
# else:
#     if int(bilet[0]) +int(bilet[1]) + int(bilet[2]) == int(bilet[3]) + int(bilet[4]) + int(bilet[5]):
#         print("Your ticket lucky")
#     else:
#         print("Your ticket unlucky")

#  перевод в двоичную

# a = input("Enter number: ")
# print(int(a,2))
