"""Given a binary number as string, convert it into decimal without using built in functions"""

s = '1010111101'
result = 0
pow_num = len(s)-1
for i in range(len(s)):
    if s[i] is '1':
        result += (2**pow_num)
    pow_num -= 1
print(result)