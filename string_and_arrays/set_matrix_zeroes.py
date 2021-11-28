# Leetcode problem: https://leetcode.com/problems/set-matrix-zeroes/

from typing import List


# Version 1
def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m, n = len(matrix), len(matrix[0])
    cells = []
    rows = []
    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            if item == 0:
                cells.append(j)
                rows.append(i)

    for i in range(m):
        if i in rows:
            for j in range(n):
                matrix[i][j] = 0
        else:
            for j in range(n):
                if j in cells:
                    matrix[i][j] = 0
    return matrix