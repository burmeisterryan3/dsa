import pytest
from src.arrays_and_strings.p643 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_643(solver):
    assert abs((solver.find_max_average([1,12,-5,-6,50,3], 4)) - 12.75) < 1e-5
    assert abs((solver.find_max_average([5], 1) - 5)) < 1e-5
    assert abs((solver.find_max_average([-10,-12,-3,-35], 2)) + 7.5) < 1e-5
    assert abs((solver.find_max_average([0,1,1,3,3], 4) - 2)) < 1e-5