# Leetcode https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            if i[:2] == "--" or i[-2:] == "--":
                x -= 1
            elif i[:2] == "++" or i[-2:] == "++":
                x += 1
        return x


    # version 2:

    # return sum(1 if x[1] == '+' else -1 for x in operations)
