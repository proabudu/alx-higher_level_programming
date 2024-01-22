#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

  # Check if matrix is a valid 2D list of integers
  if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
    raise ValueError("Matrix must be a 2D list.")
  for row in matrix:
    if not all(isinstance(x, int) for x in row):
      raise ValueError("Matrix must only contain integers.")

  # Create a new empty matrix of the same size
  new_matrix = [[0 for _ in range(len(row))] for row in matrix]

  # Loop through each element and replace it with its square in the new matrix
  for i, row in enumerate(matrix):
    for j, element in enumerate(row):
      new_matrix[i][j] = element * element

  return new_matrix
