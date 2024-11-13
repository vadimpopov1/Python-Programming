# 1
# def f(x):
#     return x**2 / (10 + x**3)
#
# def integral(a, b, N):
#     h = (b - a) / N
#     res = (h / 2) * (f(a) + f(b))
#     for i in range(1, N):
#         res += f(a + i * h)
#     res *= h
#     return res
#
# a = 0
# b = 1
# for N in [10, 100, 1000]:
#     result = integral(a, b, N)
#     print(f"Приближенное значение интеграла для N={N}: {result:.6f}")

# 2
# N = int(input("Введите размер магического квадрата (нечетное число): "))
# if N % 2 == 0:
#     print("Размер должен быть нечетным.")
# else:
#     length = N * N
#     mx = [[None for _ in range(N)] for _ in range(N)]
#     l = 0
#     h = N // 2
#     mx[l][h] = 1
#     for i in range(2, length + 1):
#         ll, hh = l, h
#         l = (l + 1) % N
#         h = (h - 1) % N
#         if mx[l][h] is not None:
#             l = ll
#             h = (hh + 1) % N
#         mx[l][h] = i
#     for m in mx:
#         print(' '.join(str(x) if x is not None else ' ' for x in m))

# 3
# n = int(input("Количество сокровищ: "))
# treasure_map = []
# print("Координаты сокровищ: ")
# for i in range(n):
#     t_m_cords = list(map(int, input().split()))
#     treasure_map.append(t_m_cords)
# cords = list(map(int, input("Координаты Александра: ").split()))
# print(treasure_map)
# mn = 1000000
# ii = 0
# for i in range(len(treasure_map)):
#     length = ((treasure_map[i][0]-cords[0])**2+(treasure_map[i][1]-cords[1])**2)**0.5
#     print(length)
#     if length <= mn:
#         mn = length
#         ii = i
# print(treasure_map[ii][0], treasure_map[ii][1])

# 4
# def switch(task):
#     if task == 1:
#         print("Меню:")
#         print("=" * 30)
#         for dish in menu:
#             name = dish[0]
#             ingredients = ", ".join(dish[1])
#             price = dish[2]
#             print(f"Блюдо: {name}")
#             print(f"Ингредиенты: {ingredients}")
#             print(f"Цена: {price} руб.")
#             print("-" * 30)
#         return 1
#
#     elif task == 2:
#         dish_name = input("Введие название блюда: ")
#         print("\n")
#         for dish in menu:
#             if dish[0].lower() == dish_name.lower():
#                 ingredients = ", ".join(dish[1])
#                 price = dish[2]
#                 print("-" * 30)
#                 print(f"Блюдо: {dish[0]}")
#                 print(f"Ингредиенты: {ingredients}")
#                 print(f"Цена: {price} руб.")
#                 print("-" * 30)
#                 return 2
#         print("Блюдо не найдено.")
#         return 2
#
#     elif task == 3:
#         name = input("Введите название нового блюда: ")
#         ingredients = input("Введите ингридиенты нового блюда: ").split(" ")
#         price = int(input("Введите цену нового блюда: "))
#         menu.append([name, ingredients, price])
#         print(f"Блюдо '{name}' добавлено в меню.")
#         return 3
#
#     elif task == 4:
#         dish_name = input("Введие название блюда: ")
#         new_price = int(input("Введите новую цену: "))
#         for dish in menu:
#             if dish[0].lower() == dish_name.lower():
#                 dish[2] = new_price
#                 print(f"Цена блюда '{dish_name}' изменена на {new_price} руб.")
#                 return 4
#         print("Блюдо не найдено.")
#         return 4
#
# menu = [
#     ["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
#     ["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
#     ["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
# ]
#
# while 1:
#     task = int(input("Введите желаемое действие: \n"
#                      "1. - Отобразить все меню. \n"
#                      "2. - Найти блюдо по названию. \n"
#                      "3. - Добавить новое блюдо. \n"
#                      "4. - Изменить цену.\n"
#                      "\n"
#                      "Ваше действие: "))
#     print("\n ")
#     print(switch(task))

# 5
# matrix = [
#     [11, 12, 13, 14],
#     [21, 22, 23, 24],
#     [31, 32, 33, 34]
# ]
#
# n = len(matrix)
# m = len(matrix[0])
# transposed = [[0] * n for _ in range(m)]
# for i in range(n):
#     for j in range(m):
#         transposed[j][i] = matrix[i][j]
# print("Транспонированная матрица:")
# for str in transposed:
#     print(str)

# 6
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# n = len(matrix)
# matrix_s = [[0] * n for _ in range(n)]
# for i in range(n):
#     matrix_s[n-i-1][i] = matrix[i][i]
#     matrix_s[i][i] = matrix[n-1-i][i]
# for i in range(n):
#     for j in range(n):
#         if matrix_s[i][j] == 0:
#             matrix_s[i][j] = matrix[i][j]
# for str in matrix_s:
#     print(str)

# 7
# n = int(input("Введите количество рядов: "))
# m = int(input("Введите количество мест в ряду: "))
# seats = []
# print("Введите информацию о занятости мест (0 - свободно, 1 - занято):")
# for _ in range(n):
#     stroka = list(map(int, input().split()))
#     seats.append(stroka)
# k = int(input("Введите количество билетов в заказе: "))
# cnt = 0
# for stroka in range(n):
#     cur_str = ''.join(map(str, seats[stroka]))
#     if '0' * k in cur_str:
#         print(stroka+1)
#         cnt += 1
#         break
# if cnt == 0:
#     print("Таких мест не найдено.")

# 8
# n = int(input("Введите количество строк: "))
# m = int(input("Введите количество столбцов: "))
# A = [[0] * m for _ in range(n)]
# for j in range(m):
#     A[0][j] = 1
# for i in range(n):
#     A[i][0] = 1
#     for i in range(1, n):
#         for j in range(1, m):
#             A[i][j] = A[i-1][j] + A[i][j-1]
# for stroka in A:
#     for a in stroka:
#         print(f"{a:6}", end=' ')
#     print()
