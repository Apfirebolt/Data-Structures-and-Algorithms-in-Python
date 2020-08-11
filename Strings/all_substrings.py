""" Given a string, print all the substrings of a given length """

def printSubstrings(s, l):
    pass

s1 = input()
l = int(input())

try:
    if l > len(s1):
        raise ValueError('Entered length cannot be more than the length of the string!')
except ValueError as Err:
    print(Err)

print(s1, l)