import pytest
from src.hashing.p2225 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p2225(solver):
    assert solver.find_winners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]) == [[1,2,10],[4,5,7,8]]
    assert solver.find_winners([[2,3],[1,3],[5,4],[6,4]]) == [[1,2,5,6],[]]