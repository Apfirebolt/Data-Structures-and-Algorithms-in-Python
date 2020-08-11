"""
Given 2 matrices, print a third matrix which is formed by multiplying those matrices, 
-1 if multiplication is not possible
"""

# Dimensions of first matrix, row followed by column
m1, n1 = map(int, input().split(' '))

# Dimensions of second matrix
m2, n2 = map(int, input().split(' '))
matrix1 = [[0] * n1 for i in range(0, m1)]
matrix2 = [[0] * n2 for i in range(0, m2)]
result = [[0] * n2 for i in range(0, m1)]

print('Enter first matrix : ')
for i in range(m1):
    for j in range(n1):
        temp = int(input())
        matrix1[i][j] = temp

print('Enter second matrix : ')
for i in range(m2):
    for j in range(n2):
        temp = int(input())
        matrix2[i][j] = temp

for i in range(m1):
  for j in range(n2):
    for k in range(m1):
      result[i][j] += matrix1[i][k] * matrix2[k][j]

print(result)

print(matrix1)
print(matrix2)
