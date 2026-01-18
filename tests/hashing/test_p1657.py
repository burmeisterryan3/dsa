import pytest
from src.hashing.p1657 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p1657(solver):
    assert solver.close_strings("abc", "bca") == True
    assert solver.close_strings("a", "aa") == False
    assert solver.close_strings("cabbba", "abbccc") == True
    assert solver.close_strings("uau", "ssx") == False