# https://leetcode.com/problems/max-consecutive-ones/

count = 0
save = 0
for i in range(len(nums)):
    if nums[i]==1:
        count+=1
        if save < count:
            save = count
    else:
        count=0
return save