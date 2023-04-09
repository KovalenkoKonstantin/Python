# Напиши программу,
# которая считает 3 строки и выводит их в лексикографическом порядке
i = str(input())
j = str(input())
k = str(input())

print(min(i, j, k),
      min(max(i, j), max(j, k), max(i, k)),
      max(i, j, k),
      sep='\n')
