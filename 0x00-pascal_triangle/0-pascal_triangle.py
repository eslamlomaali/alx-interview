#!/usr/bin/python3
"""
0-Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    solution = []
    if n > 0:
        for x in range(1, n + 1):
            high = []
            y = 1
            for z in range(1, x + 1):
                high.append(y)
                y = y * (x - z) // z
            solution.append(high)
    return solution
