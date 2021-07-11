from random import randint
from pprint import pprint

# lst = [randint(10, 50) for _ in range(20)]
# print(lst)
# lst.sort(reverse=True)
# print(lst)

text = """
    Василий Петров
    Андрей Говорухи
    Максим Мухин
    Кощей Бессмертный
    Гавриил Варфаломеев
    Спиридов Тереньтьев
    Маргарита Мартынова
    Илья Муромцев
    Станислав Трердолобов
    Полина Гусева
    Петр Николаев
    Игнат Тюльпанов
"""

lst = [line.strip() for line in text.strip('\n').split('\n')]
pprint(lst)
# lst.sort()
# pprint(lst)


# def get_last_name(full_name):
#     return full_name.split()[1]


# lst.sort(key=get_last_name, reverse=True)
# lst.sort(key=lambda x: x.split()[1])
# pprint(lst)


# sorted
tp = tuple(randint(10, 50) for _ in range(20))
print(tp)
res = tuple(sorted(tp))
print(res)

res = sorted(lst, key=lambda x: x.split()[1])
pprint(res)

res = sorted(lst, key=lambda x: len(x.split()[0]))
pprint(res)
