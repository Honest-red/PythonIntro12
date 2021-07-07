# 0x26bd
# 0o
# 0b

# chr(code)
print(chr(0x26bd))
print('\u26bd')
print(chr(9917))

print(ord('⚽'))
print(hex(ord('⚽')))
print(oct(ord('⚽')))
print(bin(ord('⚽')))

wave = '~'
boat = '\U0001F6A3'
seagull = '\u033C'
fish = '\U0001F41F'
penguin = '\U0001F427'
wale = '\U0001F40B'
octopus = '\U0001F419'

row = wave * 10 + boat + wave * 15 + '\n'
fish_row = wave * 4 + fish + wave * 21 + '\n'
wale_row = wave * 10 + wale + wave * 15 + '\n'
penguin_row = wave * 7 + penguin + wave * 18 + '\n'
octopus_row = wave * 17 + octopus + wave * 8 + '\n'

sea = row + fish_row + wale_row + penguin_row + octopus_row
print(sea)

s = 'Hello World!'

for r in s:
    print(r, end=' ')
print()

#       0   1   2   3   4
#       H   E   L   L   O
#      -5  -4  -3  -2  -1
s = 'Process finished with exit code 0'
print(s[0], s[1], s[-1])
c = s[0]
# s[0] = 'G'    # ERROR

# str[start: stop: step]
# str[:]   <==>   str
print(id(s))
print(id(s[:]))
print(s[8: 16: 2])
print(s[: 7])
print(s[8:])

s = 'Process finished with exit code 100'
print(len(s))
# print(s[33])
print(s[8: 8743568347567834])
print(s[-87356783465834: 7])
print(s[:: -1])

# str.find(sub, start, end)
# str.find(sub)
print(s)
print(s.find('e'))
print(s.find('e', 5))
print(s.find('e', 15))
print(s.find('e', 23))
print(s.find('e', 31))

# rfind()

s = 'Process finished with finished exit finished code 100'
# str.replace(old, new, count)
print(s)
print(s.replace('e', 'E', 1))
print(s.replace('finished', 'stop', 2))

# str.count(sub)
print(s)
print(s.count('e'))
print(s.count('finished'))

s = 'process Finished with finiShed eXit finished code 100'
# str.capitalize()
print(s)
print(s.capitalize())

# join()
# str.split()

# str.upper()
# str.lower()
print(s)
print(s.upper())
print(s.lower())

# str.strip(sub)
s = 'aaaaaaaaaHello World!bbbbbbbbb'
print('"' + s + '"')
s1 = s.strip('a').strip('b')
print(s1)
print('"' + s1.strip('b') + '"')
print(s.lstrip('a').rstrip('b'))

# str.title()
s = 'process Finished with finiShed eXit finished code 100'
print(s)
print(s.title())



