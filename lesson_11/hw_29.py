from random import randint

M = 9      # rows
N = 9      # cols

lst = [[randint(10, 99) for _ in range(N)] for _ in range(M)]
tmp_lst = [0] * N

# s = 'Value1: {!r}, Value2: {!r}'
# print(s)
# print(s.format(3, 5))
# print(s.format('Hello', 5))
# print(s.format(6, 'Hello'))
#
# s1 = 'Value3: {a}, Value4: {b}, Value5: {c}, Value6: {b}, Value7: {a}, Value8: {b}'
# print(s1.format(b=3, a=5, c=7))
#
# s2 = 'value: "{S:10}"'
# print(s2.format(S=5623))

# tmp = '{:4}'
for i in range(M):
    s = 0
    for j in range(N):
        # print(tmp.format(lst[i][j]), end='')
        print(lst[i][j], end='\t')
        s += lst[i][j]
        tmp_lst[j] += lst[i][j]
    print('\t', s)
print()

for value in tmp_lst:
    # print(tmp.format(value), end='')
    print(value, end='\t')
print()

