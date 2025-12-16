import pytest
from src.arrays_and_strings.p1480 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p1480(solver):
    assert solver.running_sum([1,2,3,4]) == [1,3,6,10]
    assert solver.running_sum([1,1,1,1,1]) == [1,2,3,4,5]
    assert solver.running_sum([3,1,2,10,1]) == [3,4,6,16,17]