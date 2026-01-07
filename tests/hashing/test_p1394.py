import pytest
from src.hashing.p1394 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p1394(solver):
    assert solver.find_lucky([2,2,3,4]) == 2
    assert solver.find_lucky([1,2,2,3,3,3]) == 3
    assert solver.find_lucky([2,2,2,3,3]) == -1

def test_p1394_counter(solver):
    assert solver.find_lucky_counter([2,2,3,4]) == 2
    assert solver.find_lucky_counter([1,2,2,3,3,3]) == 3
    assert solver.find_lucky_counter([2,2,2,3,3]) == -1