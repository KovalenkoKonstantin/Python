# Напиши программу,
# которая считает два целых числа - a и b,
# каждое на своей строке,
# и выведет все числа от a (включительно) до b (не включительно).
# Гарантируется что a < b
a = int(input())
b = int(input())
for i in range(a, b):
    print(i)
