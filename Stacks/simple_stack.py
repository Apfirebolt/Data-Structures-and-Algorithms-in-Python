"""A Program to implement simple stack, reverse a string"""

word = input()
reverse_word = ''
s = []

for i in range(len(word)):
  s.append(word[i])

while len(s):
  reverse_word += s.pop()

print(reverse_word)
