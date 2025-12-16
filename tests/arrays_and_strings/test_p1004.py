import pytest
from src.arrays_and_strings.p1004 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_643(solver):
    assert solver.longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
    assert solver.longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10
    assert solver.longest_ones([1], 1) == 1
    assert solver.longest_ones([0], 1) == 1
    assert solver.longest_ones([0,0,0,0,0], 2) == 2
    assert solver.longest_ones([0,0,1,1,1,0,0], 0) == 3