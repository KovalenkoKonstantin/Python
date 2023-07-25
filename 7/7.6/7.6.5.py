# Напиши программу, которая считает одну строку - набор целых чисел разделенных пробелами и выведет их сумму.
s = input()
l = s.split()
t = 0
# for i in range(len(l)):
#     t += int(l[i])
# print(t)

# print(sum(map(int, input().split())))

for i in l:
    t += int(i)
print(t)
