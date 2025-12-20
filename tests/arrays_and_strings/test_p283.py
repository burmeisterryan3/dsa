import pytest
from src.arrays_and_strings.p283 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p283(solver):
    assert solver.move_zeros([0,1,0,3,12]) == [1,3,12,0,0]
    assert solver.move_zeros([0]) == [0]
    assert solver.move_zeros([0,0,0]) == [0,0,0]
    assert solver.move_zeros([0,1,3,12,0]) == [1,3,12,0,0]
    assert solver.move_zeros([1,0,3,0,12]) == [1,3,12,0,0]