import pytest
from src.arrays_and_strings.p209 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p209(solver):
    assert solver.min_sub_array_len(7, [2,3,1,2,4,3]) == 2
    assert solver.min_sub_array_len(4, [1,4,4]) == 1
    assert solver.min_sub_array_len(11, [1,1,1,1,1,1,1,1]) == 0