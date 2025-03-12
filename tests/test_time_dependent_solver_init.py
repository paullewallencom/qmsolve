import pytest
import time_dependent_solver

def test_imports():
    """Test that TimeSimulation can be accessed via time_dependent_solver."""
    assert hasattr(time_dependent_solver, "TimeSimulation")
