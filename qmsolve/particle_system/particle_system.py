import numpy as np


class ParticleSystem:
    """Represents a system of particles with properties like mass, charge, and position."""

    def __init__(self, particles=None):
        """
        Initialize the particle system with a list of particles.

        Args:
            particles (list): List of particle dictionaries with "mass", "charge", and "position".
        """
        self.particles = particles if particles else []

    def add_particle(self, mass, charge, position):
        """Add a new particle to the system."""
        self.particles.append(
            {"mass": mass, "charge": charge, "position": np.array(position)}
        )

    def get_particle_count(self):
        """Return the total number of particles in the system."""
        return len(self.particles)

    def get_total_mass(self):
        """Compute and return the total mass of the system."""
        return sum(p["mass"] for p in self.particles)

    def get_center_of_mass(self):
        """Compute and return the center of mass of the system."""
        total_mass = self.get_total_mass()
        if total_mass == 0:
            return np.zeros(3)
        return sum(p["mass"] * p["position"] for p in self.particles) / total_mass

    def apply_force(self, index, force):
        """Apply a force vector to a specific particle, adjusting its position."""
        if index < 0 or index >= len(self.particles):
            raise IndexError("Invalid particle index")
        self.particles[index]["position"] += force  # Simple displacement for testing

    def compute_interactions(self):
        """Dummy function to simulate particle interactions. Returns an array of forces."""
        return np.zeros((len(self.particles), 3))

    def __str__(self):
        return f"ParticleSystem with {self.get_particle_count()} particles"

if __name__ == "__main__":
    # Example usage for debugging purposes
    ps = ParticleSystem()
    ps.add_particle(1.0, -1.0, [0, 0, 0])
    ps.add_particle(1.5, 1.0, [1, 0, 0])
    print(ps)
