# Leetcode: https://leetcode.com/problems/middle-of-the-linked-list/


# version 1: fast&slow approach
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# version 2
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    node = head
    length = 0
    while node:
        length += 1
        node = node.next

    mid = (length // 2) + 1

    step = 0
    while head:
        step += 1
        if step == mid:
            return head
        head = head.next
    return
