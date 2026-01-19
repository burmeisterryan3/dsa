"""https://leetcode.com/problems/middle-of-the-linked-list/description/"""

from typing import Optional
from utils.linked_lists import ListNode

class Solution:
    def delete_middle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        slow = head
        fast = head.next.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next

        return head
            
    def delete_middle_speed(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next

        return head
