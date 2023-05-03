# Напиши программу,
# которая считает стоку s,
# и выведет все ее символы с четными индексами (без пробелов, в одной строке).
#
# (Используй циклы)
s = input()
i = 0
n = ""
while i < len(s):
    if i % 2 == 0:
        n += s[i]
    i += 1
print(n)

s = input()
ans = ''
for x in range(0, len(s), 2):
    ans = ans + s[x]
print(ans)

print(input()[::2])
