import pytest
from src.linked_lists.p2095 import Solution
from utils.linked_lists import ListNode, create_llist, llist_to_list

@pytest.fixture
def solver():
    return Solution()

def test_p2095(solver):
    assert llist_to_list(solver.delete_middle(create_llist([1,3,4,7,1,2,6]))) == [1,3,4,1,2,6]
    assert llist_to_list(solver.delete_middle(create_llist([1,2,3,4]))) == [1,2,4]
    assert llist_to_list(solver.delete_middle(create_llist([2,1]))) == [2]
    assert llist_to_list(solver.delete_middle(create_llist([1]))) == []

def test_p2095_speed(solver):
    assert llist_to_list(solver.delete_middle_speed(create_llist([1,3,4,7,1,2,6]))) == [1,3,4,1,2,6]
    assert llist_to_list(solver.delete_middle_speed(create_llist([1,2,3,4]))) == [1,2,4]
    assert llist_to_list(solver.delete_middle_speed(create_llist([2,1]))) == [2]
    assert llist_to_list(solver.delete_middle_speed(create_llist([1]))) == []
