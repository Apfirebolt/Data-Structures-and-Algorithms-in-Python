from collections import Counter


def isAnangram(s1, s2):
    if Counter(s1) == Counter(s2):
        return True
    return False


s1 = input()
s2 = input()

print(isAnangram(s1, s2))