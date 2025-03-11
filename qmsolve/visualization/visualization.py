import numpy as np
from mayavi import mlab
from abc import ABC, abstractmethod  # Ensures ABC is imported
from ..util.colour_functions import complex_to_rgb
from ..util.constants import *

# 🔹 Define the Visualization base class
class Visualization(ABC):
    @abstractmethod
    def __init__(self, eigenstates):
        pass

    @abstractmethod
    def plot_eigenstate(self, k, contrast_vals):
        pass

    @abstractmethod
    def animate(self, contrast_vals):
        pass

    @abstractmethod
    def superpositions(self, states, contrast_vals, **kw):
        pass


class VisualizationSingleParticle3D(Visualization):
    def __init__(self, eigenstates):
        self.eigenstates = eigenstates
        self.plot_type = 'volume'
        self.scene = None  # 🔹 Expose scene attribute for external control

    def slider_plot(self):
        raise NotImplementedError

    def plot_eigenstate(self, k, contrast_vals=[0.1, 0.25]):
        eigenstates = self.eigenstates.array
        mlab.figure(1, bgcolor=(0, 0, 0), size=(700, 700))
        psi = eigenstates[k]

        if self.plot_type == 'volume':
            abs_max = np.amax(np.abs(eigenstates))
            psi = psi / abs_max

            L = self.eigenstates.extent / 2 / Å
            N = self.eigenstates.N

            vol = mlab.pipeline.volume(mlab.pipeline.scalar_field(psi))

            mlab.outline()
            mlab.axes(xlabel='x [Å]', ylabel='y [Å]', zlabel='z [Å]', nb_labels=6, ranges=(-L, L, -L, L, -L, L))
            φ = 30
            mlab.view(azimuth=φ, distance=N * 3.5)

            # 🔹 Store the Mayavi scene for external access
            self.scene = mlab.gcf().scene

            mlab.show()

    def animate(self, contrast_vals=[0.1, 0.25]):
        eigenstates = self.eigenstates.array
        mlab.figure(1, bgcolor=(0, 0, 0), size=(700, 700))

        if self.plot_type == 'volume':
            psi = eigenstates[0]
            abs_max = np.amax(np.abs(eigenstates))
            psi = psi / abs_max

            L = self.eigenstates.extent / 2 / Å
            N = self.eigenstates.N
            field = mlab.pipeline.scalar_field(psi)
            vol = mlab.pipeline.volume(field)

            mlab.outline()
            mlab.axes(xlabel='x [Å]', ylabel='y [Å]', zlabel='z [Å]', nb_labels=6, ranges=(-L, L, -L, L, -L, L))
            φ = 30
            mlab.view(azimuth=φ, distance=N * 3.5)

            # 🔹 Store the Mayavi scene for external access
            self.scene = mlab.gcf().scene

            @mlab.animate(delay=10)
            def animation():
                data = {'t': 0.0}
                while True:
                    data['t'] += 0.05
                    yield

            animation()
            mlab.show()

    def superpositions(self, states, contrast_vals=[0.1, 0.25], **kw):
        raise NotImplementedError


# 🔹 Restore `init_visualization()`
def init_visualization(eigenstates):
    """
    Initializes the correct visualization class based on the eigenstate type.
    """
    if eigenstates.type == "SingleParticle3D":
        return VisualizationSingleParticle3D(eigenstates)
    
    raise NotImplementedError("Visualization for this type is not implemented.")
