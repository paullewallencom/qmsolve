import pytest
from qmsolve.time_dependent_solver import SomeSolverClass  # Replace with actual class

@pytest.fixture
def solver():
    return SomeSolverClass()

def test_solver_initialization(solver):
    assert solver is not None
