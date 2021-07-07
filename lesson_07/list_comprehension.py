import random

lst = []

for _ in range(15):
    lst.append(random.randint(10, 50))

print(lst)


lst1 = [0] * 15
print(lst1)

lst2 = [random.randint(10, 50) for _ in range(15)]
print(lst2)

lst3 = []
for num in lst2:
    lst3.append(str(num))

s = ' + '.join(lst3) + ' = ' + str(sum(lst2))
print(s)

s1 = ' + '.join([str(n) for n in lst2]) + ' = ' + str(sum(lst2))
print(s1)

sum_num = sum([int(n) for n in lst3])
print(sum_num)

rows = 5
cols = 6
matrix = [[random.randint(10, 50) for _ in range(cols)] for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end='  ')
    print()
