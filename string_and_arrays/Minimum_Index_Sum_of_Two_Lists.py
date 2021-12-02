# Leetcode: https://leetcode.com/problems/minimum-index-sum-of-two-lists/
from collections import defaultdict
from typing import List


# not optimal solution, still works
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ls = defaultdict(int)

        for i, j in enumerate(list1):
            if j in list2:
                ls[j] += i

        for k, l in enumerate(list2):
            if l in list1:
                ls[l] += k

        res = []
        idx = None
        for m, n in sorted(ls.items(), key=lambda item: item[1]):
            if not res:
                res.append(m)
                idx = n
            else:
                if idx == n:
                    res.append(m)
        return res