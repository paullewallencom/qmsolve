import numpy as np
import pytest
from qmsolve.particle_system.two_bosons import TwoBosons
from qmsolve.eigenstates import Eigenstates

class MockHamiltonian:
    def __init__(self):
        self.N = 10  # Grid size
        self.extent = 5.0  # Physical extent
        self.dx = self.extent / self.N  # Grid spacing
        self.ndim = 2  # Number of dimensions
        self.spatial_ndim = 2  # Needed for TwoBosons compatibility
        self.potential_type = "TwoIdenticalParticles2D"  # Potential type

@pytest.fixture
def hamiltonian():
    return MockHamiltonian()

@pytest.fixture
def two_bosons():
    return TwoBosons()

def test_get_eigenstates(hamiltonian, two_bosons):
    """Test that eigenstates are correctly computed."""
    max_states = 5

    # Ensure NumPy arrays with proper shapes
    eigenvalues = np.linspace(1, 5, max_states, dtype=np.float64)  # (5,)
    eigenvectors = np.random.rand(max_states, hamiltonian.N, hamiltonian.N).astype(np.float64)  # (5,10,10)

    # **Ensure eigenvectors is a properly structured NumPy array**
    eigenvectors = np.array(eigenvectors, dtype=np.float64)  # Explicitly force conversion

    # Debugging print
    print(f"Eigenvalues dtype: {eigenvalues.dtype}, Eigenvectors dtype: {eigenvectors.dtype}")
    print(f"Eigenvalues shape: {eigenvalues.shape}, Eigenvectors shape: {eigenvectors.shape}")

    # **Ensure correct NumPy array usage**
    eigenstates = two_bosons.get_eigenstates(hamiltonian, max_states, eigenvalues, eigenvectors)

    # Assertions for debugging
    assert isinstance(eigenstates, Eigenstates), "get_eigenstates() should return an Eigenstates instance"
    assert isinstance(eigenstates.eigenvalues, np.ndarray), "Eigenvalues should be a NumPy array"
    assert isinstance(eigenstates.eigenvectors, np.ndarray), "Eigenvectors should be a NumPy array"
    assert eigenstates.eigenvalues.shape == (max_states,), "Eigenvalues shape mismatch"
    assert eigenstates.eigenvectors.shape == (max_states, hamiltonian.N, hamiltonian.N), "Eigenvectors shape mismatch"
