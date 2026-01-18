import pytest
from src.hashing.p205 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p205(solver):
    assert solver.is_isomorphic("egg", "add") == True
    assert solver.is_isomorphic("foo", "bar") == False
    assert solver.is_isomorphic("paper", "title") == True
    assert solver.is_isomorphic("badc", "baba") == False