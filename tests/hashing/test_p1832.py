import pytest
from src.hashing.p1832 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p1832(solver):
    assert solver.check_if_pangram("thequickbrownfoxjumpsoverthelazydog")
    assert not solver.check_if_pangram("leetcode")