import pytest
from src.arrays_and_strings.p303 import Solution

def test_p303():
    solver = Solution([[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]])
    assert solver.sum_range(0,2) == 1
    assert solver.sum_range(2,5) == -1
    assert solver.sum_range(0,5) == -3