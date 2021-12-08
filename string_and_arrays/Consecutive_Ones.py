# Source: https://binarysearch.com/problems/Consecutive-Ones

class Solution:
    def solve(self, nums):
        idx = None
        for i, j in enumerate(nums):
            if j == 1:
                if idx is None:
                    idx = i + 1

                elif idx + 1 == i + 1:
                    idx += 1
                else:
                    return False

        if idx:
            return True
        return False
