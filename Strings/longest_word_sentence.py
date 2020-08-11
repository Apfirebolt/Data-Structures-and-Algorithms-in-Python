"""
Given a string, we have to find the longest word in the input string 
and then calculate the number of characters in this word.
"""

for i in range(int(input())):
  s = input()
  max_len = -1
  sentence = s.split(' ')

  for i in range(len(sentence)):
    if len(sentence[i]) > max_len:
      max_len = len(sentence[i])
  print(max_len)