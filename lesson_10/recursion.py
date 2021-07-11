import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(200)
print(sys.getrecursionlimit())


def i_pow(num, base):
    res = 1
    while base > 0:
        res *= num
        base -= 1

    return res


print(i_pow(2, 4))


def r_pow(num, base):
    if base == 0:
        return 1

    return num * r_pow(num, base-1)


print(r_pow(2, 4))


def i_fib(num):
    x0 = 0
    x1 = 1
    while num > 0:
        y = x0 + x1
        x0 = x1
        x1 = y
        num -= 1

    return x0


print(i_fib(9))


def r_fib(num):
    # if 0 <= num <= 1:
    #     return num
    #
    # return r_fib(num-2) + r_fib(num-1)
    return num if 0 <= num <= 1 else r_fib(num-2) + r_fib(num-1)


print(r_fib(9))


