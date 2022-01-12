# https://leetcode.com/problems/sort-array-by-parity/


"""In-place solution"""
def sortArrayByParity(self, nums: List[int]) -> List[int]:
    for i in range(0, len(nums)):
        if nums[i] % 2 != 0:  # if odd
            for j in range(i, len(nums)):  # find first even and update values
                if nums[j] % 2 == 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
    return nums


"""
[3,1,2,4]
 ^   
[2,1,3,4]
[2,4,3,1]
"""