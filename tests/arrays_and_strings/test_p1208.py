import pytest
from src.arrays_and_strings.p1208 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p1208_speed(solver):
    assert solver.equal_substring_speed("abcd", "bcdf", 3) == 3
    assert solver.equal_substring_speed("abcd", "cdef", 3) == 1
    assert solver.equal_substring_speed("abcd", "acde", 0) == 1
    assert solver.equal_substring_speed("abcd", "abcd", 0) == 4


def test_p1208_memory(solver):
    assert solver.equal_substring_memory("abcd", "bcdf", 3) == 3
    assert solver.equal_substring_memory("abcd", "cdef", 3) == 1
    assert solver.equal_substring_memory("abcd", "acde", 0) == 1
    assert solver.equal_substring_memory("abcd", "abcd", 0) == 4