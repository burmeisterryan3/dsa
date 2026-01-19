"""Define utility classes to be used within problems and tests."""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_llist(arr):
    if arr == []:
        return None

    head = ListNode(arr[0])
    curr = head
    for num in arr[1:]:
        curr.next = ListNode(num)
        curr = curr.next
    return head

def llist_to_list(head):
    """Convert a linked list to a Python list."""
    if head == None:
        return []

    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result