# Напиши программу,
# которая переведет число,
# записанное в системе счисления с основанием b,
# в десятичную систему счисления
# На первой строчке вводится целое число b,
# не более 10 - основание системы счисления
# На второй строчке вводится строка
# - число записанное в системе счисления n
b = 2
n = '101'
# b = int(input())
# n = input()

print(len(n))

for i in range(len(n)):


    def convert_to(number, base, upper=False):
        digits = '0123456789abcdefghijklmnopqrstuvwxyz'
        if base > len(digits): return None
        result = ''
        while number > 0:
            result = digits[number % base] + result
            number //= base
        return result.upper() if upper else result