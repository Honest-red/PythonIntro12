import random

s = {}
print(s, type(s))
s = set()
print(s, type(s))
s = {1, 2, 3, 4, 5}
print(s, type(s))

s = set('Process finished p')
print(s)

s1 = {1, 2, 3, 4}
s2 = {1, 2, 3, 4, 2, 1}
print(s1, s2)
print(s1 == s2)

# s1 = {random.randint(10, 50) for _ in range(10)}
# s2 = {random.randint(10, 50) for _ in range(10)}
# # print(len(s))
# print(s1, s2)
s1 = {34, 35, 20, 37, 45, 12, 14, 27, 31}
s2 = {32, 34, 45, 49, 19, 20, 21, 25, 28, 30}
# len()
# add()
# remove()
# pop()
# clear()
# A | B     A.union(B)
# A |= B    A.update(B)
s3 = s1 | s2
print(s3)

# A & B     A.intersection(B)
# A &= B    A.intersection_update(B)
s3 = s1 & s2
print(s3)

# A - B     A.difference(B)
# A -= B    A.difference_update(B)
s3 = s1 - s2
print(s3)

# A ^ B     A.symmetric_difference(B)
# A ^= B    A.symmetric_difference_update(B)
s3 = s1 ^ s2
print(s3)
s11 = s1 - s2
s22 = s2 - s1
s33 = s11 | s22
print(s33)


fs1 = frozenset(s1)
print(fs1, type(fs1))
fs2 = frozenset(s2)

for el in s1:
    print(el, end='  ')
print()

for el in fs1:
    print(el, end='  ')
print()

fs3 = fs1 | fs2
print(fs3)
print(type(fs3))
fs3 = fs1 | s2
print(fs3)
print(type(fs3))
