s = input()
d = {}

for letter in s:
    if letter in d:
        d[letter] += 1
    else:
        d[letter] = 1
result = ''
for key, value in d.items():
    temp = str(key) + str(value)
    result += temp

print(result)
