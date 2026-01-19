import pytest
from src.linked_lists.p92 import Solution
from utils.linked_lists import ListNode, create_llist, llist_to_list

@pytest.fixture
def solver():
    return Solution()

def test_p92(solver):
    assert llist_to_list(solver.reverse_between(create_llist([1,2,3,4,5]), 2, 4)) == [1,4,3,2,5]
    assert llist_to_list(solver.reverse_between(create_llist([5]), 1, 1)) == [5]
    assert llist_to_list(solver.reverse_between(create_llist([1,2]), 1, 2)) == [2,1]
    assert llist_to_list(solver.reverse_between(create_llist([1,2,3,4,5]), 3, 3)) == [1,2,3,4,5]
    assert llist_to_list(solver.reverse_between(create_llist([1,2,3,4,5]), 3, 5)) == [1,2,5,4,3]

