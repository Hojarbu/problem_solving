# binarysearch.com: https://binarysearch.com/problems/Linked-List-Deletion

class Solution:
    def solve(self, node, target):

        prev, curr = None, node

        while curr:
            if curr.val == target:
                if prev:
                    prev.next = curr.next
                else:
                    node = curr.next
                curr = curr.next
            else:
                prev, curr = curr, curr.next
        return node