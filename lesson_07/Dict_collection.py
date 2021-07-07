from pprint import pprint

d = {}
d = dict()
d = {0: 'zero', 1: 'one', 2: 'two'}
print(d)

lst = [(0, 'zero'), (1, 'one'), (2, 'two'), (-1, 'dfgd')]
d1 = dict(lst)
print(d1)

d2 = dict(
    zero=0,
    one=1,
    two=2
)
print(d2)

print(d2['one'])
print(d1[-1])

print(d1)
d1[4] = 'four'
print(d1)
d1[0] = 'Null'
print(d1)

person = dict()
print(person)
person['first_name'] = 'Peter'
person['last_name'] = 'Peterson'
print(person)
person['pets'] = {'cat': 'Fox', 'dog': 'Pluto'}
pprint(person)
person['children'] = ['Ralph', 'Betty', 'Joey']
pprint(person)
print(person['pets']['dog'])
print(person['children'][1])

# len()
print(len(person))

# clear()
# person.clear()
# print(person)

# dict[key]
# print(person['first_name_1'])

# get(key, default_value)
#print(person.get('first_name_1', 'Name'))

# pop(key)
pprint(person)
print(person.pop('first_name'))
pprint(person)

# popitem()
print(person.popitem())
pprint(person)

# keys()
# values()
# items()
print(person.keys())
print(person.values())
print(person.items())
# a, b = 3, 6
for key, value in person.items():
    print(key, value)

# update()
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'e': 400, 'f': 500, 'b': 600}
print(d1)
print(d2)
d1.update(d2)
print(d1)

lst = [1, 2, 3, 4, 5, 6]
d3 = dict.fromkeys(lst)
pprint(d3)
