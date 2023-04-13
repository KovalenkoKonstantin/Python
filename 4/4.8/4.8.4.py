# Напиши программу,
# которая считает координаты двух шахматных слонов,
# и выведет "YES" (без кавычек) если они бьют друг друга,
# и "NO" (без кавычек) в противном случае.
# Два слона бьют друг друга, если находятся на одной диагонали.
# На первых двух строчках вводятся координаты первого слона,
# на третьей и четвертой строчке вводятся координаты второго слона.
# Все координаты - целые числа от 1 до 8 включительно
# Расстояние по x должно быть равно расстоянию по y,
# для того, чтобы слон бил другую фигуру.
import random

a = int(input())
b = int(input())
c = int(input())
d = int(input())
# a = 1
# b = 1
# c = 2
# d = 2
# a = random.randint(1, 8)
# b = random.randint(1, 8)
# c = random.randint(1, 8)
# d = random.randint(1, 8)
# a = 2
# b = 3
# c = 8
# d = 7
# print(a)
# print(b)
# print(c)
# print(d)
if a > c and b > d and a - c == b - d:
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
if abs(x1 - x2) == abs(y1 - y2):
    print("YES")
else:
    print("NO")
