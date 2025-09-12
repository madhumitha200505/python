import numpy as np

def matrix_sum(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def matrix_product(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

# Define two compatible matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)

# Calculate and print the sum
sum_matrix = matrix_sum(matrix1, matrix2)
print("\nSum of Matrix 1 and Matrix 2:")
print(sum_matrix)

# Calculate and print the product
product_matrix = matrix_product(matrix1, matrix2)
print("\nProduct of Matrix 1 and Matrix 2:")
print(product_matrix)