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

def test_p876(solver):
    assert solver.middle_node(create_llist([1,2,3,4,5])).val == 3
    assert solver.middle_node(create_llist([1,2,3,4,5,6])).val == 4