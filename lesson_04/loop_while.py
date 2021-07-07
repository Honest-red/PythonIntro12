"""
while <condition>:
    operator1
    operator2


break
continue

else:

"""

# a = 11
# while a <= 10:
#     a += 1
#     print(a, end=' ')
#
# print()
#
#
# b = 1
# while True:
#     print(b, end=' ')
#     if b >= 10:
#         break
#     b += 3
# print()

c = 1
while c <= 30:
    if c % 2:
        c += 1
        continue
    print(c, end=' ')
    c += 1

    if c > 23:
        break
else:
    print('After while')











