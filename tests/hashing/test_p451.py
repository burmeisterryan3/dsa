import pytest
from src.hashing.p451 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p451(solver):
    assert solver.frequency_sort("tree") in ["eert", "eetr"]
    assert solver.frequency_sort("cccaaa") in ["aaaccc", "cccaaa"]
    assert solver.frequency_sort("Aabb") in ["bbAa", "bbaA"]