"""https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/"""

from typing import Optional
from utils.linked_lists import ListNode

class Solution:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Much simpler solution by creating a node prior to head
        sentinel = ListNode(0, head)
        prev = sentinel
        curr = head

        while curr:
            if curr.next and (curr.val == curr.next.val):
                dup_val = curr.val
                while curr and (curr.val == dup_val):
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        
        return sentinel.next
        


    def delete_duplicates_first(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        repeated_val = None

        while curr:
            if curr.next and (curr.val == curr.next.val):
                # When we see the start of a repeating value, save the value
                repeated_val = curr.val
            elif curr.val != repeated_val:
                if repeated_val is not None:
                    # We enter here, if we had previously iterated through a series of repeated values
                    if not prev:
                        # If the first value repeated, move head to curr as those will be removed
                        head = curr
                    else:
                        # If repeated but not the first values, prev.next should point past the repeated values
                        prev.next = curr
                    # Reset repeated_val to indicate we are not in a repeating sequence
                    repeated_val = None
                prev = curr
            curr = curr.next
        
        if repeated_val is not None:
            # We enter here if we ended on a repeating sequence
            if not prev:
                # If the whole list was repeating, return an empty linked list
                head = None
            else:
                # Otherwise, make the the last non-repeating node the last node in the linked list
                # by setting its next to None
                prev.next = None

        return head