# Напиши программу,
# которая считывает число n,
# после чего считывает n строк
# и выводит только те из них,
# которые написаны без символов в верхнем регистре
# (и в которых есть хотя бы 1 символ в нижнем регистре):
n = int(input())
for i in range(n):
    s = input()
    if s.islower():
        print(s)