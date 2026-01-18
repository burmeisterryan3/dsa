import pytest
from src.hashing.p290 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p290(solver):
    assert solver.word_pattern("abba", "dog cat cat dog") == True
    assert solver.word_pattern("aaaa", "dog cat cat dog") == False
    assert solver.word_pattern("aaa", "aa aa aa aa") == False