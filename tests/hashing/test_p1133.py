import pytest
from src.hashing.p1133 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p1133(solver):
    assert solver.largest_unique_number([5,7,3,9,4,9,8,3,1]) == 8
    assert solver.largest_unique_number([9,9,8,8]) == -1