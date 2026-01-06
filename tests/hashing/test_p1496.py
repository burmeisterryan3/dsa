import pytest
from src.hashing.p1496 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p1496(solver):
    assert solver.is_path_crossing("NES") == False
    assert solver.is_path_crossing("NESWW") == True