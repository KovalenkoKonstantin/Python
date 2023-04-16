# Напиши программу,
# которая определяет объявлен ли шах королю, или нет
# В первых двух строчках вводятся координаты короля
# В третьей и четвертой строчках вводятся координаты
# вражеской фигуры
# В пятой строчке вводится тип вражеской фигуры:
# строка "конь", "слон", "ладья", "ферзь" или "пешка"
# (все строки вводятся без кавычек)#
# Программа должна выводить строку "Шах!" (без кавычек),
# если королю объявлен шах (если вражеская фигура бьет короля).
# Если королю не объявлен шах, то выводить ничего не нужно.
# Считать что король черный,
# а вражеская фигура - белая
# (это важно, если вражеская фигура - пешка
# (пешки ходят вверх, т. е. их первая координата уменьшается))
import random

a = random.randint(1, 8)
b = random.randint(1, 8)
c = random.randint(1, 8)
d = random.randint(1, 8)
x = random.randint(1, 5)
if x == 1:
    x = 'конь'
elif x == 2:
    x = 'слон'
elif x == 3:
    x = 'ладья'
elif x == 4:
    x = 'ферзь'
else:
    x = 'пешка'

# a = 5
# b = 5
# c = 6
# d = 4
# x = 'пешка'

print(a)
print(b)
print(c)
print(d)
print(x)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# x = str(input())

if (
        (x == 'ладья' and (a == c or b == d))  # ладья
        or (x == 'конь' and ((abs(a - c) == 1 and abs(b - d) == 2) or (abs(a - c) == 2 and abs(b - d) == 1)))  # конь
        or (x == 'слон' and ((a > c and b > d and a - c == b - d) or (c > a and d > b and c - a == d - b) or (a > c and d > b and a - c == d - b) or (c > a and b > d and c - a == b - d)))  # слон
        or (x == 'ферзь' and (
        (a == c or b == d) or (a > c and b > d and a - c == b - d) or (c > a and d > b and c - a == d - b) or (
        a > c and d > b and a - c == d - b) or (c > a and b > d and c - a == b - d)))  # ферзь
        or (x == 'пешка' and ((a == c - 1 and b == d - 1) or (a == c - 1 and b == d + 1)))  # пешка
):
    print('Шах!')

# pawn
# (a, b) бьет короля на (a-1, b-1) и (a-1, b+1)

# horse
# if (abs(a - c) == 1 and abs(b - d) == 2) \
#         or (abs(a - c) == 2 and abs(b - d) == 1):
#     print("YES")
# else:
#     print("NO")
# # rook
# if a == c or b == d:
#     print("YES")
# else:
#     print("NO")
# elephant
# if (a > c and b > d and a - c == b - d) or (c > a and d > b and c - a == d - b) or (a > c and d > b and a - c == d - b) or (c > a and b > d and c - a == b - d):
#     print("YES")
# else:
#     print("NO")
#  queen
# if (a == c or b == d) or (a > c and b > d and a - c == b - d) or (c > a and d > b and c - a == d - b) or (a > c and d > b and a - c == d - b or (c > a and b > d and c - a == b - d)):
#     print("YES")
# else:
#     print("NO")
