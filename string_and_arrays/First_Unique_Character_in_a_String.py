# Leetcode:
# https://leetcode.com/problems/first-unique-character-in-a-string/
from collections import Counter


def firstUniqChar(self, s: str) -> int:
    dc = Counter(s)      # O(N)
    for k, v in dc.items():  # O(N)
        if v == 1:
            return s.index(k)  # O(N)
    return -1

# Time complexity
#  O(N)+ O(N)+ O(N) => O(N)

