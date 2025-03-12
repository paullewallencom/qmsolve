import pytest
import numpy as np
from qmsolve.eigenstates import Eigenstates

@pytest.fixture
def sample_eigenstates():
    """Creates a sample Eigenstates object for testing."""
    eigenvalues = np.array([1.0, 2.0, 3.0])
    eigenvectors = np.array([[0.5, 0.4, 0.3],
                              [0.6, 0.5, 0.4],
                              [0.7, 0.6, 0.5]])
    extent = 10.0
    N = 3
    potential_type = "grid"
    return Eigenstates(eigenvalues, eigenvectors, extent, N, potential_type)

def test_initialization(sample_eigenstates):
    """Test that Eigenstates initializes correctly."""
    assert isinstance(sample_eigenstates.eigenvalues, np.ndarray)
    assert isinstance(sample_eigenstates.eigenvectors, np.ndarray)
    assert sample_eigenstates.extent == 10.0
    assert sample_eigenstates.N == 3
    assert sample_eigenstates.potential_type == "grid"

def test_get_ground_state(sample_eigenstates):
    """Test getting the ground state."""
    energy, wavefunction = sample_eigenstates.get_ground_state()
    assert energy == 1.0
    assert wavefunction.shape == (3,)

def test_get_excited_state(sample_eigenstates):
    """Test getting an excited state."""
    energy, wavefunction = sample_eigenstates.get_excited_state(2)
    assert energy == 3.0
    assert wavefunction.shape == (3,)

def test_excited_state_out_of_bounds(sample_eigenstates):
    """Test that getting an out-of-bounds excited state raises an error."""
    with pytest.raises(IndexError):
        sample_eigenstates.get_excited_state(10)

def test_normalize_eigenvectors(sample_eigenstates):
    """Test that eigenvectors get normalized."""
    sample_eigenstates.normalize_eigenvectors()
    norms = np.linalg.norm(sample_eigenstates.eigenvectors, axis=0)
    assert np.allclose(norms, 1.0)

def test_invalid_initialization():
    """Test that initialization fails with invalid inputs."""
    with pytest.raises(TypeError):
        Eigenstates(None, None, None, None, None)  # Invalid inputs

    with pytest.raises(ValueError):
        Eigenstates(np.array([]), np.array([]), 5.0, 10, "grid")  # Empty arrays

    with pytest.raises(ValueError):
        Eigenstates(np.array([1]), np.array([[1]]), -5.0, 10, "grid")  # Negative extent

    with pytest.raises(ValueError):
        Eigenstates(np.array([1]), np.array([[1]]), 5.0, -10, "grid")  # Negative N

    with pytest.raises(ValueError):
        Eigenstates(np.array([1]), np.array([[1]]), 5.0, 10, "invalid_type")  # Invalid potential type
