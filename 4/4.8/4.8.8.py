# Напиши программу,
# которая считает координаты двух шахматных коней,
# и выведет "YES" (без кавычек) если они бьют друг друга,
# и "NO" (без кавычек) в противном случае.
# Конь ходит (и бьет) буквой "Г"
# На первых двух строчках вводятся координаты первого коня,
# на третьей и четвертой строчке вводятся координаты второго коня.
# Все координаты - целые числа от 1 до 8 включительно
import random

# a = random.randint(1, 8)
# b = random.randint(1, 8)
# c = random.randint(1, 8)
# d = random.randint(1, 8)
# print(a)
# print(b)
# print(c)
# print(d)
a = 1
b = 1
c = 2
d = 3
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (abs(a - c) == 1 and abs(b - d) == 2)\
        or (abs(a - c) == 2 and abs(b - d) == 1):
    print("YES")
else:
    print("NO")
