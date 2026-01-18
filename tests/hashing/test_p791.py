import pytest
from src.hashing.p791 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p791(solver):
    assert solver.custom_sort_string("cba", "abcd") in ["dcba", "cdba", "cbda", "cbad"]
    assert solver.custom_sort_string("bcafg", "abcd") in ["dbca", "bdca", "bcda", "bcad"]

def test_p791_compare(solver):
    assert solver.custom_sort_string_compare("cba", "abcd") in ["dcba", "cdba", "cbda", "cbad"]
    assert solver.custom_sort_string_compare("bcafg", "abcd") in ["dbca", "bdca", "bcda", "bcad"]