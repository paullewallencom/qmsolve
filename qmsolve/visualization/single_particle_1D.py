import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from .visualization import Visualization

class VisualizationSingleParticle1D(Visualization):
    def __init__(self, eigenstates):
        """Initialize the visualization class with eigenstates."""
        self.eigenstates = eigenstates

    def plot_eigenstate(self, k, xlim=None, show_imaginary_part=False):
        """Plot the eigenstate of a single particle in 1D."""
        eigenstates_array = getattr(self.eigenstates, "eigenvectors", None)
        energies = getattr(self.eigenstates, "eigenvalues", None)

        if eigenstates_array is None or energies is None:
            raise AttributeError("Eigenstates object does not have expected attributes.")

        plt.style.use("dark_background")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_xlabel("x [Å]")
        ax.set_title(r"$\psi(x)$")

        x = np.linspace(-self.eigenstates.extent / 2, self.eigenstates.extent / 2, self.eigenstates.N)
        ax.plot(x, np.real(eigenstates_array[k]), label=r'$Re|\psi(x)|$')
        ax.plot(x, np.abs(eigenstates_array[k]), label=r'$|\psi(x)|$', color='white')
        ax.legend()
        plt.show()

    def animate(self, seconds_per_eigenstate=0.5, fps=20, max_states=2, save_animation=False):
        """Animate eigenstates over time."""
        fig, ax = plt.subplots()
        ax.set_title("Eigenstate Animation")
        ax.set_xlabel("x [Å]")

        x = np.linspace(-self.eigenstates.extent / 2, self.eigenstates.extent / 2, self.eigenstates.N)
        eigenstates_array = self.eigenstates.eigenvectors[:max_states]

        # Ensure eigenstates are valid
        if eigenstates_array.size == 0:
            raise ValueError("Eigenstates array is empty. Ensure it is properly initialized.")

        # Fix: Explicitly check if plot returns a valid line object
        plot_lines = ax.plot(x, np.zeros_like(x), lw=2)
        if not plot_lines:
            raise RuntimeError("ax.plot() did not return a valid Line2D object.")
        line = plot_lines[0]  # Extract the first line

        def init():
            """Initialize the animation by setting an empty plot."""
            line.set_data(x, np.zeros_like(x))
            return line,

        def update(frame):
            """Update the animation frame with new eigenstate data."""
            if frame >= len(eigenstates_array):
                return line,
            line.set_data(x, np.real(eigenstates_array[frame]))
            return line,

        ani = animation.FuncAnimation(fig, update, frames=min(max_states, len(eigenstates_array)), init_func=init, blit=True)

        if save_animation:
            ani.save("eigenstate_animation.mp4", fps=fps)
        else:
            plt.show()

    def superpositions(self, states, contrast_vals=[0.1, 0.25]):
        """Concrete implementation to satisfy the abstract method."""
        print("Superposition visualization is not implemented yet.")
