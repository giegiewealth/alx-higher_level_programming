#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Get the number of rows and columns in the input matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    # Create a new matrix to store the squared values
    result_matrix = [[0] * num_cols for _ in range(num_rows)]

    # Iterate through the rows and columns of the input matrix
    for i in range(num_rows):
        for j in range(num_cols):
            # Square the value at the current position and store it in the result matrix
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = square_matrix_simple(matrix)
for row in result:
    print(row)
