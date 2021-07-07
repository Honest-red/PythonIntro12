<<<<<<< HEAD
# for i in range(10):
#     for j in range(15):
#         print(i, j)

rows = 9
cols = 9

for _ in range(rows):
    for _ in range(cols):
        print('*  ', end='')
    print()
print()

for i in range(rows):
    print(i, end='\t')
    for j in range(cols):
        if (i == 0 or j == 0 or i == rows-1 or j == cols-1
            or i == j or j == cols - 1 - i
            or i == rows // 2 or j == cols // 2
        ):
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
print()

"""
 j == cols - 1 - 0
 j == cols - 1 - 1
 j == cols - 1 - 2
 j == cols - 1 - 3
 
"""
=======
# for i in range(10):
#     for j in range(15):
#         print(i, j)

rows = 9
cols = 9

for _ in range(rows):
    for _ in range(cols):
        print('*  ', end='')
    print()
print()

for i in range(rows):
    print(i, end='\t')
    for j in range(cols):
        if (i == 0 or j == 0 or i == rows-1 or j == cols-1
            or i == j or j == cols - 1 - i
            or i == rows // 2 or j == cols // 2
        ):
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
print()

"""
 j == cols - 1 - 0
 j == cols - 1 - 1
 j == cols - 1 - 2
 j == cols - 1 - 3
 
"""
>>>>>>> a281ae2b021d3a3dd0c234e75541aedf9d2e09a6
