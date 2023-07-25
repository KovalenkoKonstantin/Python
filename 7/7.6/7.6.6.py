# Напиши программу, которая считает одну строку - набор вещественных чисел разделенных пробелами
# и выведет их среднее арифметическое.
# l = input()
# l = '1.0 2.5 1.5 4.3 0.7'
s = input().split()
t = 0.0
for i in range(len(s)):
    t += float(s[i])
print(t / len(s))

print(sum(map(float, s := input().split())) / len(s))
