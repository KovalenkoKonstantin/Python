# В первых 2 строчках указаны координаты ладьи,
# а в третьей и четвертой строках написаны координаты коня.
# Напишите программу, которая считает координаты ладьи и коня,
# и выведет "Конь бьет ладью" (без кавычек),
# если конь бьет ладью,
# "Ладья бьет коня" (без кавычек),
# если ладья бьет коня.
# Если никто никого не бьет программа должна вывести
# "Нет насилию" (без кавычек)
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
c = 8
d = 8

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

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (abs(a - c) == 1 and abs(b - d) == 2) \
        or (abs(a - c) == 2 and abs(b - d) == 1):
    print("Конь бьет ладью")
elif a == c or b == d:
    print("Ладья бьет коня")
else:
    print("Нет насилию")
