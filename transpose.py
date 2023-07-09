matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("Original matrix:")
for row in matrix:
    print(row)
print("Transpose of the matrix:")
for row in transpose:
    print(row)
