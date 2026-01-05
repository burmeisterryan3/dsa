import pytest
from src.hashing.p217 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p217(solver):
    assert solver.contains_duplicate([1,2,3,1]) == True
    assert solver.contains_duplicate([1,2,3,4]) == False
    assert solver.contains_duplicate([1,1,1,3,3,4,3,2,4,2]) == True
    assert solver.contains_duplicate([3, 1]) == False

def test_p217_better(solver):
    assert solver.contains_duplicate_better([1,2,3,1]) == True
    assert solver.contains_duplicate_better([1,2,3,4]) == False
    assert solver.contains_duplicate_better([1,1,1,3,3,4,3,2,4,2]) == True
    assert solver.contains_duplicate_better([3, 1]) == False

