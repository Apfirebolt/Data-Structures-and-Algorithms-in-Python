"""
Given a String of length N reverse each word in it. Words are separated by dots.
"""

s = input()
str_list = s.split('.')
for i in range(len(str_list)):
  new_word = str_list[i][::-1]
  str_list[i] = new_word
print('.'.join(str_list))