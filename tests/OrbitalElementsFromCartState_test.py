#DocString with Sphinx syntax


import unittest
import OrbitalElementsFromCartState
import sys
from os.path import expanduser
sys.path.append(expanduser("~") + "/adam_home/SEE_functions")


class Test_OrbitalElementsFromCartState(unittest.TestCase):
    '''
    .. module:: Orbital Elements from Cartesian State unit tests
    .. moduleauthor:: Emmie King <emmie@see.com>
    .. versionadded:: 1

    '''

    def test_OrbitPeriodFromSma(self):
        """This function does something.

        :param name: The name to use.
        :type name: str.
        :param state: Current state to be in.
        :type state: bool.
        :returns:  int -- the return code.
        :raises: AttributeError, KeyError

        """
        # AlmostEqual rounding to the 8th decimal
        # solution from python method
        # self.assertAlmostEqual(OrbitalElementsFromCartState.OrbitPeriodFromSma(
        # 175521278.778045,398600.5*1000000000), 731822.2514286994)
        # solution from excel macro
        self.assertAlmostEqual(OrbitalElementsFromCartState.OrbitPeriodFromSma(
            175521278.778045, 398600.5 * 1000000000), 731822.2514287010, 8)

        # Error handling
        # option 1:
        # self.assertRaises(ZeroDivisionError,
        # OrbitalElementsFromCartState.OrbitPeriodFromSma, 16, 0)
        # option 2: use context manager
        with self.assertRaises(ZeroDivisionError):
            OrbitalElementsFromCartState.OrbitPeriodFromSma(175521278.778045, 0)

        with self.assertRaises(ValueError):
            OrbitalElementsFromCartState.OrbitPeriodFromSma(-16, 398600.5 * 1000000000)

        with self.assertRaises(ValueError):
            OrbitalElementsFromCartState.OrbitPeriodFromSma(175521278.778045, -10)

        with self.assertRaises(ValueError):
            OrbitalElementsFromCartState.OrbitPeriodFromSma(0, 398600.5 * 1000000000)

    def test_SemimajorAxisFromCartState(self):
        self.assertAlmostEqual(OrbitalElementsFromCartState.SemimajorAxisFromCartState(
            164335595.593791, 1606.26969960476, 398600.5 * 1000000000), 175521278.77804464, 8)
        with self.assertRaises(ZeroDivisionError):
            OrbitalElementsFromCartState.SemimajorAxisFromCartState(
                0, 1606.26969960476, 398600.5 * 1000000000)

    def test_OrbitEnergyFromCartState(self):
        self.assertAlmostEqual(OrbitalElementsFromCartState.OrbitEnergyFromCartState(
            164335595.593791, 1606.26969960476, 398600.5 * 1000000000), -1135476.28747637, 7)
        with self.assertRaises(ZeroDivisionError):
            OrbitalElementsFromCartState.OrbitEnergyFromCartState(
                0, 1606.26969960476, 398600.5 * 1000000000)


if __name__ == '__main__':
    unittest.main()
