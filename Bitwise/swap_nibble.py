"""
Given a byte, swap the two nibbles in it. For example 100 is be represented as 01100100 in a byte (or 8 bits). 
The two nibbles are (0110) and (0100). If we swap the two nibbles, we get 01000110 which is 70 in decimal.
"""

def convertDec(n):
  pass

n = int(input())
bin_str = str(bin(n)[2:])
print(bin_str)