import pytest
from src.hashing.p1426 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p1426(solver):
    assert solver.count_elements([1,2,3]) == 2
    assert solver.count_elements([1,1,3,3,5,5,7,7]) == 0
    assert solver.count_elements([1,1,2,2]) == 2
