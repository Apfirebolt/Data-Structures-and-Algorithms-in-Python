"""Given an array containing numbers from 1 to n, but 1 number is missing and 1 is repeated twice (O(n) time )"""

a = list(map(int, input().split(' ')))
n = len(a)
missing = -1
repeated = -1
s = sum(a)
for i in range(n):
    if a[abs(a[i])-1] > 0:
        a[abs(a[i]) - 1] = -a[abs(a[i]) - 1]
    else:
        repeated = abs(a[i])
        break
exc_sum = s - repeated
series_sum = (n * (n+1))//2
missing = series_sum - exc_sum
print(repeated, missing)
