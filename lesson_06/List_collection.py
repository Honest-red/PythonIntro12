<<<<<<< HEAD
lst = []
print(lst, type(lst))

lst = list()
lst = list('Hello World!')
print(lst)

lst = [2, 7, 4.5, 'Test', True]
print(lst)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l3)

l3 = l1 * 3
print(l3)

# len()
print(len(l3))

# del
del l3[4]
print(l3)
# del l3
# print(l3)
l3.remove(3)
print(l3)

# min(), max(), sum()
print(min(l3))
print(max(l3))
print(sum(l3))

# index()
print(l3.index(2, 2))

# count()
print(l3.count(5))

# pop()
# pop(x)
print(l3)
print(l3.pop())
print(l3)
print(l3.pop(2))
print(l3)

# append()
l3.append(34)
print(l3)

# insert()
l3.insert(3, 4)
print(l3)

# clear()
# l3.clear()
# print(l3)

# extend()
print(l1, l2)
l1.extend(l2)
print(l1, l2)


# revers()
print(l3)
l3.reverse()    # l3[:: -1]
print(l3)

# sort()
print(l3)
l3.sort(reverse=True)
print(l3)

# join()
# split()
s = 'Process    finished    with   exit   code 0'
print(s)
lst = s.split()
print(lst)

s1 = ' <-> '.join(lst)
print(s1)
=======
lst = []
print(lst, type(lst))

lst = list()
lst = list('Hello World!')
print(lst)

lst = [2, 7, 4.5, 'Test', True]
print(lst)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l3)

l3 = l1 * 3
print(l3)

# len()
print(len(l3))

# del
del l3[4]
print(l3)
# del l3
# print(l3)
l3.remove(3)
print(l3)

# min(), max(), sum()
print(min(l3))
print(max(l3))
print(sum(l3))

# index()
print(l3.index(2, 2))

# count()
print(l3.count(5))

# pop()
# pop(x)
print(l3)
print(l3.pop())
print(l3)
print(l3.pop(2))
print(l3)

# append()
l3.append(34)
print(l3)

# insert()
l3.insert(3, 4)
print(l3)

# clear()
# l3.clear()
# print(l3)

# extend()
print(l1, l2)
l1.extend(l2)
print(l1, l2)


# revers()
print(l3)
l3.reverse()    # l3[:: -1]
print(l3)

# sort()
print(l3)
l3.sort(reverse=True)
print(l3)

# join()
# split()
s = 'Process    finished    with   exit   code 0'
print(s)
lst = s.split()
print(lst)

s1 = ' <-> '.join(lst)
print(s1)
>>>>>>> a281ae2b021d3a3dd0c234e75541aedf9d2e09a6
