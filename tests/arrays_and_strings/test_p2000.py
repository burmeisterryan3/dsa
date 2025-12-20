
import pytest
from src.arrays_and_strings.p2000 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p2000(solver):
    assert solver.reverse_prefix("abcdefd", "d") == "dcbaefd"
    assert solver.reverse_prefix("xyxzxe", "z") == "zxyxxe"
    assert solver.reverse_prefix("abcd", "z") == "abcd"

def test_p2000_pythonic(solver):
    assert solver.reverse_prefix_pythonic("abcdefd", "d") == "dcbaefd"
    assert solver.reverse_prefix_pythonic("xyxzxe", "z") == "zxyxxe"
    assert solver.reverse_prefix_pythonic("abcd", "z") == "abcd"