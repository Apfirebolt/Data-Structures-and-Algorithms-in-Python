"""Print the character that occurs maximum number of times witin a string, if there are more than 1,
return the smaller character"""

s = input()
d = {}
max_value = 0
max_key = ''

for letter in s:
  if letter not in d:
    d[letter] = 1
  else:
    d[letter] += 1

for key, value in d.items():
  if value > max_value or ( value == max_value and key < max_key):
    max_value = value
    max_key = key

print(max_value, max_key)
