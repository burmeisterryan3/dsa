import pytest
from src.hashing.p1748 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p1748(solver):
    assert solver.sum_of_unique([1,2,3,2]) == 4
    assert solver.sum_of_unique([1,1,1,1,1]) == 0
    assert solver.sum_of_unique([1,2,3,4,5]) == 15

def test_p1748_pythonic(solver):
    assert solver.sum_of_unique_pythonic([1,2,3,2]) == 4
    assert solver.sum_of_unique_pythonic([1,1,1,1,1]) == 0
    assert solver.sum_of_unique_pythonic([1,2,3,4,5]) == 15

def test_p1748_counter(solver):
    assert solver.sum_of_unique_counter([1,2,3,2]) == 4
    assert solver.sum_of_unique_counter([1,1,1,1,1]) == 0
    assert solver.sum_of_unique_counter([1,2,3,4,5]) == 15