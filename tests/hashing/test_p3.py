import pytest
from src.hashing.p3 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p3(solver):
    assert solver.length_of_longest_substring("abcabcbb") == 3
    assert solver.length_of_longest_substring("bbbbb") == 1
    assert solver.length_of_longest_substring("pwwkew") == 3
    assert solver.length_of_longest_substring("aab") == 2
    assert solver.length_of_longest_substring(" ") == 1
    assert solver.length_of_longest_substring("au") == 2
    assert solver.length_of_longest_substring("cdd") == 2
    assert solver.length_of_longest_substring("abba") == 2

def test_p3_window(solver):
    assert solver.length_of_longest_substring_window("abcabcbb") == 3
    assert solver.length_of_longest_substring_window("bbbbb") == 1
    assert solver.length_of_longest_substring_window("pwwkew") == 3
    assert solver.length_of_longest_substring_window("aab") == 2
    assert solver.length_of_longest_substring_window(" ") == 1
    assert solver.length_of_longest_substring_window("au") == 2
    assert solver.length_of_longest_substring_window("cdd") == 2
    assert solver.length_of_longest_substring_window("abba") == 2