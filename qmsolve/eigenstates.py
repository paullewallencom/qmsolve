import numpy as np

class Eigenstates:
    """Class to store eigenvalues, eigenvectors, and related attributes of a quantum system."""

    def __init__(self, eigenvalues, eigenvectors, extent, N, potential_type):
        """
        Initialize the Eigenstates class.

        Parameters:
        - eigenvalues: np.ndarray, 1D array of eigenvalues
        - eigenvectors: np.ndarray, 2D array of eigenvectors
        - extent: float, physical extent of the system
        - N: int, number of grid points
        - potential_type: str, type of potential ("grid" or "matrix")
        """

        # **Type Checking**
        if not isinstance(eigenvalues, np.ndarray) or not isinstance(eigenvectors, np.ndarray):
            raise TypeError("Eigenvalues and eigenvectors must be NumPy arrays.")
        if not isinstance(extent, (int, float)) or extent <= 0:
            raise ValueError("Extent must be a positive number.")
        if not isinstance(N, int) or N <= 0:
            raise ValueError("N must be a positive integer.")
        if potential_type not in ["grid", "matrix"]:
            raise ValueError("Potential type must be 'grid' or 'matrix'.")

        # **Empty Array Check**
        if eigenvalues.size == 0 or eigenvectors.size == 0:
            raise ValueError("Eigenvalues and eigenvectors cannot be empty.")

        self.eigenvalues = eigenvalues
        self.eigenvectors = eigenvectors
        self.extent = extent
        self.N = N
        self.potential_type = potential_type

    def get_ground_state(self):
        """Returns the ground state wavefunction and energy."""
        return self.eigenvalues[0], self.eigenvectors[:, 0]

    def get_excited_state(self, n):
        """Returns the n-th excited state wavefunction and energy."""
        if not (0 <= n < len(self.eigenvalues)):
            raise IndexError("State index out of range.")
        return self.eigenvalues[n], self.eigenvectors[:, n]

    def normalize_eigenvectors(self):
        """Normalize the eigenvectors."""
        norms = np.linalg.norm(self.eigenvectors, axis=0)
        self.eigenvectors /= norms
