import pytest
from src.linked_lists.p876 import Solution
from utils.data_structures import ListNode

@pytest.fixture
def solver():
    return Solution()

def create_llist(list):
    head = ListNode(list[0])
    curr = head
    for num in list[1:]:
        curr.next = ListNode(num)
        curr = curr.next
    return head

def llist_to_list(head):
    """Convert a linked list to a Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test_p876(solver):
    assert llist_to_list(solver.middle_node(create_llist([1,2,3,4,5]))) == [3,4,5]
    assert llist_to_list(solver.middle_node(create_llist([1,2,3,4,5,6]))) == [4,5,6]