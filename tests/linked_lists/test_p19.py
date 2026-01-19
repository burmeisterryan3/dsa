import pytest
from src.linked_lists.p19 import Solution
from utils.linked_lists import ListNode, create_llist, llist_to_list

@pytest.fixture
def solver():
    return Solution()

def test_p19(solver):
    assert llist_to_list(solver.remove_nth_from_end(create_llist([1,2,3,4,5]), 2)) == [1,2,3,5]
    assert llist_to_list(solver.remove_nth_from_end(create_llist([1]), 1)) == []
    assert llist_to_list(solver.remove_nth_from_end(create_llist([1,2]), 1)) == [1]
