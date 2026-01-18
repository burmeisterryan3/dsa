import pytest
from src.hashing.p1207 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p1207(solver):
    assert solver.unique_occurrences([1,2,2,1,1,3]) == True
    assert solver.unique_occurrences([1,2]) == False
    assert solver.unique_occurrences([-3,0,1,-3,1,1,1,-3,10,0]) == True
