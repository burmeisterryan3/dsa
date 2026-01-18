import pytest
from src.hashing.p1512 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p1512(solver):
    assert solver.num_identical_pairs([1,2,3,1,1,3]) == 4
    assert solver.num_identical_pairs([1,1,1,1]) == 6
    assert solver.num_identical_pairs([1,2,3]) == 0