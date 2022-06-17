from typing import List

# https://leetcode.com/problems/next-greater-element-i/


def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    st = []
    res = {}
    for i in nums2[::-1]:
        if st:
            if st[-1] > i:
                res[i] = st[-1]
                st.append(i)
            else:
                while st and st[-1] < i:
                    st.pop()
                if st:
                    res[i] = st[-1]
                else:
                    res[i] = -1
                st.append(i)

        else:
            st.append(i)
            res[i] = -1

    result = []
    for check in nums1:
        if check in res.keys():
            result.append(res[check])
        else:
            result.append(-1)
    return result
