import pytest
from src.linked_lists.p82 import Solution
from utils.linked_lists import ListNode, create_llist, llist_to_list

@pytest.fixture
def solver():
    return Solution()

def test_p82(solver):
    assert llist_to_list(solver.delete_duplicates(create_llist([1,2,3,3,4,4,5]))) == [1,2,5]
    assert llist_to_list(solver.delete_duplicates(create_llist([1,1,1,2,3]))) == [2,3]
    assert llist_to_list(solver.delete_duplicates(create_llist([1,1]))) == []
    assert llist_to_list(solver.delete_duplicates(create_llist([1,2,2]))) == [1]
    assert llist_to_list(solver.delete_duplicates(create_llist([0,0,0,0,0]))) == []
    assert llist_to_list(solver.delete_duplicates(create_llist([0,0,0,0,3]))) == [3]

def test_p82_first(solver):
    assert llist_to_list(solver.delete_duplicates_first(create_llist([1,2,3,3,4,4,5]))) == [1,2,5]
    assert llist_to_list(solver.delete_duplicates_first(create_llist([1,1,1,2,3]))) == [2,3]
    assert llist_to_list(solver.delete_duplicates_first(create_llist([1,1]))) == []
    assert llist_to_list(solver.delete_duplicates_first(create_llist([1,2,2]))) == [1]
    assert llist_to_list(solver.delete_duplicates_first(create_llist([0,0,0,0,0]))) == []
    assert llist_to_list(solver.delete_duplicates_first(create_llist([0,0,0,0,3]))) == [3]


