import pytest
from src.arrays_and_strings.p977 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p977(solver):
    assert solver.sorted_squares([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert solver.sorted_squares([-7,-3,2,3,11])  == [4,9,9,49,121]
    assert solver.sorted_squares([-7,-5,-3,-2]) == [4,9,25,49]
    assert solver.sorted_squares([-7,-5,-3,-2,0]) == [0,4,9,25,49]

def test_p977_alt(solver):
    assert solver.sorted_squares_alt([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert solver.sorted_squares_alt([-7,-3,2,3,11])  == [4,9,9,49,121]
    assert solver.sorted_squares_alt([-7,-5,-3,-2]) == [4,9,25,49]
    assert solver.sorted_squares_alt([-7,-5,-3,-2,0]) == [0,4,9,25,49]
