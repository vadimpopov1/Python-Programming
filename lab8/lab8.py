# Лабораторный практикум

# import string
# s = input()
# letters, numbers = [], []
# for i in range(len(s)):
#     if s[i] in string.digits:
#         numbers += s[i]
#     if s[i] in string.ascii_lowercase or s[i] in string.ascii_uppercase:
#         letters += s[i]
# print(letters)
# print(numbers)

# import random
#
# ticket, wticket = [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]
# for i in range(0, 6):
#     ticket[i] = random.randint(0,49)
#     wticket[i] = random.randint(0, 49)
#     i += 1
#
# if wticket == ticket:
#     print("Вы выиграли!")
# else:
#     print(f"{ticket} - Ваш билет\n"
#           f"{wticket} - Выигрышный билет")

# s = input("Введите числа, разделенные пробелами: ")
# s = list(map(int, s.split()))
# s2 = []
# for i in range(1,len(s)):
#     if s[i] > s[i-1]:
#         s2.append(s[i])
# print(s2)

# s = input("Введите числа, разделенные пробелами: ")
# s = list(map(int, s.split()))
# avg = sum(s)/len(s)
# print(f"{avg}")
# upper = ""
# lower = ""
# for i in range(len(s)):
#     if s[i] <= avg:
#         upper += str(s[i])
#         upper += " "
#     else:
#         lower += str(s[i])
#         lower += " "
# print(f"{upper}")
# print(f"{lower}")

# r = int(input("Введите рост Андрея: "))
# s = input("Введите рост остальных: ")
# s = list(map(int, s.split()))
# pos = 1
# for i in s:
#     if i >= r:
#         pos += 1
# print(pos)

# import random
# def flip():
#     return 'O' if random.randint(0,1) == 0 else 'P'
# cnt = 0
# ccnt = 0
# lflip = None
# while ccnt < 3:
#     flip_c = flip()
#     print(flip_c, end = ' ')
#     cnt += 1
#
#     if flip_c == lflip:
#         ccnt += 1
#     else:
#         ccnt = 1
#     lflip = flip_c
#
# print(f"Необходимо {cnt} раз.")

# card = input("Введите номер карты: ")
# if len(card) == 16:
#     s = [int(i) for i in str(card)]
#     s.reverse()
#     sum = 0
#     for i in range(len(s)):
#             if i % 2 == 0:
#                 sum += s[i]
#             else:
#                 d = s[i] * 2
#                 if s[i] * 2 > 9:
#                     d -= 9
#                 sum += d
#     if sum % 10 == 0:
#         print("Корректный номер.")
#     else:
#         print("Некорректный номер.")
# else:
#     print("Некорректный номер.")
#
# c = int(input())
# words = []
# words_correct = []
# for i in range(c):
#     word = input()
#     words.append(word)
#     if len(word) > 10:
#         word = str(word[0]) + str(len(word)-2) + str(word[-1])
#         words_correct.append(word)
#     else:
#         words_correct.append(word)
# for i in range(c):
#     print(words_correct[i])


# n = int(input("Введите количество комнат: "))
# rooms = []
# for i in range(n):
#     p, q = map(int, input("Введите p и q для комнат: ").split())
#     rooms.append((p, q))
# cnt = 0
# for p, q in rooms:
#     if q - p >= 2:
#         cnt += 1
# print(cnt)

# number = [int(digit) for digit in str(4276440013361511)]

# sum1 = 0
# sum2 = 0
# sum3 = 0
# number.reverse()
# for i in range(len(number) -1, -1, -1):

#     pos_from_end = len(number) - i

#     if pos_from_end % 2 == 0:
#         sum1 += number[i]
#     else:
#         a = number[i] * 2
#         if a > 9:
#             a -= 9
#         sum2 += a
# print(number)
# print(sum1)
# print(sum2)
# sum3 = sum1 + sum2
# print(sum3)
# if sum3 % 10 == 0: print("Корректный номер!")
# else: print("Некорректный номер!")
