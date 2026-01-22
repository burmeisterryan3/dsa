import pytest
from src.linked_lists.p1721 import Solution
from utils.linked_lists import ListNode, create_llist, llist_to_list

@pytest.fixture
def solver():
    return Solution()

def test_p1721(solver):
    assert llist_to_list(solver.swap_nodes(create_llist([1,2,3,4,5]), 2)) == [1,4,3,2,5]
    assert llist_to_list(solver.swap_nodes(create_llist([7,9,6,6,7,8,3,0,9,5]),5)) == [7,9,6,6,8,7,3,0,9,5]
    assert llist_to_list(solver.swap_nodes(create_llist([1]), 1)) == [1]
    assert llist_to_list(solver.swap_nodes(create_llist([100,90]), 2)) == [90,100]
    assert llist_to_list(solver.swap_nodes(create_llist([100,24,24,36,18,52,95,61,54,88,86,79,11,1,31,26]), 16)) == [26,24,24,36,18,52,95,61,54,88,86,79,11,1,31,100]

def test_p1721_better(solver):
    assert llist_to_list(solver.swap_nodes_better(create_llist([1,2,3,4,5]), 2)) == [1,4,3,2,5]
    assert llist_to_list(solver.swap_nodes_better(create_llist([7,9,6,6,7,8,3,0,9,5]),5)) == [7,9,6,6,8,7,3,0,9,5]
    assert llist_to_list(solver.swap_nodes_better(create_llist([1]), 1)) == [1]
    assert llist_to_list(solver.swap_nodes_better(create_llist([100,90]), 2)) == [90,100]
    assert llist_to_list(solver.swap_nodes_better(create_llist([100,24,24,36,18,52,95,61,54,88,86,79,11,1,31,26]), 16)) == [26,24,24,36,18,52,95,61,54,88,86,79,11,1,31,100]
    

