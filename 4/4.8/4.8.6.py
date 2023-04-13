# Напиши программу,
# которая считает координаты двух шахматных ферзей,
# и выведет "YES" (без кавычек) если они бьют друг друга,
# и "NO" (без кавычек) в противном случае.
# Ферзь бьет другую фигуру если находится на одной вертикали,
# горизонтали или диагонали с ней.
# На первых двух строчках вводятся координаты первого ферзя,
# на третьей и четвертой строчке вводятся координаты второго ферзя.
# Все координаты - целые числа от 1 до 8 включительно

import random

a = random.randint(1, 8)
b = random.randint(1, 8)
c = random.randint(1, 8)
d = random.randint(1, 8)
print(a)
print(b)
print(c)
print(d)

# a = 1
# b = 1
# c = 2
# d = 2
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == c or b == d:
    print("YES")
elif a > c and b > d and a - c == b - d:
    print("YES")
elif c > a and d > b and c - a == d - b:
    print("YES")
elif a > c and d > b and a - c == d - b:
    print("YES")
elif c > a and b > d and c - a == b - d:
    print("YES")
else:
    print("NO")

x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")
