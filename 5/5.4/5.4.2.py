a = 45
b = 131
for i in range(a, b):
    if i % 100 == 39:
        print("Число", i, "оканчивается на 39")
        break
else:
    print("Не получилось найти числа, оканчивающегося на 39 от", a, "до", b - 1)

a = 1
b = 1001
for i in range(a, b):
    if i % 100 == 39:
        print("Число", i, "оканчивается на 39")
        break
else:
    print("Не получилось найти числа, оканчивающегося на 39 от", a, "до", b - 1)

for i in range(10):
    if i == 10:
        print("Цикл завершен преждевременно")
        break
else:
    print("Цикл завершился в штатном режиме")

for i in range(6):
    if i == 3:
        continue
    print(i)

for i in range(10):
    print(i, end=" ")
    continue

for i in range(10):
    continue
    print(i, end=" ")

for i in range(10):
    if i == 4:
        continue
    if i == 7:
        break
    print(i, end=" ")

for i in range(10):
    if i % 2 == 0:
        continue
    if i == 4:
        break
    print(i, end=" ")

for i in range(10):
    if i == 5:
        continue
    print(i, end="")
else:
    print(5)
