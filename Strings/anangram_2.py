from collections import defaultdict

s1 = input()
s2 = input()

d1 = defaultdict()
d2 = defaultdict()

for letter in s1:
    if letter in d1:
        d1[letter] += 1
    else:
        d1[letter] = 1

for letter in s2:
    if letter in d2:
        d2[letter] += 1
    else:
        d2[letter] = 1

if d1 == d2:
    print('True')
else:
    print('False')

