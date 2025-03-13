import unittest
import numpy as np
from matplotlib.colors import hsv_to_rgb
from qmsolve.util.colour_functions import complex_to_rgb, complex_to_rgba


class TestColourFunctions(unittest.TestCase):

    def test_complex_to_rgb(self):
        """Test complex_to_rgb function with known inputs."""
        Z = np.array([1 + 1j, -1 - 1j, 1 - 1j, -1 + 1j])
        expected_shapes = (4, 3)  # Expected shape (N, 3) for RGB values
        
        rgb = complex_to_rgb(Z)

        self.assertEqual(rgb.shape, expected_shapes, "RGB output shape mismatch")
        self.assertTrue(np.all((rgb >= 0) & (rgb <= 1)), "RGB values should be in [0,1] range")

    def test_complex_to_rgb_single_value(self):
        """Test complex_to_rgb with a single complex number."""
        Z = np.array([1 + 1j])
        rgb = complex_to_rgb(Z)
        
        self.assertEqual(rgb.shape, (1, 3), "Single value should return shape (1,3)")
        self.assertTrue(np.all((rgb >= 0) & (rgb <= 1)), "RGB values should be within valid range")

    def test_complex_to_rgba(self):
        """Test complex_to_rgba function with known inputs."""
        Z = np.array([1 + 1j, -1 - 1j, 1 - 1j, -1 + 1j])
        max_val = 2.0
        expected_shapes = (4, 4)  # Expected shape (N, 4) for RGBA values
        
        rgba = complex_to_rgba(Z, max_val=max_val)

        self.assertEqual(rgba.shape, expected_shapes, "RGBA output shape mismatch")
        self.assertTrue(np.all((rgba[:, :3] >= 0) & (rgba[:, :3] <= 1)), "RGB values should be in [0,1] range")
        self.assertTrue(np.all((rgba[:, 3] >= 0) & (rgba[:, 3] <= 1)), "Alpha values should be in [0,1] range")

    def test_complex_to_rgba_alpha_scaling(self):
        """Test complex_to_rgba alpha channel scaling."""
        Z = np.array([0.5 + 0.5j, 1 + 1j, 2 + 2j, 3 + 3j])
        max_val = 2.0
        rgba = complex_to_rgba(Z, max_val=max_val)
        
        self.assertTrue(np.all(rgba[:, 3] <= 1), "Alpha values should be capped at 1.0")
        self.assertTrue(np.all(rgba[:, 3] >= 0), "Alpha values should be non-negative")

if __name__ == '__main__':
    unittest.main()
