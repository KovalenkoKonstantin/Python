# Напиши программу, которая считывает строку, и выводит все слова из нее каждое в отдельной строчке.
s = input()
l = s.split()
print(*l, sep='\n')
print(*input().split(), sep='\n')
