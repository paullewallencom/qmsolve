# qmsolve/particle_system/__init__.py

def get_particle_system():
    from .particle_system import ParticleSystem  # Delayed import
    return ParticleSystem


def get_single_particle():
    from .single_particle import SingleParticle
    return SingleParticle


def get_two_bosons():
    from .two_bosons import TwoBosons
    return TwoBosons


def get_two_particles():
    from .two_particles import TwoParticles
    return TwoParticles


# Define a dynamic attribute to make ParticleSystem accessible in tests
import sys
import types

module = sys.modules[__name__]
module.ParticleSystem = get_particle_system()

# Explicitly expose these in __all__
__all__ = ["ParticleSystem", "get_single_particle",
           "get_two_bosons", "get_two_particles"]
