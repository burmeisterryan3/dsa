import pytest
from src.arrays_and_strings.p557 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p557(solver):
    assert solver.reverse_words("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert solver.reverse_words("Mr Ding") == "rM gniD"

def test_p557_pythonic(solver):
    assert solver.reverse_words("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert solver.reverse_words("Mr Ding") == "rM gniD"