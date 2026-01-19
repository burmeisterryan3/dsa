import pytest
from src.linked_lists.p83 import Solution
from utils.linked_lists import ListNode, create_llist, llist_to_list

@pytest.fixture
def solver():
    return Solution()

def test_p83(solver):
    assert llist_to_list(solver.delete_duplicates(create_llist([1,1,2]))) == [1,2]
    assert llist_to_list(solver.delete_duplicates(create_llist([1,1,2,3,3]))) == [1,2,3]
    assert llist_to_list(solver.delete_duplicates(create_llist([]))) == []