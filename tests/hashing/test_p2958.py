import pytest
from src.hashing.p2958 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p2958(solver):
    assert solver.max_subarray_length([1,2,3,1,2,3,1,2], 2) == 6
    assert solver.max_subarray_length([1,2,1,2,1,2,1,2], 1) == 2
    assert solver.max_subarray_length([5,5,5,5,5,5,5], 4) == 4
    assert solver.max_subarray_length([5], 3) == 1