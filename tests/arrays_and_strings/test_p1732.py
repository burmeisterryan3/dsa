import pytest
from src.arrays_and_strings.p1732 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p1732(solver):
    assert solver.largest_altitude([-5,1,5,0,-7]) == 1
    assert solver.largest_altitude([-4,-3,-2,-1,4,3,2]) == 0
