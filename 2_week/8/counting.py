from collections import Counter

li = [1, 2, 2, 3, 3, 3, 4, 4, 4,4,4]

countings = Counter(li)
print(countings)


# accessing counter elements

print(countings[5])
print(countings[4])