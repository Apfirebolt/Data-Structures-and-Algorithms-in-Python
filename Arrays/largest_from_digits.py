"""
Given an array of numbers form 0 to 9 of size N. 
Your task is to rearrange elements of the array such that after combining all the elements of the 
array number formed is maximum.
"""

arr = list(map(int, input().split(' ')))
arr.sort()
print(''.join([str(x) for x in arr[::-1]]))