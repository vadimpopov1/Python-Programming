# Лабораторный практикум

# s = "Довольно распространённая ошибка ошибка – это лишний повтор повтор слова слова Смешно не не правда ли Не нужно портить хор хоровод."
# words = s.split()
# s2 = ""
# for i in range(len(words)-1):
#     if words[i] == words[i+1]:
#         pass
#     else:
#         s2 += words[i]
#         s2 += " "
# if words[len(words)-1] != words[len(words)-2]:
#      s2 += words[len(words)-1]
#
# print(s2)

# s = input("Enter your phrase: ")
# words = s.split()
# if len(words) != 2:
#     print("Incorrect num of words")
# else: print(f"{words[1]} {words[0]}")

# s = input("Enter your word: ")
# s2 = ""
# for i in range(len(s)-1):
#     s2 += s[i]
#     s2 += "."
# s2 += s[-1]
# print(s2)

# plohoy = ["не плохая", "Не плохой", "Не плохая", "Не плохой", "не плоха", "Не плоха"]
# s = input()
# for i in range(6):
#     if plohoy[i] in s:
#         s = s.replace(plohoy[i], "хорошая")
# print(s)

# def vow(line):
#     v = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
#     return sum(1 for char in line if char in v)
#
# def haiku(l):
#     if len(l) != 3:
#         return "Не хайку. Должно быть 3 строки."
#
#     c = [vow(line) for line in l]
#
#     if c == [5, 7, 5]:
#         return "Хайку!"
#     else:
#         return "Не хайку."
# l = []
# for i in range(3):
#     line = input(f"Введите строку {i + 1}: ")
#     l.append(line)
#
# print(haiku(l))
#
# s = input("Enter your word: ")
# s2 = ""
# if len(s) % 2 == 0:
#     a = len(s)//2
#     c = 0
# else:
#     a = (len(s)+1)//2
#     c = 1
# dif = int(input("If you want to shifr print 0, if dishifr 1 "))
# if dif == 1:
#     for i in range(a):
#         s2 += s[2*i]
#     for i in range(a):
#         s2+= s[-2*i-1]
# else:
#     for i in range(a):
#         s2 += s[i]
#         s2 += s[-i-1]
# if c == 1:
#     print(s2[:-c])
# else:
#     print(s2)

# import random
# import string
#
# def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
#     characters = ''
#     if use_uppercase:
#         characters += string.ascii_uppercase
#     if use_lowercase:
#         characters += string.ascii_lowercase
#     if use_digits:
#         characters += string.digits
#     if use_special:
#         characters += string.punctuation
#     if not characters:
#         raise ValueError("Необходимо выбрать хотя бы один тип символов для генерации пароля.")
#
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password
#
# length = int(input("Введите желаемую длину пароля: "))
# use_uppercase = input("Нужны ли заглавные буквы? (да/нет): ").strip().lower() == 'да'
# use_lowercase = input("Нужны ли строчные буквы? (да/нет): ").strip().lower() == 'да'
# use_digits = input("Нужны ли цифры? (да/нет): ").strip().lower() == 'да'
# use_special = input("Нужны ли специальные символы? (да/нет): ").strip().lower() == 'да'
#
# print(f"Ваш пароль: {generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)}")

# s = input("Enter: ")
# scheta = s[-1]
# schetb = s[-3]
# words = s[:-3].split("-")
# if schetb > scheta:
#     print(words[0])
# elif scheta > schetb:
#     print(words[1])
# else:
#     print("Ничья")
