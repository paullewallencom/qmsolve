import pytest
import numpy as np
from qmsolve.particle_system import MockParticleSystem

class MockHamiltonian:
    """Mock Hamiltonian for testing."""
    def __init__(self, N=5):
        self.N = N

@pytest.fixture
def mock_particle_system():
    """Fixture to create a MockParticleSystem instance."""
    return MockParticleSystem(num_particles=2, mass=1.5)

@pytest.fixture
def mock_hamiltonian():
    """Fixture to create a MockHamiltonian instance."""
    return MockHamiltonian(N=5)

def test_initialization(mock_particle_system):
    """Test the initialization of the MockParticleSystem."""
    assert mock_particle_system.num_particles == 2
    assert mock_particle_system.mass == 1.5

def test_kinetic_matrix(mock_particle_system, mock_hamiltonian):
    """Test the kinetic energy matrix method."""
    kinetic_matrix = mock_particle_system.get_kinetic_matrix(mock_hamiltonian)
    assert isinstance(kinetic_matrix, np.ndarray)
    assert kinetic_matrix.shape == (5, 5)
    assert np.allclose(kinetic_matrix, np.eye(5))
