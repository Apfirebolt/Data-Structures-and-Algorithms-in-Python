""" You have a given array where every element occurs twice except a single element which appears only once, 
find that element """

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5]

xor_result = 0
for i in range(len(arr)):
    xor_result ^= arr[i]

print(xor_result)


