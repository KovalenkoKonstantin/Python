# Напиши программу,
# которая переведет число,
# записанное в системе счисления с основанием b,
# в десятичную систему счисления
# На первой строчке вводится целое число b,
# не более 10 - основание системы счисления
# На второй строчке вводится строка
# - число записанное в системе счисления n

# генератор случайных числовых строк от 1 до 10
import random

# import string
#
# length = random.randint(1, 10)
# def generate_random_string(length):
#     digits = string.digits
#     rand_string = ''.join(random.sample(digits, length))
#     print("Random string of length", length, "is:", rand_string)
#
# generate_random_string(length)


b = 5
# b = random.randint(1, 10)
# print('основание - ' + str(b))

n = '101'
# n = rand_string = ''.join(random.sample(string.digits, length))
# print('случайное строковое число - ' + str(n))
# print('длина случайного строкового числа - ' + str(len(n)))
# print('число - ' + str(n))
# print('длина числа - ' + str(len(n)))
# b = int(input())
# n = input()
a = len(n)-1
x = 0
if b == 0:
    print(0)
elif b > 0:
    for char in n:
        # print(char)
        for j in range(a, a - 1, - 1):  # обратный порядок
            print(char + " " + str(j))
            # x += int(char) * pow(b, j)
            # x += pow((int(char) * b), j)
            x += int(char) * b ** j
            # print(pow(b, j) * int(char))
        a -= 1
    print(int(x))
else:
    for char in n:
        # print(char)
        for j in range(a, a - 1, - 1):  # обратный порядок
            print(char + " " + str(j))
            # x += int(char) * pow(b, j)
            # x += pow((int(char) * b), j)
            x += int(char) * b ** abs(j)
            # print(pow(b, j) * int(char))
        a -= 1
    print(int(x))

# for i in range(len(n)):
#     print(n)

# for i, x in enumerate(range(len(n), 0, -1)):
#     print((i, x))

# for k in (range(0, b + 1)):  # прямой порядок
#     print(k)
# print('обратный порядок основания')
# for j in range(b, -1, -1):  # обратный порядок
#     print(j)

# for k in reversed(range(0, b + 1)):  # обратный порядок
#     print(k)
# print('вычисление')
# for j in range(b, -1, -1):
#     print((int(n) * b) ** j)
# print(pow((int(n) * b), j))  # с использованием метода

b = int(input())
n = input()
x = 0
a = len(n)-1
if b == 0:
    print(0)
elif b > 0:
    for char in n:
        for j in range(a, a - 1, - 1):  # обратный порядок
            x += int(char) * b ** j
        a -= 1
    print(int(x))
else:
    for char in n:
        for j in range(a, a - 1, - 1):  # обратный порядок
            x += int(char) * b ** abs(j)
        a -= 1
    print(int(x))

    b = int(input())
    print(int(input(), b))
