import pytest
from src.hashing.p1436 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p1436(solver):
    assert solver.dest_city([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]) == "Sao Paulo"
    assert solver.dest_city([["B","C"],["D","B"],["C","A"]]) == "A"
    assert solver.dest_city([["A","Z"]]) == "Z"