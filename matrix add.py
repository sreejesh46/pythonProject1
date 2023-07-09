matrix1 = [[1, 12, 3], [4, 10, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 10, 4], [3, 12, 1]]
result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
print("Result matrix after adding the two matrices:")
for row in result:
    print(row)
