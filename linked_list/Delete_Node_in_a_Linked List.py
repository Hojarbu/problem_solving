# https://leetcode.com/problems/delete-node-in-a-linked-list/


class Solution:
    def deleteNode(self, node):
        prev = node
        while node.next:
            node.val = node.next.val
            prev = node
            node = node.next

        prev.next = None
