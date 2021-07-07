# [10, 11, 15, 15, 17, 18, 19, 20, 20, 23, 24, 27, 29, | 33, 38, | 39, 40, 41, 44, 47]
#                                                         ^
# key = 33
from random import randint
from bubble_sort import bubble


def binary(array, key_value, left=0, right=None):
    if right is None:
        right = len(array)

    middle = (left + right) // 2
    while array[middle] != key_value and left <= right:
        if array[middle] < key_value:
            left = middle + 1
        else:
            right = middle - 1

        middle = (left + right) // 2

    return (True, middle) if not (left > right) else (False, middle+1)


lst = [randint(10, 50) for _ in range(20)]
print(lst)
bubble(lst)
print(lst)
key = int(input('Please enter a key value: '))
res = binary(lst, key)
if res[0]:
    print('Value:', key, 'found. Index:', res[1])
else:
    lst.insert(res[1], key)
    print(lst)
