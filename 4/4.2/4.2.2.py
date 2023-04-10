# Напиши программу,
# которая считывает число и выводит "YES",
# если оно оканчивается на 39, и "NO" иначе.
# a = 12339
# print(a % 100)
if int(input()) % 100 == 39:
    print('YES')
else:
    print('NO')

print('YES' if input()[-2:] == '39' else 'NO')
