# Linked List Delete Last Occurrence of Value
# link: https://binarysearch.com/problems/Linked-List-Delete-Last-Occurrence-of-Value

class Solution:

    def solve(self, node, target):
        ind = 0
        last = None
        cur = node

        # remember last index
        while cur:
            ind += 1
            if cur.val == target:
                last = ind
            cur = cur.next

        prev, head = None, node
        ind = 0
        # remove item in that index
        while head:
            ind += 1
            if ind == last:
                if prev:
                    prev.next = head.next
                else:
                    node = head.next
                break
            else:
                prev, head = head, head.next
        return node
