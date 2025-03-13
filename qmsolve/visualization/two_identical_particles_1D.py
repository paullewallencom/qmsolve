import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from .visualization import Visualization, TimeVisualization
from ..util.colour_functions import complex_to_rgb, complex_to_rgba
from ..util.constants import Å, femtoseconds

class VisualizationIdenticalParticles1D(Visualization):
    def __init__(self, eigenstates):
        self.eigenstates = eigenstates

    def plot_eigenstate(self, k, xlim=None):
        eigenstates_array = self.eigenstates.array
        plt.style.use("dark_background")

        fig, ax = plt.subplots(figsize=(7, 7))
        L = self.eigenstates.extent / (2 * Å)
        ax.imshow(complex_to_rgb(eigenstates_array[k]), extent=[-L, L, -L, L], origin='lower')

        ax.set_title(r"$\Psi(x_1, x_2)$")
        ax.set_xlabel(r"$x_1$ [Å]")
        ax.set_ylabel(r"$x_2$ [Å]")

        if xlim:
            ax.set_xlim(xlim)
            ax.set_ylim(xlim)

        plt.show()

    def slider_plot(self, xlim=None):
        # Placeholder for slider plot functionality
        pass

    def animate(self):
        # Placeholder
        pass

    def superpositions(self):
        # Placeholder
        pass


class TimeVisualizationTwoIdenticalParticles1D(TimeVisualization):
    def __init__(self, simulation):
        self.simulation = simulation
        self.H = simulation.H

    def plot(self, t_index, figsize=(10, 5)):
        plt.style.use("dark_background")

        fig, ax = plt.subplots(figsize=figsize)
        L = self.simulation.H.extent / Å

        potential_plot = (self.simulation.H.Vgrid - self.simulation.Vmin) / (self.simulation.Vmax - self.simulation.Vmin)
        ax.imshow(potential_plot, origin="lower", extent=[-L / 2, L / 2, -L / 2, L / 2], cmap="gray")

        wavefunction_plot = complex_to_rgba(self.simulation.Ψ_plot[t_index])
        ax.imshow(wavefunction_plot, origin="lower", extent=[-L / 2, L / 2, -L / 2, L / 2])

        ax.set_title(r"$\psi(x_1,x_2)$")
        ax.set_xlabel(r"$x_1$ [Å]")
        ax.set_ylabel(r"$x_2$ [Å]")

        plt.show()

    def animate(self, animation_duration=5, fps=20, save_animation=False):
        total_frames = int(animation_duration * fps)

        plt.style.use("dark_background")
        fig, ax = plt.subplots(figsize=(7, 7))
        L = self.simulation.H.extent / Å

        potential_plot = (self.simulation.H.Vgrid - self.simulation.Vmin) / (self.simulation.Vmax - self.simulation.Vmin)
        ax.imshow(potential_plot, cmap="gray", origin="lower", extent=[-L/2, L/2, -L/2, L/2])

        wavefunction_img = ax.imshow(complex_to_rgba(self.simulation.Ψ_plot[0]), origin="lower",
                                     extent=[-L / 2, L / 2, -L / 2, L / 2])

        def animate(frame):
            t_idx = int(frame * self.simulation.store_steps / total_frames)
            wavefunction_img.set_data(complex_to_rgba(self.simulation.Ψ_plot[t_idx]))
            return (wavefunction_img,)

        ani = animation.FuncAnimation(fig, animate, frames=total_frames, interval=1000/fps, blit=True)

        if save_animation:
            ani.save("animation.mp4", writer="ffmpeg")
        else:
            plt.show()
