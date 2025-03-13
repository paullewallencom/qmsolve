import unittest
import numpy as np
import matplotlib.pyplot as plt
from unittest.mock import patch, MagicMock
from qmsolve.visualization.single_particle_1D import VisualizationSingleParticle1D

class MockEigenstates:
    """Mock class for Eigenstates to use in tests."""
    def __init__(self):
        self.eigenvalues = np.array([1.0, 2.0, 3.0])
        self.eigenvectors = np.array([
            np.sin(np.linspace(0, np.pi, 100)), 
            np.cos(np.linspace(0, np.pi, 100)), 
            np.tan(np.linspace(0, np.pi/4, 100))
        ])
        self.extent = 10.0
        self.N = 100

class TestVisualizationSingleParticle1D(unittest.TestCase):

    def setUp(self):
        """Set up a mock eigenstates object for testing."""
        self.eigenstates = MockEigenstates()
        self.visualization = VisualizationSingleParticle1D(self.eigenstates)

    def test_initialization(self):
        """Test that the class initializes correctly."""
        self.assertEqual(self.visualization.eigenstates, self.eigenstates)

    @patch("matplotlib.pyplot.show")
    def test_plot_eigenstate(self, mock_show):
        """Test plot_eigenstate method without rendering the plot."""
        with patch.object(plt, "figure", return_value=MagicMock()):
            self.visualization.plot_eigenstate(k=0, xlim=[-5, 5])
        mock_show.assert_called_once()

    @patch("matplotlib.pyplot.show")
    def test_animate(self, mock_show):
        """Test animate method without rendering animation."""
        with patch.object(plt, "figure", return_value=MagicMock()):
            self.visualization.animate(seconds_per_eigenstate=0.5, fps=20, max_states=2, save_animation=False)
        mock_show.assert_called_once()

if __name__ == '__main__':
    unittest.main()
