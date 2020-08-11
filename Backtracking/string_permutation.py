"""Print all permutations of a string using backtracking and a global variable"""

all_strings = []

def printPermutation(s, start, end):
    if start == end:
        all_strings.append(s)

    for i in range(start, end):
        s[start], s[i] = s[i], s[start]
        printPermutation(s, start+1, end)
        s[start], s[i] = s[i], s[start]

input_str = input()
s = list(input_str)
printPermutation(s, 0, len(s))
print(len(all_strings))