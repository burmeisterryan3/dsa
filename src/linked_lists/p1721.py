"""https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/"""

from typing import Optional
from utils.linked_lists import ListNode

class Solution:
    def swap_nodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        for _ in range(k-1):
            fast = fast.next
        left = fast
        fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        if left.next == slow:
            # Swapping two adjacent nodes where k is less than or equal to half the length of the linked list
            temp = slow.next.next
            left.next = slow.next
            left.next.next = slow
            slow.next = temp
        elif slow.next == left:
            # Swapping two adjacent nodes where k is greater than half the length of the linked list
            temp = left.next.next
            slow.next = left.next
            slow.next.next = left
            left.next = temp
        else:
            n = left.next
            tmp = slow.next.next
            left.next  = slow.next
            left.next.next = n.next
            slow.next = n
            slow.next.next = tmp

        return dummy.next

    def swap_nodes_better(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        prev_n1 = dummy
        for _ in range(k-1):
            prev_n1 = prev_n1.next
        n1 = prev_n1.next

        fast = n1
        prev_n2 = dummy
        while fast.next:
            fast = fast.next
            prev_n2 = prev_n2.next
        n2 = prev_n2.next

        if n1 == n2:
            # Middle node, no need to swap
            return dummy.next

        prev_n1.next, prev_n2.next = n2, n1
        n1.next, n2.next = n2.next, n1.next

        return dummy.next