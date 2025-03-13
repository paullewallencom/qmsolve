import unittest
import qmsolve.util.constants as constants

class TestConstants(unittest.TestCase):

    def test_atomic_units(self):
        """Verify atomic unit conversion constants."""
        self.assertEqual(constants.hbar, 1.0)
        self.assertEqual(constants.m_e, 1.0)
        self.assertEqual(constants.a_0, 1.0)
        self.assertEqual(constants.e, 1.0)
        self.assertEqual(constants.hartree, 1.0)
        self.assertEqual(constants.Eh, constants.hartree)

    def test_length_units(self):
        """Check length unit conversions."""
        self.assertAlmostEqual(constants.nm, 1.8897261246257702e1)
        self.assertAlmostEqual(constants.Å, 1.8897261246257702)

    def test_energy_units(self):
        """Check energy unit conversions."""
        self.assertAlmostEqual(constants.eV, 0.03674932217565499)
        self.assertAlmostEqual(constants.V, 0.03674932217565499)

    def test_time_units(self):
        """Check time unit conversions."""
        self.assertAlmostEqual(constants.ps, 4.134137333518212e4)
        self.assertAlmostEqual(constants.picoseconds, constants.ps)
        self.assertAlmostEqual(constants.fs, 4.134137333518212 * 10)
        self.assertAlmostEqual(constants.femtoseconds, constants.fs)

    def test_physical_constants(self):
        """Check physical constants in atomic units."""
        self.assertAlmostEqual(constants.k, 0.5)
        self.assertAlmostEqual(constants.m_p, 1836.1526734400013)
        self.assertAlmostEqual(constants.𝜇0, 0.0006691762566207213)
        self.assertAlmostEqual(constants.ε0, 0.0795774715459477)
        self.assertAlmostEqual(constants.c, 137.035999083818)
        self.assertAlmostEqual(constants.α, 0.0072973525693)

    def test_misc_units(self):
        """Check miscellaneous unit conversions."""
        self.assertAlmostEqual(constants.V_m, 1.9446903811488876e-12)
        self.assertAlmostEqual(constants.T, 4.254382157326325e-06)
        self.assertAlmostEqual(constants.m, 1.8897261246257702e10)
        self.assertAlmostEqual(constants.C, 6.241509074460763e+18)
        self.assertAlmostEqual(constants.s, 4.134137333518173e+16)
        self.assertAlmostEqual(constants.Hz, 2.4188843265857225e-17)
        self.assertAlmostEqual(constants.kg, 1.0977691057577634e30)
        self.assertAlmostEqual(constants.J, 2.293712278396328e+17)
        self.assertAlmostEqual(constants.A, 150.974884744557)

if __name__ == '__main__':
    unittest.main()
