# Read the matrix dimensions from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize the matrix as a list of lists
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input("Enter element [{},{}]: ".format(i, j)))
        row.append(element)
    matrix.append(row)

# Find the sum of each row
row_sums = []
for i in range(rows):
    row_sum = sum(matrix[i])
    row_sums.append(row_sum)

# Find the sum of each column
col_sums = []
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    col_sums.append(col_sum)

# Print the results
print("Row sums:", row_sums)
print("Column sums:", col_sums)
