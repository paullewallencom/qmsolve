import pytest
import numpy as np
from qmsolve.hamiltonian import Hamiltonian
from qmsolve.time_dependent_solver.crank_nicolson import CrankNicolson


class MockParticleSystem:
    """
    Mock class for particle system to provide necessary attributes for Hamiltonian.
    """

    def get_kinetic_matrix(self, H):
        """
        Generates a mock kinetic energy matrix.
        """
        return np.identity(H.N)


def mock_potential(particle_system):
    """Mock potential function returning a valid 1D potential array."""
    return np.zeros(10)  # Ensure it's 1D


@pytest.fixture
def mock_hamiltonian():
    """
    Creates a mock Hamiltonian object with a valid potential grid.
    """
    return Hamiltonian(MockParticleSystem(), mock_potential, 10, 5.0, 1, "grid")


@pytest.fixture
def mock_simulation(mock_hamiltonian):
    """
    Creates a mock simulation object with a valid Hamiltonian.
    """

    class MockSimulation:
        def __init__(self):
            self.H = mock_hamiltonian
            self.store_steps = 1
            self.Ψ = np.ones(10, dtype=np.complex128)

    return MockSimulation()


@pytest.fixture
def mock_wavefunction():
    """
    Creates a mock wavefunction.
    """
    return np.ones(10, dtype=np.complex128)


def test_crank_nicolson_initialization(mock_simulation):
    """
    Tests proper initialization of Crank-Nicolson solver.
    """
    solver = CrankNicolson(mock_simulation)
    assert solver.simulation == mock_simulation, "Solver initialization failed."


def test_crank_nicolson_run(mock_simulation, mock_wavefunction):
    """
    Tests execution of Crank-Nicolson solver.
    """
    solver = CrankNicolson(mock_simulation)
    try:
        solver.run(mock_wavefunction, total_time=1.0, dt=0.01, store_steps=5)
    except Exception as e:
        pytest.fail(f"Crank-Nicolson run failed with error: {e}")
