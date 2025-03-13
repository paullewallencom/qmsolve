import unittest
import numpy as np
import h5py
import os
from qmsolve.eigenstates import Eigenstates
from qmsolve.util.file_handling import save_eigenstates, load_eigenstates

class TestFileHandling(unittest.TestCase):

    def setUp(self):
        """Create a temporary Eigenstates object for testing."""
        self.test_filename = "test_eigenstates.h5"
        self.eigenvalues = np.array([1.0, 2.0, 3.0])
        self.eigenvectors = np.array([[1, 2], [3, 4]])
        self.extent = 10.0  # Explicit float to match class expectations
        self.N = 100  # Explicit int
        self.potential_type = "grid"  # Valid value ("grid" or "matrix")

        self.eigenstates = Eigenstates(
            self.eigenvalues, self.eigenvectors, self.extent, self.N, self.potential_type
        )

    def tearDown(self):
        """Remove test file after each test."""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_save_and_load_eigenstates(self):
        """Test saving and loading Eigenstates objects."""
        save_eigenstates(self.eigenstates, self.test_filename)
        loaded_eigenstates = load_eigenstates(self.test_filename)

        np.testing.assert_array_equal(loaded_eigenstates.eigenvalues, self.eigenvalues)
        np.testing.assert_array_equal(loaded_eigenstates.eigenvectors, self.eigenvectors)
        self.assertEqual(loaded_eigenstates.extent, self.extent)
        self.assertEqual(loaded_eigenstates.N, self.N)
        self.assertEqual(loaded_eigenstates.potential_type, self.potential_type)

    def test_hdf5_file_content(self):
        """Verify the actual contents of the saved HDF5 file."""
        save_eigenstates(self.eigenstates, self.test_filename)

        with h5py.File(self.test_filename, 'r') as f:
            np.testing.assert_array_equal(f['energies'], self.eigenvalues)
            np.testing.assert_array_equal(f['array'], self.eigenvectors)
            self.assertEqual(float(f.attrs['extent']), self.extent)  # Ensure float conversion
            self.assertEqual(int(f.attrs['N']), self.N)  # Ensure int conversion
            self.assertEqual(str(f.attrs['potential_type']), self.potential_type)  # Ensure string

if __name__ == '__main__':
    unittest.main()
