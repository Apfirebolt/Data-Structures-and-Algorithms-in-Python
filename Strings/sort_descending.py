"""Given a string, sort it in descending order"""


s = 'abcyhsix'
str_list = list(s)
str_list.sort()
print(''.join(str_list[::-1]))
