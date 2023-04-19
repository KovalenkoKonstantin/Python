# Напиши программу,
# которая считывает n чисел
# и выводит второе по минимальности из них
# (минимальное из всех кроме самого минимального)
# На первой строке вводится целое число n >= 2
#
# На следующих n строках вводится по целому числу.
n = int(input())

m = int(input())
o = int(input())
mi = min(m, o)
ma = max(m, o)

if n == 2:
    print(ma)
elif n > 2:
    for i in range(n - 2):
        r = int(input())
        if r <= mi:
            ma = mi
            mi = r
        elif r <= ma:
            ma = r
    print(ma)
