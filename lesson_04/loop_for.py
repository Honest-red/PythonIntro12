"""
for variable in <collection>:
    operator1
    operator2


for _ in range():
    operator1
    operator2


range(start, stop, step)
range(1, 10, 2)     1 3 5 7 9       <10
range(start, stop)      step=1
range(1, 10)    1 2 3 4 5 6 7 8 9
range(stop)     start=0, step=1
range(10)       0 1 2 3 4 5 6 7 8 9

"""

for var in range(1, 31, 2):
    print(var, end=' ')
print()

for var in range(26):
    print(var, end=' ')
print()

for var in range(5, 26):
    print(var, end=' ')
print()

for s in 'Process finished with exit code 0':
    print(s, end='.')
print()

for _ in range(10):
    print('A', end=' -> ')
print()

i = 1
for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
    print('#', i, ' color of rainbow is ', color, sep='')
    i += 1
