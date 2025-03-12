from qmsolve.eigenstates import Eigenstates
import numpy as np

class TwoBosons:
    def __init__(self):
        """Initialize the TwoBosons system."""
        pass

    def get_eigenstates(self, H, max_states: int, eigenvalues, eigenvectors):
        """
        Compute and return eigenstates for two bosons in the system.

        Args:
            H: Hamiltonian object containing system parameters.
            max_states: Maximum number of eigenstates to consider.
            eigenvalues: Eigenvalues corresponding to the eigenstates.
            eigenvectors: Eigenvectors corresponding to the eigenstates.

        Returns:
            Eigenstates: An object containing normalized eigenstates and corresponding energies.
        """

        # Ensure eigenvalues and eigenvectors are NumPy arrays
        eigenvalues = np.array(eigenvalues, dtype=np.float64)
        eigenvectors = np.array(eigenvectors, dtype=np.float64)

        # Fix potential type to "grid"
        return Eigenstates(
            eigenvalues,
            eigenvectors,
            extent=H.extent,
            N=H.N,
            potential_type="grid",  # <-- This ensures compatibility with Eigenstates
        )
