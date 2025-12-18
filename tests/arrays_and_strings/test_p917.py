import pytest
from src.arrays_and_strings.p917 import Solution

@pytest.fixture
def solver():
    return Solution()

def test_p917(solver):
    assert solver.reverse_only_letters("ab-cd") == "dc-ba"
    assert solver.reverse_only_letters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
    assert solver.reverse_only_letters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
    assert solver.reverse_only_letters("7_28]") == "7_28]"