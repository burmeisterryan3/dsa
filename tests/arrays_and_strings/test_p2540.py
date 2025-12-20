import pytest
from src.arrays_and_strings.p2540 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p2540(solver):
    assert solver.get_common([1,2,3], [2,4]) == 2
    assert solver.get_common([2,3,4,5], [1,2,3,6]) == 2
    assert solver.get_common([1,2,3], [4,5,6]) == -1
    assert solver.get_common([4,5,6], [1,2,3]) == -1