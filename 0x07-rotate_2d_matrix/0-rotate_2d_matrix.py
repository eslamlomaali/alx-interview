#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """rotate two dimension matrix
    Args:
        matrix (list[[list]]): a matrix
    """
    n = len(matrix)
    for i in range(int(n / 2)):
        y = (n - i - 1)
        for j in range(i, y):
            x = (n - 1 - j)
            # current number
            tmp = matrix[i][j]
            # change top
            matrix[i][j] = matrix[x][i]
            # change left
            matrix[x][i] = matrix[y][x]
            # change bottom
            matrix[y][x] = matrix[j][y]
            # change right
            matrix[j][y] = tmp
