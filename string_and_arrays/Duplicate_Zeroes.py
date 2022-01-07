# https://leetcode.com/problems/duplicate-zeros/

def duplicateZeros(self, arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    indexes = []
    for i, j in enumerate(arr):
        if j == 0:
            indexes.append(i)
    ln = len(arr)

    for i in range(len(indexes)):
        pos = indexes[i] + i + 1  # i starts with 0, that's why i+1
        if pos < len(arr):
            arr.insert(pos, 0)
            arr.pop()