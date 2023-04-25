for i in range(10):
    print(i)
    if i == 5:
        break

for i in range(10):
    print(i, end=' ')
    break

for i in range(10):
    break
    print(i)

for i in range(1, 20):
    print(i, end=" ")
    if i % 17 == 0:
        break
a = 30
b = 41
for i in range(a, b):
    if not i % 23:
        print(i, "делится на 23")
        break
else:
    print("Среди чисел от 30 до 40 нет чисел, делящихся на 23")

a = 1
b = 1001
for i in range(a, b):
    if not i % 23:
        print(i, "делится на 23")
        # break
else:
    print("Среди чисел от 30 до 40 нет чисел, делящихся на 23")
