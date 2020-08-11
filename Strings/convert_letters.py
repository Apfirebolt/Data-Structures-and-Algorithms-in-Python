"""Convert small letters to caps and wise versa without using python functions"""

s = input()
result = ''
for letter in s:
    current_ascii = ord(letter)
    # Capital letter
    if current_ascii >= 65 and current_ascii <= 90:
        modified_ascii = current_ascii + 32
    # Small letter check
    if current_ascii >= 97 and current_ascii <= 122:
        modified_ascii = current_ascii - 32
    result += chr(modified_ascii)

print(result)