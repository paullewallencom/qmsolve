import pytest
import numpy as np
from qmsolve.particle_system.two_particles import TwoParticles


class MockHamiltonian:
    """Mock Hamiltonian class for testing."""
    def __init__(self, spatial_ndim=1, N=10, extent=5.0, dx=0.5):
        self.spatial_ndim = spatial_ndim
        self.N = N
        self.extent = extent
        self.dx = dx
        self.ndim = None


@pytest.fixture
def two_particles():
    """Fixture to create a TwoParticles instance."""
    return TwoParticles()


@pytest.fixture
def mock_hamiltonian():
    """Fixture to create a MockHamiltonian instance."""
    return MockHamiltonian()


def test_get_observables_1d(two_particles, mock_hamiltonian):
    """Test get_observables method for 1D case."""
    two_particles.get_observables(mock_hamiltonian)
    assert hasattr(two_particles, "x1") and hasattr(two_particles, "x2")
    assert mock_hamiltonian.ndim == 2


def test_get_observables_2d(two_particles):
    """Test get_observables method for 2D case."""
    H = MockHamiltonian(spatial_ndim=2)
    two_particles.get_observables(H)
    assert hasattr(two_particles, "x1") and hasattr(two_particles, "y1")
    assert hasattr(two_particles, "x2") and hasattr(two_particles, "y2")
    assert H.ndim == 4


def test_get_observables_invalid(two_particles):
    """Test get_observables with an invalid spatial dimension."""
    H = MockHamiltonian(spatial_ndim=3)
    with pytest.raises(NotImplementedError):
        two_particles.get_observables(H)


def test_compute_momentum_space_1d(two_particles, mock_hamiltonian):
    """Test momentum space computation for 1D case."""
    two_particles.compute_momentum_space(mock_hamiltonian)
    assert hasattr(two_particles, "p1") and hasattr(two_particles, "p2")
    assert hasattr(two_particles, "p_squared")


def test_compute_momentum_space_2d(two_particles):
    """Test momentum space computation for 2D case (should raise NotImplementedError)."""
    H = MockHamiltonian(spatial_ndim=2)
    with pytest.raises(NotImplementedError):
        two_particles.compute_momentum_space(H)


def test_get_kinetic_matrix_1d(two_particles, mock_hamiltonian):
    """Test kinetic matrix generation for 1D case."""
    T = two_particles.get_kinetic_matrix(mock_hamiltonian)
    assert T.shape == (mock_hamiltonian.N**2, mock_hamiltonian.N**2)


def test_get_kinetic_matrix_2d(two_particles):
    """Test kinetic matrix generation for 2D case (should raise NotImplementedError)."""
    H = MockHamiltonian(spatial_ndim=3)
    with pytest.raises(NotImplementedError):
        two_particles.get_kinetic_matrix(H)
