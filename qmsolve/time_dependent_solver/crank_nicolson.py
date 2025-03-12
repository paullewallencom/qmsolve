import numpy as np
from scipy.sparse import diags, identity
from scipy.sparse.linalg import spsolve


class CrankNicolson:
    """
    Implements the Crank-Nicolson method for time evolution in quantum mechanics.
    """

    def __init__(self, simulation):
        """
        Initializes the solver with the given simulation parameters.

        Args:
            simulation: An instance of a time-dependent quantum simulation.
        """
        self.simulation = simulation
        self.H = simulation.H
        self.dt = None
        self.A = None
        self.B = None

    def construct_matrices(self, dt):
        """
        Constructs the Crank-Nicolson matrices A and B.

        Args:
            dt: Time step for evolution.
        """
        N = self.H.N
        H_matrix = self.H.T + self.H.V
        I = identity(N, format="csr")  # Identity matrix
        factor = -0.5j * dt

        # Ensure the matrices are properly formatted for diagonal storage
        H_csr = H_matrix.tocsr()
        A = I - factor * H_csr
        B = I + factor * H_csr

        return A, B

    def run(self, wavefunction, total_time, dt, store_steps=1):
        """
        Runs the Crank-Nicolson time evolution.

        Args:
            wavefunction: Initial wavefunction.
            total_time: Total simulation time.
            dt: Time step for evolution.
            store_steps: Frequency of storing wavefunction snapshots.
        """
        self.dt = dt
        self.A, self.B = self.construct_matrices(dt)

        num_steps = int(total_time / dt)
        Ψ = wavefunction

        for step in range(num_steps):
            Ψ = spsolve(self.A, self.B @ Ψ)

            if step % store_steps == 0:
                self.simulation.store_wavefunction(Ψ)

        return Ψ
