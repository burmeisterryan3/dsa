import pytest
from src.arrays_and_strings.p1413 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p1413(solver):
    assert solver.min_start_value([1,2]) == 1
    assert solver.min_start_value([-3,2,-3,4,2]) == 5
    assert solver.min_start_value([1,-2,-3]) == 5