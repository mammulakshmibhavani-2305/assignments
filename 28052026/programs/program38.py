def multiply_matrices(mat1, mat2):
  row1 = len(mat1)
  col1 = len(mat1[0])
  row2 = len(mat2)
  col2 = len(mat2[0])
  if col1 != row2:
    return "Matrix multiplication is not possible. Number of column"
  result = [[0 for _ in range(col2)] for _ in range(row1)]
  for i in range(row1):
    for j in range(col2):
      for k in range(col1):
        result[i][j] += mat1[i][k] * mat2[k][j]
  return result
matrix1 = [[1, 2, 3],
           [4, 5, 6]]
matrix2 = [[7, 8],
           [9, 10],
           [11, 12]]
result_matrix = multiply_matrices(matrix1, matrix2)
if isinstance(result_matrix, str):
  print(result_matrix)
else:
  print("Result of matrix multiplication:")
  for row in result_matrix:
    print(row)
