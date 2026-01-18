"""https://leetcode.com/problems/middle-of-the-linked-list/description/"""

from typing import Optional
from utils.data_structures import ListNode

class Solution:
    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow