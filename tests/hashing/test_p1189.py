import pytest
from src.hashing.p1189 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p1189(solver):
    assert solver.max_number_of_balloons("nlaebolko") == 1
    assert solver.max_number_of_balloons("loonbalxballpoon") == 2
    assert solver.max_number_of_balloons("leetcode") == 0