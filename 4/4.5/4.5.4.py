a = True
if a == 1:
    print(True)
else:
    print(False)
# тип bool является подтипом int,
# False равняется 0, а True равняется 1

print(True + False)  # 1
print(True + True + True)  # 3
print(10 * True)  # 10
print(3 + False)  # 3
print(10 // True)  # 10
print(True ** 3)  # 1
print(10 ** False)  # 1

a = 10
a += True
print(a)

print(False % True)
