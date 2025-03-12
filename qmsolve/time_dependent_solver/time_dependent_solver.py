import numpy as np
from .split_step import SplitStep
from .crank_nicolson import CrankNicolson


class TimeSimulation:
    """
    Manages time evolution of a quantum system using numerical solvers.
    """

    def __init__(self, hamiltonian, method="split-step"):
        """
        Initializes the time simulation with the selected solver.

        Args:
            hamiltonian: The Hamiltonian object defining the system.
            method (str): The numerical solver to use ("split-step" or "crank-nicolson").
        """
        self.H = hamiltonian

        # Ensure Vgrid is properly structured
        if hasattr(self.H, "Vgrid") and isinstance(self.H.Vgrid, np.ndarray):
            self.Vgrid = self.H.Vgrid
        else:
            self.Vgrid = self.H.Vgrid.reshape(self.H.N, self.H.N)

        self.Vmin = np.amin(self.Vgrid)  # Ensure Vmin is correctly derived

        self.method = self.select_solver(method)

    def select_solver(self, method):
        """
        Selects the appropriate solver based on the provided method.

        Args:
            method (str): Solver method to use.

        Returns:
            An instance of the selected solver.
        """
        solvers = {
            "split-step": SplitStep(self),
            "crank-nicolson": CrankNicolson(self),
        }

        if method not in solvers:
            raise NotImplementedError(f"Method '{method}' is not implemented.")

        return solvers[method]

    def run(self, wavefunction, total_time, dt, store_steps=1):
        """
        Runs the time evolution using the selected solver.

        Args:
            wavefunction: Initial wavefunction.
            total_time: Total simulation time.
            dt: Time step for evolution.
            store_steps: Frequency of storing wavefunction snapshots.
        """
        return self.method.run(wavefunction, total_time, dt, store_steps)

    def store_wavefunction(self, wavefunction):
        """
        Placeholder for storing wavefunction states during evolution.

        Args:
            wavefunction: The current wavefunction state.
        """
        # This function can be extended for data logging or visualization
        pass
