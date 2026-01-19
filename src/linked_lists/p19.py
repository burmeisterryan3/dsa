"""https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/"""

from typing import Optional
from utils.linked_lists import ListNode

class Solution:        
    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = None

        for _ in range(n):
            # Move fast n nodes ahead
            fast = fast.next
        
        if not fast:
            # fast is at the end, thus we are removing the first element
            # we will change head to slow.next (don't need to set it before returning)
            return slow.next

        while fast:
            # When fast is None, slow will be at the node we want to remove (as it is n nodes behind fast)
            fast = fast.next
            prev = slow
            slow = slow.next

        # To remove slow, point prev.next (slow) to the node after slow
        prev.next = slow.next
        
        return head