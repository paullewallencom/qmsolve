# Import necessary modules without causing circular dependencies
from .hamiltonian import Hamiltonian
from .eigenstates import Eigenstates
from .time_dependent_solver import crank_nicolson
from qmsolve.util.colour_functions import complex_to_rgb, complex_to_rgba
from .visualization import visualization

# Delay importing particle_system and eigenstates to avoid circular import
# These will be available when explicitly imported elsewhere
__all__ = [
    "Eigenstates",
    "particle_system",
    "time_dependent_solver",
    "util",
    "visualization"
]
