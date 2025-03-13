import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from .visualization import Visualization
from ..util.colour_functions import complex_to_rgb, complex_to_rgba
from ..util.constants import Å

class VisualizationSingleParticle2D(Visualization):
    def __init__(self, eigenstates):
        self.eigenstates = eigenstates

    def plot_eigenstate(self, k, xlim=None, ylim=None):
        eigenstates_array = self.eigenstates.array
        plt.style.use("dark_background")
        fig, ax = plt.subplots(figsize=(7, 7))

        L = self.eigenstates.extent / (2 * Å)
        ax.imshow(complex_to_rgb(eigenstates_array[k]), extent=[-L, L, -L, L], origin='lower')

        ax.set_title(r"$\Psi(x,y)$")
        ax.set_xlabel(r"$x$ [Å]")
        ax.set_ylabel(r"$y$ [Å]")

        plt.show()

    def slider_plot(self, xlim=None, ylim=None):
        pass  # Placeholder method to implement slider functionality later

    def animate(self):
        pass  # Placeholder method to satisfy abstract base class

    def superpositions(self):
        pass  # Placeholder method to satisfy abstract base class
