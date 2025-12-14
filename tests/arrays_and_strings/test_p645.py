import pytest
from src.arrays_and_strings.p645 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_643(solver):
    assert solver.find_error_nums([1,2,2,4]) == [2, 3]
    assert solver.find_error_nums([1,1]) == [1, 2]
    assert solver.find_error_nums([1,3,3,4]) == [3, 2]
    assert solver.find_error_nums([3,2,2]) == [2, 1]
    assert solver.find_error_nums([3,2,3,4,6,5]) == [3,1]