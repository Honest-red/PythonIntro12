"""
def function_name(param1, param2, param3):
    operator_1
    expression_1

    return value1, value2
"""

# None


def get_food(x, y):
    # res = x + y
    return x + y    # res


# print("Сколько бананов и ананасов для обезьян?")
# a = int(input())
# b = int(input())
# res = get_food(a, b)
# # get_food(a, a)
# print("Всего", res, "шт.")

# print("Сколько жуков и червей для ежей?")
# a = int(input())
# b = int(input())
# get_food(2 * a, 5 * b)
# print("Всего", a + b, "шт.")
#
# print("Сколько рыб и моллюсков для выдр?")
# a = int(input())
# b = int(input())
# print("Всего", a + b, "шт.")


def hello():
    print('Hello World!')


hello()


def calculate_2_x_2():
    print(2 * 2)


calculate_2_x_2()
print(calculate_2_x_2())


def calculate(a, b):
    print(a * b)


calculate(3, 6)
calculate(7, 1)


def calculate_1(a, b):
    return a * b


print(calculate_1(3, 6))
print(calculate_1(7, 1))


PI = 3.14

b = 58


def func_1(a):
    global b
    b = 34
    print(b)    # 34
    return a * PI


print(b)        # 58
print(func_1(4))
print(b)        # 58


def my_pow(num=2, exp=2):
    return num ** exp


print(my_pow(2, 3))
print(my_pow(4))
print(my_pow())


def func_2(a, b, c, d=1, e=2, f=3):
    print(a, b, c, d, e, f)


func_2(10, 20, 30)
func_2(10, 20, 30, 40)
func_2(10, 20, 30, 40, 50)
func_2(10, 20, 30, 40, 50, 60)


def func_3(*args):
    print(type(args), args)


func_3(3, 6, 'g', True)


def func_4(**kwargs):
    print(type(kwargs), kwargs)


func_4(r=8, h=9, c=0)


d = {
    'aaa': ['1', '2', '3'],
    'bbb': ['4', '2', '6'],
    'ccc': ['4', '5', '6'],
}

d1 = {
    '1': ['aaa'],
    '2': ['aaa', 'bbb'],
    '3': ['aaa'],
    '4': ['bbb', 'ccc'],
    '5': ['ccc'],
    '6': ['bbb', 'ccc']
}
