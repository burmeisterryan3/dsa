"""https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/"""

from typing import Optional
from utils.linked_lists import ListNode

class Solution:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        last_val = head.val
        dummy = head
        
        while dummy and dummy.next:
            if dummy.next.val == last_val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
                last_val = dummy.val
        
        return head