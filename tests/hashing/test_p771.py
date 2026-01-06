import pytest
from src.hashing.p771 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p771(solver):
    assert solver.num_jewels_in_stones("aA", "aAAbbbb") == 3
    assert solver.num_jewels_in_stones("z", "ZZ") == 0

def test_p771_pythonic(solver):
    assert solver.num_jewels_in_stones_pythonic("aA", "aAAbbbb") == 3
    assert solver.num_jewels_in_stones_pythonic("z", "ZZ") == 0