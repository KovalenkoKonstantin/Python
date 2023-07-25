# Что выведет этот код?

l = [1, 2, 3, 4]
l.append("Hello world")
l.append(6)
print(l)

l = [1, 2, 3, 4]
l.append(5)
del l[4]
print(l)

l = [1, 2, 3, 4]
del l[1]
del l[1]
print(l)
