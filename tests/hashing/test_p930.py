import pytest
from src.hashing.p930 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p930(solver):
    assert solver.num_subarrays_with_sum([1,0,1,0,1], 2) == 4
    assert solver.num_subarrays_with_sum([0,0,0,0,0], 0) == 15
    assert solver.num_subarrays_with_sum([1,0], 2) == 0
    assert solver.num_subarrays_with_sum([0,1], 2) == 0
    assert solver.num_subarrays_with_sum([0,0,0,0,1], 2) == 0