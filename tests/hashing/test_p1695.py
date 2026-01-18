import pytest
from src.hashing.p1695 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p1695(solver):
    assert solver.maximum_unique_subarray([4,2,4,5,6]) == 17
    assert solver.maximum_unique_subarray([5,2,1,2,5,2,1,2,5]) == 8

def test_p1695_set(solver):
    assert solver.maximum_unique_subarray_set([4,2,4,5,6]) == 17
    assert solver.maximum_unique_subarray_set([5,2,1,2,5,2,1,2,5]) == 8
