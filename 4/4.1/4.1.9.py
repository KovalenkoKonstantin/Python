# У Сакуры было n конфет,
# которые она хочет подарить m своим друзьям,
# чтобы каждому досталось поровну.
# "Лишние" конфеты Сакура съест.
# Напишите программу,
# которая выведет сколько конфет съест Сакура,
# или строку "Лишних конфет не осталось :(" (без кавычек),
# если ей не удастся поесть конфет.
#
# Числа n и m вводятся каждое на своей строчке.
# n = 53
# m = 10
n = int(input())
m = int(input())
if n % m == 0:
    print('Лишних конфет не осталось :(')
else:
    print(n % m)

print(int(input()) % int(input()) or 'Лишних конфет не осталось :(')
