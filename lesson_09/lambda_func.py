from random import randint

# lambda x, y, z: x * y + z

func = lambda x, y, z: x * y + z
print(func(2, 4, 5))


# def far(temp):
#     return round(((float(9) / 5) * temp + 32), 2)


tmp = [36.6, 38, 32.8, 41.5, 43]


# f_tmp = []
# for t in tmp:
#     f_tmp.append(far(t))

# print(f_tmp)

# map(func_ref, collection)
# res = list(map(far, tmp))
# print(res)

res1 = list(map(lambda t: round(((float(9) / 5) * t + 32), 2), tmp))
print(res1)

# filter(func_ref, collection)
lst = [randint(10, 90) for _ in range(25)]
print(lst)
even = []
for el in lst:
    if not el % 2:
        even.append(el)

print(even)

res = list(filter(lambda x: not x % 2, lst))
print(res)


lst1 = [0, 1, 2, 3, 4, 5, 6]
lst2 = ['zero', 'one', 'two', 'three', 'four']
lst3 = ['a', 'b', 'c', 'd', 'e']
d2 = {0: ('a', 'zero'), 1: ('b', 'one'), 2: ('c', 'two'), 3: ('d', 'three'), 4: ('e', 'four')}
d = {}
# for i in range(len(lst1)):
#     d[lst1[i]] = lst2[i]

print(d)

d1 = dict(zip(lst1, zip(lst3, lst2)))
print(d1)

d3 = list(zip(lst2, d2))
print(d3)

