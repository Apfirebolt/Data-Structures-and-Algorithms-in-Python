"""Given a number, convert it into binary base without using functions"""

n = int(input())
binary_num = ''

while n:
    r = n % 2
    binary_num += str(r)
    n = n // 2

# Print the reverse of the string
print(binary_num[::-1])
