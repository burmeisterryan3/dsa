import pytest
from src.arrays_and_strings.p2090 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p1480(solver):
    assert solver.get_averages([7,4,3,9,1,8,5,2,6], 3) == [-1,-1,-1,5,4,4,-1,-1,-1]
    assert solver.get_averages([100000], 0) == [100000]
    assert solver.get_averages([8], 100000) == [-1]

def test_p1480_better(solver):
    assert solver.get_averages_better([7,4,3,9,1,8,5,2,6], 3) == [-1,-1,-1,5,4,4,-1,-1,-1]
    assert solver.get_averages_better([100000], 0) == [100000]
    assert solver.get_averages_better([8], 100000) == [-1]