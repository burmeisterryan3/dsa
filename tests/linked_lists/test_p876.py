import pytest
from src.linked_lists.p876 import Solution
from utils.linked_lists import ListNode, create_llist, llist_to_list

@pytest.fixture
def solver():
    return Solution()

def test_p876(solver):
    assert llist_to_list(solver.middle_node(create_llist([1,2,3,4,5]))) == [3,4,5]
    assert llist_to_list(solver.middle_node(create_llist([1,2,3,4,5,6]))) == [4,5,6]