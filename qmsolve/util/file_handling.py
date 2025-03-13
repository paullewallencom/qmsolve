# Used for loading and storing eigenstates in large computations. Requires h5py package
import numpy as np
from ..eigenstates import Eigenstates
import h5py

def save_eigenstates(eigenstates, name: str):
    """Save an Eigenstates object to an HDF5 file."""
    with h5py.File(name, 'w') as f:  # 'w' mode ensures a clean save
        f.create_dataset('energies', data=eigenstates.eigenvalues)
        f.create_dataset('array', data=eigenstates.eigenvectors)
        f.attrs['extent'] = float(eigenstates.extent)  # Explicit float conversion
        f.attrs['N'] = int(eigenstates.N)  # Explicit int conversion
        f.attrs['potential_type'] = str(eigenstates.potential_type)  # Ensure string

def load_eigenstates(name: str):
    """Load an Eigenstates object from an HDF5 file."""
    with h5py.File(name, 'r') as f:  # Use 'r' mode to prevent unintended writes
        eigenvalues = np.array(f['energies'])
        eigenvectors = np.array(f['array'])
        extent = float(f.attrs['extent'])  # Ensure this is a float
        N = int(f.attrs['N'])  # Ensure this is an integer
        potential_type = str(f.attrs['potential_type'])  # Ensure it's a string
    return Eigenstates(eigenvalues, eigenvectors, extent, N, potential_type)
