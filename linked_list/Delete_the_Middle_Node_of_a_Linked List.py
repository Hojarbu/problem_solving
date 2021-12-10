# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """Find midle of the linked list by its length"""
    node = head
    length = 0
    while node:
        length += 1
        node = node.next
    mid = (length // 2) + 1

    """Remove node that is equal to mid node"""
    node = head
    prev = None
    step = 0
    while node:
        step += 1
        if step == mid:
            if prev:
                prev.next = node.next
            else:
                head = node.next
            node = node.next
        else:
            prev, node = node, node.next
    return head
