"""
Given two strings s1 and s2, remove those characters from first string which are present in 
second string. Both the strings are different and contain only lowercase characters.
"""


def removeDuplicates(s1, s2):
  s = set()
  for letter in s2:
    s.add(letter)
  string_list = list(s1)
  for i in range(len(string_list)):
    if string_list[i] in s:
      string_list[i] = ''

  return ''.join(string_list)

s1 = input()
s2 = input()
print(removeDuplicates(s1, s2))
