"""
Using merge sort to solve the problem. The interesting method is getMid(). Using
2 pointers technique to find the mid node of the linked list.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        left = head
        mid = self.getMid(head)
        right = mid.next
        mid.next = None

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    def getMid(self, node: ListNode) -> ListNode:
        slow, fast = node, node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(
        self, left: Optional[ListNode], right: Optional[ListNode]
    ) -> Optional[ListNode]:
        tail = head = ListNode()
        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

        tail.next = left if left else right
        return head.next
