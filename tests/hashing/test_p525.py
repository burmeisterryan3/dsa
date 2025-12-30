import pytest
from src.hashing.p525 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p525(solver):
    assert solver.find_max_length([0,1]) == 2
    assert solver.find_max_length([0,1,0]) == 2
    assert solver.find_max_length([0,1,1,1,1,1,0,0,0]) == 6
    assert solver.find_max_length([0,0,1]) == 2

def test_p525_better(solver):
    assert solver.find_max_length_better([0,1]) == 2
    assert solver.find_max_length_better([0,1,0]) == 2
    assert solver.find_max_length_better([0,1,1,1,1,1,0,0,0]) == 6
    assert solver.find_max_length_better([0,0,1]) == 2