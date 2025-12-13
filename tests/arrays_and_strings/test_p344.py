import pytest
from src.arrays_and_strings.p344 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p344(solver):
    solver.reverse_string(["h","e","l","l","o"])
    assert solver.solution == ["o","l","l","e","h"]
    
    solver.reverse_string(["H","a","n","n","a","h"])
    assert solver.solution == ["h","a","n","n","a","H"]