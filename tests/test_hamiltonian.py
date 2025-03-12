import pytest
import numpy as np
from qmsolve.hamiltonian import Hamiltonian
from scipy.sparse import diags


class MockParticleSystem:
    """Mock class for testing Hamiltonian."""
    def __init__(self):
        self.H = None

    def get_kinetic_matrix(self, hamiltonian):
        """Mock kinetic matrix as an identity matrix."""
        return diags([np.ones(hamiltonian.N ** hamiltonian.spatial_ndim)], [0])

    def get_observables(self, hamiltonian):
        """Mock observables setup for Hamiltonian."""
        pass


@pytest.fixture
def hamiltonian():
    """Fixture to create a Hamiltonian instance with a mock potential."""
    N = 10
    extent = 5.0
    spatial_ndim = 3

    def mock_potential(particle_system):
        """Mock potential function returning a zero potential grid."""
        return np.zeros((N ** spatial_ndim,))

    return Hamiltonian(
        particles=MockParticleSystem(),
        potential=mock_potential,
        N=N,
        extent=extent,
        spatial_ndim=spatial_ndim,
        potential_type="grid"
    )


def test_initialization(hamiltonian):
    """Test Hamiltonian initialization."""
    assert hamiltonian.N == 10
    assert hamiltonian.extent == 5.0
    assert hamiltonian.spatial_ndim == 3
    assert hamiltonian.potential_type == "grid"


def test_get_potential_matrix(hamiltonian):
    """Test potential matrix calculation."""
    potential_matrix = hamiltonian.get_potential_matrix()
    assert potential_matrix.shape[0] == hamiltonian.N ** hamiltonian.spatial_ndim


def test_solve_eigsh(hamiltonian):
    """Test solving Hamiltonian using eigsh method."""
    eigenvalues, eigenvectors = hamiltonian.solve(method="eigsh", max_states=3)
    assert len(eigenvalues) == 3
    assert eigenvectors.shape[1] == 3


def test_solve_lobpcg(hamiltonian):
    """Test solving Hamiltonian using lobpcg method."""
    eigenvalues, eigenvectors = hamiltonian.solve(method="lobpcg", max_states=3)
    assert len(eigenvalues) == 3
    assert eigenvectors.shape[1] == 3


def test_solve_invalid_method(hamiltonian):
    """Test invalid solver method raises an error."""
    with pytest.raises(ValueError, match="Invalid solver method"):
        hamiltonian.solve(method="invalid_method", max_states=3)
