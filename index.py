# Define the size of the matrix
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Create an empty matrix
matrix = []

# Read the matrix from the user
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input("Enter element ({},{}): ".format(i, j)))
        row.append(element)
    matrix.append(row)

# Find the sum of each row and each column
row_sums = [sum(row) for row in matrix]
col_sums = [sum(matrix[i][j] for i in range(rows)) for j in range(cols)]

# Print the matrix and the sums
print("Matrix:")
for row in matrix:
    print(row)
print("Row sums:", row_sums)
print("Column sums:", col_sums)