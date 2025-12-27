import pytest
from src.arrays_and_strings.p724 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p724(solver):
    assert solver.pivot_index([1,7,3,6,5,6]) == 3
    assert solver.pivot_index([1,2,3]) == -1
    assert solver.pivot_index([2,1,-1]) == 0

def test_p724_better(solver):
    assert solver.pivot_index_better([1,7,3,6,5,6]) == 3
    assert solver.pivot_index_better([1,2,3]) == -1
    assert solver.pivot_index_better([2,1,-1]) == 0