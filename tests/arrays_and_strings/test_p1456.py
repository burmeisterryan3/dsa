import pytest
from src.arrays_and_strings.p1456 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p1456(solver):
    assert solver.max_vowels("abciiidef", 3) == 3
    assert solver.max_vowels("aeiou", 2) == 2
    assert solver.max_vowels("leetcode", 3) == 2