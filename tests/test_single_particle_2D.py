import unittest
from unittest.mock import MagicMock
import numpy as np
from matplotlib import pyplot as plt
from qmsolve.visualization.single_particle_2D import VisualizationSingleParticle2D


class TestVisualizationSingleParticle2D(unittest.TestCase):

    def setUp(self):
        self.mock_eigenstates_obj = MagicMock()
        self.mock_eigenstates_obj.array = np.random.rand(10, 100, 100) + 1j * np.random.rand(10, 100, 100)
        self.mock_eigenstates_obj.energies = np.linspace(0, 9, 10)
        self.mock_eigenstates_obj.extent = 10
        self.mock_eigenstates_obj.N = 100

    def test_plot_eigenstate(self):
        vis = VisualizationSingleParticle2D(self.mock_eigenstates_obj)
        vis.plot_eigenstate(0)
        plt.close('all')
        self.assertTrue(True, "plot_eigenstate executed successfully.")

    def test_slider_plot(self):
        vis = VisualizationSingleParticle2D(self.mock_eigenstates_obj)
        vis.slider_plot()
        plt.close('all')
        self.assertTrue(True, "slider_plot executed successfully.")

    def test_animate(self):
        vis = VisualizationSingleParticle2D(self.mock_eigenstates_obj)
        vis.animate()
        plt.close('all')
        self.assertTrue(True, "animate placeholder executed successfully.")

    def test_superpositions(self):
        vis = VisualizationSingleParticle2D(self.mock_eigenstates_obj)
        vis.superpositions()
        plt.close('all')
        self.assertTrue(True, "superpositions placeholder executed successfully.")


if __name__ == '__main__':
    unittest.main()
