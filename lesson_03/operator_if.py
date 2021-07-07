"""
if <condition>:
    operator1
    operator2
operator3
"""

a = 4
# if a >= 0:
#     print('Variable is positive')
#
# print('End')

"""
if <condition>:
    operator1
    operator2
else:
    operator3
    operator4
"""

print('Variable is ', end='')
if a >= 0:
    print('positive')
else:
    print('negative')

"""
1000        1%
5000        2%
10000       5%
25000       10%
50000       11%
> 50000     15%

10 <= x <= 100
x >= 10 and x <= 100

"""

# total = int(input('Please enter value: '))
# percentage = 0
# if 0 < total < 1000:
#     percentage = 1
# elif 1000 <= total < 5000:
#     percentage = 2
# elif 5000 <= total < 10000:
#     percentage = 5
# elif 10000 <= total < 25000:
#     percentage = 10
# elif 25000 <= total < 50000:
#     percentage = 11
# else:
#     percentage = 15
#
# print(percentage)

a = -5
s = 'Variable is positive' if a >= 0 else 'Variable is negative'
print(s)
