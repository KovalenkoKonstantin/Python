# Мику считает красивыми положительные числа,
# в которых есть и цифра 3, и цифра 9,
# а всего цифр не более 4.
#
# Напиши программу,
# которая считает целое (возможно отрицательное) число
# и выведет "YES" (без кавычек),
# если Мику считает число красивым,
# и "NO" (без кавычек), иначе.
# Для того
# чтобы определить есть ли цифра в числе
# можно привести число (и цифру) в строковый тип
# и использовать оператор in
# import random
# a = random.randint(-100000, 100000)
# print(a)
# x = str(a)
x = input()
if len(str(int(x))) > 4:
    print('NO')
elif int(x) < 0:
    print('NO')
elif '3' in str(int(x)) and '9' in str(int(x)):
    print('YES')
else:
    print('NO')

n = input()
if "3" in n and "9" in n and 0 < int(n) < 10000:
    print("YES")
else:
    print("NO")
