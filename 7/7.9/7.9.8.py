# Напиши программу,
# которая считает набор чисел в одной строке,
# и выведет их в отсортированном порядке в одной строке через пробел
# s = sorted(input().split())

print(' '.join(sorted(input().split())))
print(*sorted(input().split()))
