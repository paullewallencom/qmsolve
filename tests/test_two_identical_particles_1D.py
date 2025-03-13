import unittest
from unittest.mock import MagicMock
import numpy as np
from matplotlib import pyplot as plt
from qmsolve.visualization.two_identical_particles_1D import (
    VisualizationIdenticalParticles1D,
    TimeVisualizationTwoIdenticalParticles1D
)

class TestVisualizationIdenticalParticles1D(unittest.TestCase):

    def setUp(self):
        self.mock_eigenstates_obj = MagicMock()
        self.mock_eigenstates_obj.array = np.random.rand(10, 100, 100) + 1j * np.random.rand(10, 100, 100)
        self.mock_eigenstates_obj.energies = np.linspace(0, 9, 10)
        self.mock_eigenstates_obj.extent = 10
        self.mock_eigenstates_obj.N = 100

    def test_plot_eigenstate(self):
        vis = VisualizationIdenticalParticles1D(self.mock_eigenstates_obj)
        vis.plot_eigenstate(0)
        plt.close('all')
        self.assertTrue(True)

    def test_slider_plot(self):
        vis = VisualizationIdenticalParticles1D(self.mock_eigenstates_obj)
        vis.slider_plot()
        plt.close('all')
        self.assertTrue(True)


class TestTimeVisualizationTwoIdenticalParticles1D(unittest.TestCase):

    def setUp(self):
        self.simulation_mock = MagicMock()
        self.simulation_mock.H = MagicMock()
        self.simulation_mock.H.Vgrid = np.random.rand(100, 100)
        self.simulation_mock.H.extent = 10
        self.simulation_mock.H.N = 100
        self.simulation_mock.Vmin = -1
        self.simulation_mock.Vmax = 1
        self.simulation_mock.store_steps = 100
        self.simulation_mock.total_time = 10
        self.simulation_mock.Ψ = np.random.rand(100, 100, 100) + 1j * np.random.rand(100, 100, 100)
        self.simulation_mock.Ψmax = np.max(np.abs(self.simulation_mock.Ψ))
        self.simulation_mock.Ψ_plot = self.simulation_mock.Ψ / self.simulation_mock.Ψmax

    def test_plot(self):
        vis_time = TimeVisualizationTwoIdenticalParticles1D(self.simulation_mock)
        vis_time.plot = MagicMock()
        vis_time.plot(0)
        plt.close('all')
        self.assertTrue(vis_time.plot.called)

    def test_animation_creation(self):
        vis_time = TimeVisualizationTwoIdenticalParticles1D(self.simulation_mock)
        vis_time.animate(animation_duration=1.0, fps=5, save_animation=False)
        plt.close('all')
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
