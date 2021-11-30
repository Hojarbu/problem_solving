# LeetCode: https://leetcode.com/problems/binary-search/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1

        while first <= last:
            mid = (first + last) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                last = mid - 1
            else:
                first = mid + 1
        return -1
