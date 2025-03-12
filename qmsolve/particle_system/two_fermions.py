import numpy as np
from ..util.constants import eV
from qmsolve.eigenstates import Eigenstates
from .two_particles import TwoParticles


class TwoFermions(TwoParticles):
    """Represents two fermions in a quantum system."""

    def get_eigenstates(self, H, max_states, eigenvalues, eigenvectors):
        """
        Compute eigenstates for two fermions, ensuring antisymmetry.

        Args:
            H: Hamiltonian object containing system parameters.
            max_states (int): Number of eigenstates to process.
            eigenvalues (np.ndarray): Array of eigenvalues.
            eigenvectors (np.ndarray): Matrix of eigenvectors.

        Returns:
            Eigenstates: Normalized antisymmetric eigenstates.
        """
        # **Input validation**
        if not isinstance(eigenvalues, np.ndarray):
            eigenvalues = np.array(eigenvalues, dtype=np.float64)
        if not isinstance(eigenvectors, np.ndarray):
            eigenvectors = np.array(eigenvectors, dtype=np.float64)

        if not isinstance(max_states, int) or max_states <= 0:
            raise ValueError("max_states must be a positive integer.")
        if not hasattr(H, 'N') or not hasattr(H, 'dx') or not hasattr(H, 'spatial_ndim'):
            raise AttributeError("Hamiltonian object must have N, dx, and spatial_ndim attributes.")

        # Ensure eigenvectors are properly shaped
        expected_shape = (max_states, H.N, H.N)
        if eigenvectors.shape != expected_shape:
            raise ValueError(f"Eigenvectors must have shape {expected_shape}, but got {eigenvectors.shape}")

        # Normalize eigenstates
        eigenvectors /= np.sqrt(H.dx ** H.spatial_ndim)

        # Ensure antisymmetry of eigenvectors
        for i in range(max_states):
            if not np.allclose(eigenvectors[i], -eigenvectors[i].T, atol=1e-8):
                raise ValueError("Eigenvectors must be antisymmetric for fermions.")

        # Convert to Eigenstates object
        return Eigenstates(eigenvalues / eV, eigenvectors, H.extent, H.N, "grid")  # Fixed `potential_type`
