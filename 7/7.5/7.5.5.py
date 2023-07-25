# Что выведет этот код?

l = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l.extend(l2)
print(l)

l = [1, 2, 3]
l2 = ["4", "5", "6"]
l2.extend(l)
print(l2)

l = [1, 2, 3]
l2 = ["4", "5", "6"]
print(l2.extend(l))
