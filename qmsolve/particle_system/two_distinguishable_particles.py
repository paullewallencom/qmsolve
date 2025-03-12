import numpy as np
from scipy.sparse import diags, kron, eye
from .two_particles import TwoParticles
from ..util.constants import m_e, k, eV
from ..eigenstates import Eigenstates


class TwoDistinguishableParticles(TwoParticles):
    """
    Represents a system of two distinguishable particles in a potential well.
    """

    def __init__(self, m1: float = m_e, m2: float = m_e, spin: float = None):
        """
        Initialize two distinguishable particles.

        Parameters:
        - m1 (float): Mass of the first particle (default: electron mass).
        - m2 (float): Mass of the second particle (default: electron mass).
        - spin (float, optional): Spin of the system.
        """
        if m1 <= 0 or m2 <= 0:
            raise ValueError("Masses must be positive values.")
        
        self.m1 = m1
        self.m2 = m2
        self.spin = spin

    def get_kinetic_matrix(self, H) -> np.ndarray:
        """
        Compute the kinetic energy matrix.

        Parameters:
        - H: Hamiltonian object containing system parameters.

        Returns:
        - np.ndarray: The kinetic energy matrix.
        """
        if not hasattr(H, "N") or not hasattr(H, "dx") or not hasattr(H, "spatial_ndim"):
            raise AttributeError("Hamiltonian object must have attributes 'N', 'dx', and 'spatial_ndim'.")

        I = eye(H.N)
        T_ = diags([-2.0, 1.0, 1.0], [0, -1, 1], shape=(H.N, H.N)) * -k / (H.dx**2)

        if H.spatial_ndim == 1:
            return kron(T_ / self.m1, I) + kron(I, T_ / self.m2)
        elif H.spatial_ndim == 2:
            return (
                kron(T_ / self.m1, I, I, I)
                + kron(I, T_ / self.m1, I, I)
                + kron(I, I, T_ / self.m2, I)
                + kron(I, I, I, T_ / self.m2)
            )
        else:
            raise ValueError("Only spatial dimensions of 1 or 2 are supported.")

    def get_energies_and_eigenstates(
        self, H, max_states: int, eigenvalues: np.ndarray, eigenvectors: np.ndarray
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Process and normalize eigenstates and convert energies to eV.

        Parameters:
        - H: Hamiltonian object containing system parameters.
        - max_states (int): Number of eigenstates to process.
        - eigenvalues (np.ndarray): Array of eigenvalues.
        - eigenvectors (np.ndarray): Matrix of eigenvectors.

        Returns:
        - tuple[np.ndarray, np.ndarray]: Normalized eigenstates and energies in eV.
        """
        if not isinstance(eigenvalues, np.ndarray) or not isinstance(eigenvectors, np.ndarray):
            raise TypeError("Eigenvalues and eigenvectors must be NumPy arrays.")

        eigenstates = eigenvectors.T.reshape((max_states, *([H.N] * H.ndim)))
        assert eigenvectors.size == np.prod([max_states] + [H.N] * H.ndim), "Mismatch in eigenvector shape."
        eigenstates /= np.sqrt(H.dx ** H.ndim)  # Normalize eigenstates
        return eigenvalues / eV, eigenstates
