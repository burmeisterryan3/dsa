"""https://leetcode.com/problems/reverse-linked-list-ii/description/"""

from typing import Optional
from utils.linked_lists import ListNode

class Solution:
    def reverse_between(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:   
        prev = None
        curr = head

        # Move to the left node (Node 1 is at index 0, so we subtract 1)
        for _ in range(left-1):
            prev = curr
            curr = curr.next
        
        l_node = curr
        for _ in range(right-left+1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        if left == 1:
            # When left is 1, our head needs to be original right, i.e., the new left and beginning node
            head = prev
        else: # left != 1:
            # When left is 1, this will fail as their are no nodes to prior to left
            # l_node is at the beginning and l_node.next is None (line 19 - prev would be None at that point)
            # After executing, the node prior to left will now point to the original right node
            # Thus, we successfully will have moved the original right node to the left position
            l_node.next.next = prev
        # Our original left.next should point to what was orignally right.next
        # This ensures we don't lose what was to the right of our original right node
        l_node.next = curr

        return head

            

        

