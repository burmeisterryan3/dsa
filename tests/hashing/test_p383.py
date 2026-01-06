import pytest
from src.hashing.p383 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p383(solver):
    assert solver.can_construct("a", "b") == False
    assert solver.can_construct("aa", "ab") == False
    assert solver.can_construct("aa", "aab") == True
    assert solver.can_construct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj") == True

def test_p383_pythonic(solver):
    assert solver.can_construct_pythonic("a", "b") == False
    assert solver.can_construct_pythonic("aa", "ab") == False
    assert solver.can_construct_pythonic("aa", "aab") == True
    assert solver.can_construct_pythonic("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj") == True