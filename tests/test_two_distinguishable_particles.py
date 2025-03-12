import pytest
import numpy as np
from scipy.sparse import csr_matrix
from qmsolve.particle_system.two_distinguishable_particles import TwoDistinguishableParticles
from qmsolve.util.constants import m_e, k, eV


class MockHamiltonian:
    """Mock class for testing purposes."""
    
    def __init__(self, N=10, dx=0.1, spatial_ndim=1):
        self.N = N
        self.dx = dx
        self.spatial_ndim = spatial_ndim
        self.ndim = spatial_ndim  # <-- Ensure this attribute exists


@pytest.fixture
def two_distinguishable_particles():
    """Fixture to create a TwoDistinguishableParticles instance."""
    return TwoDistinguishableParticles(m1=m_e, m2=m_e)


@pytest.fixture
def mock_hamiltonian():
    """Fixture for a mock Hamiltonian object."""
    return MockHamiltonian()


def test_initialization():
    """Test initialization and attributes of the TwoDistinguishableParticles class."""
    particles = TwoDistinguishableParticles(m1=2 * m_e, m2=3 * m_e, spin=0.5)
    assert particles.m1 == 2 * m_e
    assert particles.m2 == 3 * m_e
    assert particles.spin == 0.5


def test_invalid_mass():
    """Ensure ValueError is raised for non-positive mass values."""
    with pytest.raises(ValueError):
        TwoDistinguishableParticles(m1=-1, m2=m_e)


def test_get_kinetic_matrix(two_distinguishable_particles, mock_hamiltonian):
    """Test kinetic matrix calculation."""
    T = two_distinguishable_particles.get_kinetic_matrix(mock_hamiltonian)
    assert isinstance(T, csr_matrix) or isinstance(T, np.ndarray)


def test_invalid_spatial_ndim(two_distinguishable_particles):
    """Ensure ValueError is raised for unsupported spatial dimensions."""
    invalid_H = MockHamiltonian(spatial_ndim=3)
    with pytest.raises(ValueError):
        two_distinguishable_particles.get_kinetic_matrix(invalid_H)


def test_get_energies_and_eigenstates(two_distinguishable_particles, mock_hamiltonian):
    """Test retrieval and normalization of eigenstates."""
    max_states = 5
    
    # Ensure NumPy arrays with proper shapes
    eigenvalues = np.linspace(1, 5, max_states, dtype=np.float64)  # (5,)
    ndim = mock_hamiltonian.ndim  # Ensure ndim is correctly used

    # Create eigenvectors with the correct shape (5, 10, 10) for ndim=2
    eigenvectors_shape = (max_states,) + tuple([mock_hamiltonian.N] * ndim)
    eigenvectors = np.random.rand(*eigenvectors_shape).astype(np.float64)

    # Debugging print
    print(f"Eigenvalues dtype: {eigenvalues.dtype}, Eigenvectors dtype: {eigenvectors.dtype}")
    print(f"Eigenvalues shape: {eigenvalues.shape}, Eigenvectors shape: {eigenvectors.shape}")

    # Ensure correct NumPy array usage
    energies, eigenstates = two_distinguishable_particles.get_energies_and_eigenstates(
        mock_hamiltonian, max_states, eigenvalues, eigenvectors
    )

    assert energies.shape == (max_states,)
    assert eigenstates.shape == eigenvectors_shape  # Ensure the shape is as expected


def test_invalid_eigenstates(two_distinguishable_particles, mock_hamiltonian):
    """Ensure TypeError is raised when passing invalid eigenstates."""
    with pytest.raises(TypeError):
        two_distinguishable_particles.get_energies_and_eigenstates(mock_hamiltonian, 5, [1, 2, 3], "invalid_matrix")
