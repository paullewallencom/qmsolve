import pytest
import numpy as np
from qmsolve.time_dependent_solver.time_dependent_solver import TimeSimulation
from qmsolve.hamiltonian import Hamiltonian


class MockParticleSystem:
    """Mock Particle System for testing."""
    def get_kinetic_matrix(self, H):
        return np.eye(H.N)

    def compute_momentum_space(self, H):
        """Mock momentum space computation."""
        pass  # No-op for testing

    @property
    def p2(self):
        """Mock p2 attribute to avoid attribute error."""
        return np.zeros(10)


def mock_potential(particle_system):
    """Mock potential function returning a valid 1D potential array."""
    return np.zeros(10)  # Ensure it's 1D


@pytest.fixture
def mock_hamiltonian():
    """Creates a mock Hamiltonian object with a valid potential grid."""
    return Hamiltonian(MockParticleSystem(), mock_potential, 10, 5.0, 1, "grid")


def test_time_simulation_initialization(mock_hamiltonian):
    """Test initialization of TimeSimulation with different methods."""
    sim_split_step = TimeSimulation(mock_hamiltonian, method="split-step")
    sim_crank_nicolson = TimeSimulation(mock_hamiltonian, method="crank-nicolson")

    assert sim_split_step.method is not None
    assert sim_crank_nicolson.method is not None


def test_time_simulation_invalid_method(mock_hamiltonian):
    """Test that an invalid solver raises an error."""
    with pytest.raises(NotImplementedError):
        TimeSimulation(mock_hamiltonian, method="invalid-method")
