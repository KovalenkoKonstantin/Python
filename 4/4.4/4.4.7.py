# Напиши программу,
# которая считает натуральное число n
# и выведет последнюю цифру факториала этого числа
#
# Запрещается пользоваться циклами
# Факториал натурального числа n -
# это произведение всех целых чисел от 1 до n включительно.
a = int(input())
if a > 4:
    print(0)
elif a == 1:
    print(1)
elif a == 2:
    print(2)
elif a == 3:
    print(6)
else:
    print(4)

from math import factorial
for n in range(1, 30):
    print(factorial(n))
