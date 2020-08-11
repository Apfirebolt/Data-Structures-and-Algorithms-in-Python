"""Program to print the nth number of a fibonacci series"""
dp = []
dp.append(0)
dp.append(1)

for i in range(2, 100):
    temp = dp[i-1] + dp[i-2]
    dp.append(temp)

try:
    n = int(input())
    if n >= 100:
        raise ValueError("The value of integer cannot be greater than 100")
    print(dp[n])
except ValueError as Err:
    print(Err)
