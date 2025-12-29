import pytest
from src.hashing.p268 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p268_option_1(solver):
    assert solver.missing_number_option_1([3,0,1]) == 2
    assert solver.missing_number_option_1([0,1]) == 2
    assert solver.missing_number_option_1([9,6,4,2,3,5,7,0,1]) == 8

def test_p268_option_2(solver):
    assert solver.missing_number_option_2([3,0,1]) == 2
    assert solver.missing_number_option_2([0,1]) == 2
    assert solver.missing_number_option_2([9,6,4,2,3,5,7,0,1]) == 8

def test_p268_better_1(solver):
    assert solver.missing_number_better_1([3,0,1]) == 2
    assert solver.missing_number_better_1([0,1]) == 2
    assert solver.missing_number_better_1([9,6,4,2,3,5,7,0,1]) == 8

def test_p268_better_2(solver):
    assert solver.missing_number_better_2([3,0,1]) == 2
    assert solver.missing_number_better_2([0,1]) == 2
    assert solver.missing_number_better_2([9,6,4,2,3,5,7,0,1]) == 8