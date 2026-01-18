import pytest
from src.hashing.p3005 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p3005(solver):
    assert solver.max_frequency_elements([1,2,2,3,1,4]) == 4
    assert solver.max_frequency_elements([1,2,3,4,5]) == 5

def test_p3005_counter(solver):
    assert solver.max_frequency_elements_counter([1,2,2,3,1,4]) == 4
    assert solver.max_frequency_elements_counter([1,2,3,4,5]) == 5