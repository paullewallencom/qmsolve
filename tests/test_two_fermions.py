import pytest
import numpy as np
from qmsolve.particle_system.two_fermions import TwoFermions
from qmsolve import Eigenstates


class MockHamiltonian:
    """Mocked Hamiltonian for unit testing."""
    def __init__(self):
        self.N = 10  # Number of grid points
        self.dx = 0.1  # Grid spacing
        self.extent = 5.0  # System extent
        self.spatial_ndim = 2  # Number of spatial dimensions


@pytest.fixture
def two_fermions():
    return TwoFermions()


@pytest.fixture
def mock_hamiltonian():
    return MockHamiltonian()


def test_get_eigenstates_valid(two_fermions, mock_hamiltonian):
    """Test valid eigenstate generation."""
    max_states = 5
    eigenvalues = np.array(np.linspace(1, 5, max_states), dtype=np.float64)
    eigenvectors = np.random.rand(max_states, mock_hamiltonian.N, mock_hamiltonian.N)

    # Ensure antisymmetry
    for i in range(max_states):
        eigenvectors[i] = 0.5 * (eigenvectors[i] - eigenvectors[i].T)

    eigenstates = two_fermions.get_eigenstates(mock_hamiltonian, max_states, eigenvalues, eigenvectors)
    assert eigenstates is not None
    assert len(eigenstates.eigenvalues) == max_states


def test_get_eigenstates_invalid_shapes(two_fermions, mock_hamiltonian):
    """Test invalid eigenvector reshaping."""
    max_states = 5
    eigenvalues = np.linspace(1, 5, max_states)
    eigenvectors = np.random.rand(mock_hamiltonian.N, max_states)  # Wrong shape

    with pytest.raises(ValueError, match="Eigenvectors must have shape"):
        two_fermions.get_eigenstates(mock_hamiltonian, max_states, eigenvalues, eigenvectors)


def test_get_eigenstates_invalid_types(two_fermions, mock_hamiltonian):
    """Test invalid input types."""
    max_states = "five"
    eigenvalues = [1, 2, 3, 4, 5]
    eigenvectors = np.random.rand(5, 10, 10)

    with pytest.raises(ValueError):
        two_fermions.get_eigenstates(mock_hamiltonian, max_states, eigenvalues, eigenvectors)


def test_get_eigenstates_antisymmetry(two_fermions, mock_hamiltonian):
    """Test that eigenstates maintain antisymmetry."""
    max_states = 3
    eigenvalues = np.linspace(1, 3, max_states)
    eigenvectors = np.random.rand(max_states, mock_hamiltonian.N, mock_hamiltonian.N)

    # Manually enforce antisymmetry
    for i in range(max_states):
        eigenvectors[i] = 0.5 * (eigenvectors[i] - eigenvectors[i].T)

    eigenstates = two_fermions.get_eigenstates(mock_hamiltonian, max_states, eigenvalues, eigenvectors)

    for eig_vec in eigenstates.eigenvectors:
        assert np.allclose(eig_vec, -eig_vec.T, atol=1e-8), "Eigenvectors must be antisymmetric."


def test_get_eigenstates_empty(two_fermions, mock_hamiltonian):
    """Test case where no eigenstates are added."""
    max_states = 3
    eigenvalues = np.array([0, 0, 0])  # Degenerate case
    eigenvectors = np.zeros((max_states, mock_hamiltonian.N, mock_hamiltonian.N))

    eigenstates = two_fermions.get_eigenstates(mock_hamiltonian, max_states, eigenvalues, eigenvectors)

    assert len(eigenstates.eigenvalues) == max_states
    assert len(eigenstates.eigenvectors) == max_states
