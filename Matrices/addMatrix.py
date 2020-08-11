""" Enter 2 matrices as input and the third matrix would be the result for this """

# Must be a square matrix
n = int(input())
matrix1 = [[0] * n for i in range(0, n)]
matrix2 = [[0] * n for i in range(0, n)]
result = [[0] * n for i in range(0, n)]

print('Enter first matrix : ')
for i in range(n):
    for j in range(n):
        temp = int(input())
        matrix1[i][j] = temp

print('Enter second matrix : ')
for i in range(n):
    for j in range(n):
        temp = int(input())
        matrix2[i][j] = temp

for i in range(n):
    for j in range(n):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print(result)