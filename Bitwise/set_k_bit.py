"""Given a binary number and an integer k, set the kth bit of this binary number if not already set"""

def convertDecimal(bin_string):
    string_bin = ''
    for letter in bin_string:
        string_bin += str(letter)
    result = 0
    pow_count = n - 1
    for i in range(n):
        if string_bin[i] is '1':
            temp = 2**pow_count
            result += temp
        pow_count -= 1
    return result

try:
    n, k = map(int, input().split(' '))
    binary_str = bin(n)[2:]
    if len(binary_str) < k:
        raise ValueError("Invalid value of k")
    print(binary_str)
    binary_list = list(binary_str)
    binary_list[k-1] = 1
    print(convertDecimal(binary_list))
except ValueError as Err:
    print(Err)


