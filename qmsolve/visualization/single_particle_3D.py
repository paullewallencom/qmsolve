import numpy as np
from mayavi import mlab
from .visualization import Visualization
from ..util.colour_functions import complex_to_rgb
from ..util.constants import *

class VisualizationSingleParticle3D(Visualization):
    def __init__(self, eigenstates):
        self.eigenstates = eigenstates
        self.plot_type = 'volume'
        self.scene = None  # 🔹 Ensure `scene` is initialized

    def plot_eigenstate(self, k, contrast_vals=[0.1, 0.25]):
        eigenstates = self.eigenstates.array
        mlab.figure(1, bgcolor=(0, 0, 0), size=(700, 700))
        psi = eigenstates[k]

        if self.plot_type == 'volume':
            abs_max = np.amax(np.abs(eigenstates))
            psi = psi / abs_max

            vol = mlab.pipeline.volume(mlab.pipeline.scalar_field(psi))

            mlab.outline()
            mlab.axes(xlabel='x [Å]', ylabel='y [Å]', zlabel='z [Å]', nb_labels=6)

            # 🔹 Assign the Mayavi scene to `self.scene`
            self.scene = mlab.gcf().scene  

            mlab.show()

    def animate(self, contrast_vals=[0.1, 0.25]):
        """🔹 Placeholder implementation to satisfy the abstract class requirement."""
        pass  # Implement animation logic later if needed

    def superpositions(self, states, contrast_vals=[0.1, 0.25], **kw):
        """🔹 Placeholder implementation to satisfy the abstract class requirement."""
        pass  # Implement superpositions logic later if needed
