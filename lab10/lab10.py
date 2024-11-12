#  1
# file = open("file4.txt", "r")
#
# winner, prizer = " "," "
# mx_res, mx2_res = 0, 0
#
# for i in file:
#     if int(i.split()[2]) >= mx_res:
#         mx2_res = mx_res
#         prizer = winner
#         mx_res = int(i.split()[2])
#         winner = i
#     if int(i.split()[2]) >= mx2_res and int(i.split()[2]) != mx_res:
#         mx2_res = int(i.split()[2])
#         prizer = i
#
# print(f"Победитель - {winner}Призер - {prizer}")

# 2
# def search(file):
#     cnt = 0
#     mxcnt = 0
#     for i in file:
#         cnt += 1
#         if i == "Academy":
#             mxcnt = cnt
#     if mxcnt != 0:
#         return f"Слово найдено в файле на позиции {mxcnt}."
#     else:
#         return "Не найдено."
#
# file5 = open("file5.txt", "r").read().split()
# file6 = open("file6.txt", "r").read().split()
# print(search(file5))
# print(search(file6))

# 3
# file = open("file6.txt", "r").read().split()
# cnt = 0
# slova = 0
# for i in file:
#     if "e" in i:
#         cnt += 1
#     slova += 1
# print(f"Всего слов содержащих символ 'e' - {cnt}. Всего слов - {slova}. \n"
#       f"Процентное содержание этих слов на весь файл - {str(cnt/slova*100)[:5]}%")

# 4
# file7 = open("file7.txt", "r")
# file8 = open("file8.txt", "r")
# n = int(input("Введите количество имен: "))
# p = input("Какие имена вы хотите (м/ж): ").lower()
# res = []
# cnt = 0
# if n <= 0:
#     print("Неверное количество.")
#     cnt = -1
# if p == "ж":
#     file = file7
# elif p == "м":
#     file = file8
# else:
#     print("Введите правильный пол.")
#     cnt = -1
#
# if cnt >= 0:
#     for i in file:
#         cnt += 1
#         if cnt <= n:
#             res.append(i.split()[0])
#         else:
#             break
#     print(" \n".join(res))

# 5
# def newline(filename, stroka):
#     with open(filename, "r") as file:
#         lines = file.readlines()
#     mi = len(lines) // 2
#     lines.insert(mi, stroka + "\n")
#     with open(filename, "w") as file:
#         file.writelines(lines)
# stroka = input("Введите нужную строку: ")
# newline('file3.txt', stroka)

# 6
# file = input().split()
# file = open("file6rev.txt", "r").read().split()
# file = open("file6.txt", "r").read().split()
# res = []
# for i in file:
#     res.append(i[::-1])
# print(" ".join(res))

# 7
# import random
# def genpass(file):
#     with open(file, 'r') as file:
#         words = [line.strip() for line in file if len(line.strip()) >= 3]
#     while True:
#         word1 = random.choice(words)
#         word2 = random.choice(words)
#         password = word1.capitalize() + word2.capitalize()
#         if 8 <= len(password) <= 10:
#             break
#     return password
#
# file = 'words.txt'
# password = genpass(file)
# print("Пароль:", password)

# 8
# n, m = map(int, input().split())
# matrix = [['.' for _ in range(m)] for _ in range(n)]
# cnt = 0
# for j in range(n):
#     if j % 2 == 0 or j == 0:
#         for i in range(m):
#             matrix[j][i] = "#"
#     elif j % 2 != 0:
#         if cnt % 2 == 0:
#             matrix[j][m-1] = "#"
#             cnt += 1
#         else:
#             matrix[j][0] = "#"
#             cnt += 1
#
# for row in matrix:
#     print(''.join(row))
