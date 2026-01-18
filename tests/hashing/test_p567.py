import pytest
from src.hashing.p567 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p567(solver):
    assert solver.check_inclusion("ab","eidbaooo") == True
    assert solver.check_inclusion("ab","eidboaoo") == False
    assert solver.check_inclusion("the","chettheoo") == True

def test_p567_counter(solver):
    assert solver.check_inclusion_counter("ab","eidbaooo") == True
    assert solver.check_inclusion_counter("ab","eidboaoo") == False
    assert solver.check_inclusion_counter("the","chettheoo") == True