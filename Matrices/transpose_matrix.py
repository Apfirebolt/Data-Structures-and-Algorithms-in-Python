"""Given a square matrix, print the matrix which is the transpose of this matrix"""


def transposeMatrix(matrix, n):
  for i in range(n):
    for j in range(n):
      if i != j and i > j:
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

try:
  n = int(input())
  if n not in [1, 2, 3, 4, 5]:
    raise ValueError("Not an acceptable value of n, must be between 1 to 5")
  matrix_inp = list(map(int, input().split(' ')))
  if len(matrix_inp) != n*n:
    raise ValueError("Invalid length of the matrix")
  # Conversion of input into a matrix
  index = 0
  matrix = []

  for i in range(n):
    current_row = []
    for j in range(n):
      current_row.append(matrix_inp[index])
      index += 1
    matrix.append(current_row)

  print(matrix)
  transposeMatrix(matrix, n)
  print(matrix)

except ValueError as Err:
  print(Err)


